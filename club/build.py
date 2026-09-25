#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Erzeugt alle Vereinsdokumente als PDF im angegebenen Zielordner.

    build-club ZIELORDNER                  # Entwurfsfassung (config.DRAFT), alle Dokumente
    build-club ZIELORDNER --final          # Einreichungsfassung: ohne Hinweise, ohne Entwurfs-Fußzeile
    build-club ZIELORDNER satzung          # nur ein Dokument
    build-club ZIELORDNER --stand 16.09.2026
"""
import argparse
import importlib
from pathlib import Path

from . import config

DOCS = ["satzung", "protokoll", "beitragsordnung", "ausleihordnung", "leihvertrag"]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("output_dir", type=Path, help="Zielordner für die erzeugten PDFs")
    ap.add_argument("docs", nargs="*", choices=DOCS, metavar="DOC",
                     help="Dokumente (Standard: alle; mögliche Werte: %s)" % ", ".join(DOCS))
    ap.add_argument("--final", action="store_true", help="Einreichungsfassung erzeugen")
    ap.add_argument("--stand", help="Datum der Fußzeile überschreiben, z. B. 16.09.2026")
    args = ap.parse_args()

    config.OUT_DIR = args.output_dir
    if args.final:
        config.DRAFT = False
    if args.stand:
        config.STAND = args.stand

    for name in args.docs or DOCS:
        importlib.import_module(f".{name}", __package__)

    print("\nAusgabe in %s (%s)" % (config.OUT_DIR, "Einreichungsfassung" if not config.DRAFT else "Entwurf"))
    for p in sorted(config.OUT_DIR.glob("*.pdf")):
        print("  ", p.name)


if __name__ == "__main__":
    main()
