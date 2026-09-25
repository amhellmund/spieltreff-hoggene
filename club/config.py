# -*- coding: utf-8 -*-
"""Zentrale Konfiguration. Alles, was sich zwischen Verein, Fassung und
Zeitpunkt ändert, steht hier – die Dokumentskripte lesen nur."""
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# --- Verein ---------------------------------------------------------------
VEREINSNAME = "Spieltreff Hoggene"
SITZ = "Hockenheim"
REGISTERGERICHT = "Amtsgericht Mannheim"
FINANZAMT = "Finanzamt Schwetzingen"

# Anfallberechtigte bei Auflösung (§ 18 Abs. 3 Satzung). Der zweite Teil
# ergänzt die Pflichtformulierung der Mustersatzung, ohne sie anzutasten.
BEGUENSTIGTE = "die Stadt Hockenheim"
BEGUENSTIGTE_ZWECK = "insbesondere zur Förderung der Jugendarbeit und der Bildung"

# --- Beträge --------------------------------------------------------------
INNENBINDUNG_EUR = "1.000"          # § 8 Abs. 7 Satzung
BEITRAEGE = [                       # Beitragsordnung § 2
    ("Ordentliche Mitgliedschaft (Erwachsene)", "24,00 EUR"),
    ("Ermäßigte Mitgliedschaft", "12,00 EUR"),
    ("Familienmitgliedschaft", "40,00 EUR"),
    ("Fördermitgliedschaft (Mindestbeitrag)", "50,00 EUR"),
    ("Juristische Personen (Mindestbeitrag)", "100,00 EUR"),
]
BEITRAG_FAELLIG = "1. März"
AUSLEIHGEBUEHREN = [                # Ausleihordnung § 4
    ("Ausleihe je Titel, bis 14 Tage", "1,00 EUR", "3,00 EUR"),
    ("Verlängerung je 14 Tage", "1,00 EUR", "3,00 EUR"),
    ("Kaution je Titel (rückzahlbar)", "keine", "10,00 EUR"),
    ("Säumnisgebühr je angefangene Woche", "1,00 EUR", "2,00 EUR"),
]

# --- Fassung --------------------------------------------------------------
# DRAFT=True : kursive Hinweise im Text, Fußzeile "Entwurf, Stand …"
# DRAFT=False: Einreichungsfassung – keine Hinweise, keine Entwurfs-Fußzeile
DRAFT = True
STAND = date.today().strftime("%d.%m.%Y")

# --- Pfade ----------------------------------------------------------------
LOGO = ROOT.parent / "images" / "logo-icon.png"  # zentrales Website-Logo
OUT_DIR = ROOT / "build"  # Standard; wird von build.py per Argument überschrieben
