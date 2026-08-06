"""Loads YAML data files and computes derived, build-time-only values
(event past/next/future status, German date formatting, sorted games)."""

import datetime
from pathlib import Path

import yaml

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

KNOWN_CATEGORIES = {"Familie", "Kenner", "Party", "Kinder", "Experte"}

EVENT_TYPE_INFO = {
    "spieltreff": {"label": "Spieltreff", "page": "events/spieltreff.html"},
    "brett-vorm-kopf": {"label": "Brett vorm Kopf", "page": "events/brett-vorm-kopf.html"},
    "brett-am-ring": {"label": "Brett am Ring", "page": "events/brett-am-ring.html"},
}

KNOWN_EVENT_TYPES = set(EVENT_TYPE_INFO)

GERMAN_MONTHS = [
    "Januar", "Februar", "März", "April", "Mai", "Juni",
    "Juli", "August", "September", "Oktober", "November", "Dezember",
]


def _load_yaml(name):
    with open(DATA_DIR / name, encoding="utf-8") as f:
        return yaml.safe_load(f)


def format_german_date(date):
    return f"{date.day}. {GERMAN_MONTHS[date.month - 1]} {date.year}"


def format_german_date_range(date_start, date_end):
    if date_start == date_end:
        return format_german_date(date_start)
    if (date_start.year, date_start.month) == (date_end.year, date_end.month):
        return f"{date_start.day}.–{date_end.day}. {GERMAN_MONTHS[date_start.month - 1]} {date_start.year}"
    return f"{format_german_date(date_start)} – {format_german_date(date_end)}"


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
        event.setdefault("date_end", event["date"])
        if "days" not in event:
            # Single-day event: synthesize the one-entry `days` list so
            # templates can treat every event uniformly.
            event["days"] = [{
                "date": event["date"],
                "time_start": event["time_start"],
                "time_end": event["time_end"],
            }]
        for day in event["days"]:
            day["date_display"] = format_german_date(day["date"])
        event["date_display"] = format_german_date_range(event["date"], event["date_end"])
        event["type_label"] = EVENT_TYPE_INFO[event["type"]]["label"]
        event["type_page"] = EVENT_TYPE_INFO[event["type"]]["page"]
    events.sort(key=lambda e: e["date"])

    # A multi-day event is only "past" once its last day has passed, and
    # stays the "next" event until then too.
    future_or_today = [e for e in events if e["date_end"] >= today]
    next_event = future_or_today[0] if future_or_today else None

    for event in events:
        if event is next_event:
            event["status"] = "next"
        elif event["date_end"] < today:
            event["status"] = "past"
        else:
            event["status"] = "future"

    return events, next_event
