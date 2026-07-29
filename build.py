#!/usr/bin/env python3
"""Static site generator entry point. Run with: uv run build.py"""

import argparse
import datetime
import shutil
from pathlib import Path

from generator.context import load_events, load_footer, load_games, load_nav, load_site
from generator.render import OUTPUT_DIR, render_page

ROOT_DIR = Path(__file__).resolve().parent
STATIC_ASSETS = ["css", "images", "favicon.ico"]


def clear_output_dir():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for entry in OUTPUT_DIR.iterdir():
        if entry.is_dir() and not entry.is_symlink():
            shutil.rmtree(entry)
        else:
            entry.unlink()


def copy_static_assets():
    for name in STATIC_ASSETS:
        src = ROOT_DIR / name
        dst = OUTPUT_DIR / name
        if src.is_dir():
            shutil.copytree(src, dst, dirs_exist_ok=True)
        else:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--today",
        type=datetime.date.fromisoformat,
        default=None,
        help="Override 'today' for past/next/future computation (YYYY-MM-DD). Defaults to the real current date.",
    )
    args = parser.parse_args()

    clear_output_dir()
    copy_static_assets()

    site = load_site()
    nav = load_nav()
    footer = load_footer()
    games = load_games()
    all_events, next_event = load_events(today=args.today)
    upcoming_events = [e for e in all_events if e["status"] != "past"]
    spieltreff_events, spieltreff_next_event = load_events(today=args.today, type="spieltreff")
    _, brett_vorm_kopf_next_event = load_events(today=args.today, type="brett-vorm-kopf")

    render_page("home.html", "index.html", site, nav, footer,
                page_title="Spieltreff Hoggene", title="Spieltreff Hoggene",
                events=upcoming_events, next_event=next_event)

    render_page("spieltreff.html", "events/spieltreff.html", site, nav, footer,
                page_title="Spieltreff", events=spieltreff_events,
                next_event=spieltreff_next_event)

    render_page("brett-vorm-kopf.html", "events/brett-vorm-kopf.html", site, nav, footer,
                page_title="Brett vorm Kopf", title="Brett vorm Kopf",
                next_event=brett_vorm_kopf_next_event)

    render_page("stub.html", "events/brett-am-ring.html", site, nav, footer,
                page_title="Brett-am-Ring", title="Brett-am-Ring")

    render_page("games.html", "games.html", site, nav, footer,
                page_title="Spiele", games=games)

    render_page("verein.html", "verein.html", site, nav, footer,
                page_title="Verein", title="Verein")

    render_page("contact.html", "contact.html", site, nav, footer,
                page_title="Kontakt & Impressum")


if __name__ == "__main__":
    main()
