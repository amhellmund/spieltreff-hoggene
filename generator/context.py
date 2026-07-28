"""Loads YAML data files and computes derived, build-time-only values
(event past/next/future status, German date formatting, sorted games)."""

import datetime
from pathlib import Path

import yaml

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

KNOWN_CATEGORIES = {"Familie", "Kenner", "Party", "Kinder", "Experte"}

KNOWN_EVENT_TYPES = {"spieltreff", "brett-vorm-kopf", "brett-am-ring"}

GERMAN_MONTHS = [
    "Januar", "Februar", "März", "April", "Mai", "Juni",
    "Juli", "August", "September", "Oktober", "November", "Dezember",
]


def _load_yaml(name):
    with open(DATA_DIR / name, encoding="utf-8") as f:
        return yaml.safe_load(f)


def format_german_date(date):
    return f"{date.day}. {GERMAN_MONTHS[date.month - 1]} {date.year}"


def load_site():
    return _load_yaml("site.yaml")["site"]


def load_nav():
    return _load_yaml("site.yaml")["nav"]


def load_footer():
    return _load_yaml("site.yaml")["footer"]


def load_games():
    games = _load_yaml("games.yaml")["games"]
    for game in games:
        if game["category"] not in KNOWN_CATEGORIES:
            raise ValueError(
                f"Unknown category {game['category']!r} for game {game['name']!r}. "
                f"Must be one of {sorted(KNOWN_CATEGORIES)}."
            )
    games.sort(key=lambda g: g["name"].casefold())
    return games


def load_events(today=None, type=None):
    today = today or datetime.date.today()
    events = _load_yaml("events.yaml")["events"]
    for event in events:
        if event["type"] not in KNOWN_EVENT_TYPES:
            raise ValueError(
                f"Unknown event type {event['type']!r} for event on {event['date']}. "
                f"Must be one of {sorted(KNOWN_EVENT_TYPES)}."
            )
    if type is not None:
        events = [e for e in events if e["type"] == type]
    for event in events:
        event["date_display"] = format_german_date(event["date"])
    events.sort(key=lambda e: e["date"])

    future_or_today = [e for e in events if e["date"] >= today]
    next_event = future_or_today[0] if future_or_today else None

    for event in events:
        if event is next_event:
            event["status"] = "next"
        elif event["date"] < today:
            event["status"] = "past"
        else:
            event["status"] = "future"

    return events, next_event
