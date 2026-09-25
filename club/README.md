# Vereinsdokumente – Spieltreff Hoggene

Generiert alle Gründungsdokumente des Vereins als PDF aus Python-Quelltext.
Layout, Logo und Fußzeile sind zentral, Inhalte liegen je Dokument in `docs/`,
alles Veränderliche (Name, Beträge, Begünstigte, Fassung) in `config.py`.

## Dokumente

| Skript | Ausgabe | Beschließt |
|---|---|---|
| `satzung.py` | `Satzung.pdf` | Gründungsversammlung, einstimmig |
| `protokoll.py` | `Gruendungsprotokoll-Vorlage.pdf` | – (Vorlage nach Muster A des AG Mannheim) |
| `beitragsordnung.py` | `Beitragsordnung.pdf` | Mitgliederversammlung |
| `ausleihordnung.py` | `Archiv-und-Ausleihordnung.pdf` | Mitgliederversammlung |
| `leihvertrag.py` | `Leihvertrag-Spielesammlung.pdf` | Vorstandsmitglied, das nicht Leihgeber ist |

Im Entwurfsmodus tragen die Dateien den Zusatz `-Entwurf`.

## Installation

Das Skript ist als `build-club` in das Projekt (`pyproject.toml`) integriert:

```bash
uv sync
```

## Bauen

```bash
uv run build-club ZIELORDNER                      # Entwurf: mit kursiven Hinweisen und Fußzeile "Entwurf, Stand <heute>"
uv run build-club ZIELORDNER --final               # Einreichungsfassung: ohne Hinweise, ohne Entwurfs-Fußzeile
uv run build-club ZIELORDNER satzung protokoll     # nur einzelne Dokumente
uv run build-club ZIELORDNER --stand 16.09.2026    # Datum der Fußzeile festlegen
```

`ZIELORDNER` ist ein beliebiger, vom Aufrufer vorgegebener Ordner (wird bei Bedarf angelegt).

## Anpassen

- **Name, Sitz, Begünstigte, Beträge, Gebühren:** `config.py`
- **Fassung (Entwurf/Final):** `config.DRAFT` oder `--final`
- **Logo:** zentrales Website-Logo `../images/logo-icon.png`; das Seitenverhältnis steht in `layout.py` (`LOGO_RATIO`)
- **Inhalt eines Dokuments:** das jeweilige Skript im Ordner `club/`

Text wird als reportlab-Markup geschrieben: Umlaute und Sonderzeichen als HTML-Entities
(`&uuml;`, `&sect;`, `&nbsp;`), Hervorhebung mit `<b>…</b>`. Die Helfer:

- `para(nr, titel, *absaetze)` – ein Paragraph mit automatisch nummerierten Absätzen.
  Ein Tupel `("raw", text)` erzeugt einen eingerückten Absatz ohne Nummer (Aufzählungen),
  ein Tupel `("note", text)` einen kursiven Hinweis, der nur im Entwurf erscheint.
- `note(text)` – kursiver Hinweis außerhalb von `para`, nur im Entwurf.
- `grid(data, colw, rowh, ...)` – Tabelle mit Spaltenbreiten in mm.
- `sigblock([...])` – Unterschriftenzeilen.
- `logo_header()` – Logo für den Kopf der ersten Seite.

## Rechtlicher Hinweis

Die Texte sind Entwürfe und keine Rechtsberatung. Die Satzung ist gegen die Mustersatzung
nach Anlage 1 zu § 60 AO und gegen das Merkblatt des Amtsgerichts Mannheim abgeglichen,
aber weder vom Registergericht noch vom Finanzamt geprüft. Die Absätze, die wörtlich aus der
Mustersatzung stammen (§ 3, § 18 Abs. 3 der Satzung), dürfen nicht umformuliert werden.

## Struktur

```
club/
├── __init__.py
├── build.py             Baut alle oder einzelne Dokumente (Entry-Point build-club)
├── config.py            Alle veränderlichen Werte
├── layout.py            Seitenlayout, Styles, Logo, Helfer
├── satzung.py
├── protokoll.py
├── beitragsordnung.py
├── ausleihordnung.py
└── leihvertrag.py
```

Das Logo liegt zentral im Repository unter `images/logo-icon.png`.
