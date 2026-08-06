#!/usr/bin/env python3
"""Deploy the built site (.build/) to a remote server via SSH/SCP.

Run with: uv run deploy-page --host example.com --username deploy --deploy-dir /var/www/spieltreff
"""

import argparse
import getpass
import os
import sys
from pathlib import Path

import paramiko
from scp import SCPClient
from tqdm import tqdm

BUILD_DIR = Path(__file__).resolve().parent / ".build"
PASSWORD_ENV_VAR = "DEPLOY_PASSWORD"


def get_password():
    password = os.environ.get(PASSWORD_ENV_VAR)
    if password:
        return password
    return getpass.getpass("SSH password: ")


def clear_remote_dir(ssh, deploy_dir):
    quoted_dir = f"'{deploy_dir}'"
    stdin, stdout, stderr = ssh.exec_command(
        f"mkdir -p {quoted_dir} && rm -rf {quoted_dir}/* {quoted_dir}/.[!.]*"
    )
    exit_status = stdout.channel.recv_exit_status()
    if exit_status != 0:
        raise RuntimeError(f"Failed to clear remote directory: {stderr.read().decode()}")


def total_upload_size():
    return sum(f.stat().st_size for f in BUILD_DIR.rglob("*") if f.is_file())


def upload_build_dir(ssh, deploy_dir):
    state = {"filename": None, "file_sent": 0}

    with tqdm(total=total_upload_size(), unit="B", unit_scale=True, unit_divisor=1024,
              desc="Total", position=1, leave=True) as total_bar, \
         tqdm(total=0, unit="B", unit_scale=True, unit_divisor=1024,
              position=0, leave=True) as file_bar:

        def progress(filename, size, sent):
            filename = filename.decode() if isinstance(filename, bytes) else filename
            if filename != state["filename"]:
                state["filename"] = filename
                state["file_sent"] = 0
                file_bar.reset(total=size)
                file_bar.set_description(Path(filename).name, refresh=False)

            delta = sent - state["file_sent"]
            state["file_sent"] = sent
            if delta > 0:
                file_bar.update(delta)
                total_bar.update(delta)

        with SCPClient(ssh.get_transport(), progress=progress) as scp:
            for entry in BUILD_DIR.iterdir():
                scp.put(str(entry), remote_path=deploy_dir, recursive=entry.is_dir())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", required=True, help="Remote server hostname or IP")
    parser.add_argument("--username", required=True, help="SSH username")
    parser.add_argument("--deploy-dir", required=True, help="Remote deployment directory")
    parser.add_argument("--port", type=int, default=22, help="SSH port (default: 22)")
    args = parser.parse_args()
    args.host = args.host.strip()
    args.username = args.username.strip()
    args.deploy_dir = args.deploy_dir.strip()

    if not BUILD_DIR.is_dir():
        sys.exit(f"Build directory not found: {BUILD_DIR}. Run 'uv run build-page' first.")

    password = get_password()

    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.RejectPolicy())
    ssh.connect(args.host, port=args.port, username=args.username, password=password)

    try:
        print(f"Clearing {args.deploy_dir} on {args.host}...")
        clear_remote_dir(ssh, args.deploy_dir)

        print(f"Uploading {BUILD_DIR} to {args.deploy_dir}...")
        upload_build_dir(ssh, args.deploy_dir)

        print("Deployment complete.")
    finally:
        ssh.close()


if __name__ == "__main__":
    main()
