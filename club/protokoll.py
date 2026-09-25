# -*- coding: utf-8 -*-
from reportlab.platypus import Paragraph, Spacer, KeepTogether, PageBreak
from reportlab.lib.units import mm
from . import config
from .layout import logo_header, note, out, Doc, grid, sigblock, BODY, BODY_INDENT, NOTE, DOC_TITLE, DOC_SUB, TOP_HEAD

V = config.VEREINSNAME
S = logo_header() + [Paragraph("Protokoll der Gr&uuml;ndungsversammlung", DOC_TITLE),
     Paragraph("des %s" % V, DOC_SUB), Spacer(1, 5 * mm),
     *note("Aufbau nach Abschnitt&nbsp;A des Merkblatts des Amtsgerichts Mannheim. Alle in eckigen "
               "Klammern gesetzten Stellen sind auszuf&uuml;llen, alle Abstimmungsergebnisse "
               "zahlenm&auml;&szlig;ig anzugeben. Kursive Hinweise vor der Einreichung entfernen. "
               "Das Protokoll braucht keine Beglaubigung."), Spacer(1, 2 * mm)]

def kv(rows):
    return grid(rows, (48, 90), header=False, fs=9.2)

S += [kv([["Ort der Versammlung", "[Anschrift des Versammlungsorts], Hockenheim"],
          ["Tag der Versammlung", "[Datum]"],
          ["Beginn / Ende", "[Uhrzeit] Uhr / [Uhrzeit] Uhr"],
          ["Versammlungsleitung", "[Vor- und Nachname]"],
          ["Protokollf&uuml;hrung", "[Vor- und Nachname]"],
          ["Erschienene Gr&uuml;ndungsmitglieder", "[Zahl] Personen, siehe Anwesenheitsliste (Anlage&nbsp;1)"]]),
      Spacer(1, 4 * mm)]

def top(n, title, *paras):
    out = [Paragraph("TOP %d &ndash; %s" % (n, title), TOP_HEAD)]
    for p in paras:
        if isinstance(p, tuple) and p[0] == "note":
            out.append(Paragraph(p[1], NOTE))
        elif isinstance(p, tuple) and p[0] == "tbl":
            out.append(p[1]); out.append(Spacer(1, 2 * mm))
        else:
            out.append(Paragraph(p, BODY))
    return out

def vote(label="Abstimmungsergebnis"):
    return grid([[label, "Ja-Stimmen", "Nein-Stimmen", "Enthaltungen"],
                 ["", "[Zahl]", "[Zahl]", "[Zahl]"]], (50, 29, 29, 30), header=True, fs=8.8,
                align_center_cols=(1, 2, 3))

S += top(1, "Er&ouml;ffnung und Feststellungen",
    "[Vor- und Nachname] er&ouml;ffnet die Versammlung um [Uhrzeit] Uhr, begr&uuml;&szlig;t die "
    "Anwesenden und wird von diesen einstimmig zur Versammlungsleitung bestimmt. Die "
    "Versammlungsleitung bestimmt [Vor- und Nachname] zur Protokollf&uuml;hrung.",
    "Die Versammlungsleitung stellt fest, dass [Zahl] Gr&uuml;ndungsmitglieder erschienen sind. "
    "Die Anwesenheitsliste ist diesem Protokoll als Anlage&nbsp;1 beigef&uuml;gt. Die Tagesordnung "
    "wird bekanntgegeben; Einw&auml;nde werden nicht erhoben.")

S += top(2, "Beschluss &uuml;ber die Gr&uuml;ndung des Vereins",
    "Die Anwesenden beschlie&szlig;en, einen Verein mit dem Namen &bdquo;%s&ldquo; mit Sitz in "
    "Hockenheim zu gr&uuml;nden, der in das Vereinsregister eingetragen werden soll." % V,
    ("tbl", vote()))

S += top(3, "Beratung und Beschlussfassung &uuml;ber die Satzung",
    "Der den Anwesenden vorab &uuml;bersandte Satzungsentwurf wird verlesen und beraten. "
    "[Ggf.: Folgende &Auml;nderungen gegen&uuml;ber dem Entwurf werden beschlossen: &hellip;]",
    "Die Satzung wird in der beratenen Fassung <b>einstimmig</b> angenommen. Sie tr&auml;gt das "
    "Datum des heutigen Tages und wird von den anwesenden Gr&uuml;ndungsmitgliedern "
    "unterschrieben. Die unterschriebene Satzung ist diesem Protokoll als Anlage&nbsp;2 "
    "beigef&uuml;gt.",
    ("tbl", vote()),
    ("note", "Die Gr&uuml;ndungssatzung muss einstimmig angenommen werden &ndash; wer nicht "
     "zustimmt, unterschreibt nicht und ist kein Gr&uuml;ndungsmitglied. Mindestens sieben "
     "Unterschriften auf der Satzung selbst."))

def wahl(amt):
    return grid([["Amt", amt],
                 ["Vor- und Nachname", "[ ]"],
                 ["Geburtsdatum", "[ ]"],
                 ["Anschrift", "[ ]"],
                 ["Ja / Nein / Enthaltungen", "[Zahl] / [Zahl] / [Zahl]"],
                 ["Annahme der Wahl", "Die oder der Gew&auml;hlte erkl&auml;rt die Annahme der Wahl."]],
                (48, 90), header=False, fs=9.0)

S += top(4, "Wahl des Vorstands",
    "Die Versammlungsleitung erl&auml;utert, dass nach &sect;&nbsp;8 der Satzung der Vorstand aus "
    "der oder dem Vorsitzenden, der oder dem stellvertretenden Vorsitzenden und der "
    "Schatzmeisterin oder dem Schatzmeister besteht, jedes Vorstandsmitglied den Verein allein "
    "vertritt und die Amtszeit zwei Jahre betr&auml;gt. Die Wahl erfolgt f&uuml;r jedes Amt "
    "einzeln und offen; Einw&auml;nde gegen die offene Wahl werden nicht erhoben.",
    ("tbl", wahl("Vorsitzende / Vorsitzender")),
    ("tbl", wahl("Stellvertretende Vorsitzende / Stellvertretender Vorsitzender")),
    ("tbl", wahl("Schatzmeisterin / Schatzmeister")),
    ("note", "Geburtsdatum und Anschrift sind Pflichtangaben nach Merkblatt A.5.a). Das "
     "Registergericht &uuml;bernimmt sie in das Register."))

S += top(5, "Wahl der Kassenpr&uuml;fung",
    "Zu Kassenpr&uuml;ferinnen bzw. Kassenpr&uuml;fern nach &sect;&nbsp;12 der Satzung werden "
    "gew&auml;hlt: [Vor- und Nachname] und [Vor- und Nachname]. Beide geh&ouml;ren nicht dem "
    "Vorstand an und nehmen die Wahl an.",
    ("tbl", vote()))

S += top(6, "Beitragsordnung",
    "Die Versammlung beschlie&szlig;t die vorliegende Beitragsordnung nach &sect;&nbsp;6 Abs.&nbsp;2 "
    "der Satzung. Sie tritt mit dem heutigen Tag in Kraft und ist als Anlage&nbsp;3 "
    "beigef&uuml;gt.",
    ("tbl", vote()))

S += top(7, "Archiv- und Ausleihordnung, Leihvertr&auml;ge",
    "Die Versammlung beschlie&szlig;t die vorliegende Archiv- und Ausleihordnung nach "
    "&sect;&nbsp;16 Abs.&nbsp;3 der Satzung (Anlage&nbsp;4).",
    ("tbl", vote()),
    "Die Versammlung genehmigt den Abschluss von Leihvertr&auml;gen &uuml;ber die unentgeltliche "
    "&Uuml;berlassung privater Spielesammlungen mit [Name], [Name] und [Name] nach dem "
    "vorliegenden Vertragsmuster (Anlage&nbsp;5). Die Vertr&auml;ge werden auf Seiten des "
    "Vereins jeweils von einem Vorstandsmitglied unterzeichnet, das nicht selbst Leihgeber "
    "ist. Die betroffenen Leihgeber enthalten sich bei dieser Abstimmung.",
    ("tbl", vote()),
    ("note", "Diesen Punkt vor der Gr&uuml;ndungsversammlung streichen, falls die Leihvertr&auml;ge "
     "sp&auml;ter geschlossen werden sollen. Er ist f&uuml;r die Eintragung nicht erforderlich."))

S += top(8, "Erm&auml;chtigung des Vorstands zu Satzungs&auml;nderungen",
    "Die Versammlung beschlie&szlig;t:",
    ("tbl", grid([["&bdquo;Sollten &Auml;nderungen der Satzung aufgrund Beanstandungen des "
                   "Registergerichts Mannheim bzw. des zust&auml;ndigen Finanzamtes notwendig sein, "
                   "wird der Vorstand erm&auml;chtigt, in einer eigens daf&uuml;r einberufenen "
                   "Vorstandssitzung die notwendige &Auml;nderung der Satzung zu "
                   "beschlie&szlig;en.&ldquo;"]], (138,), header=False, fs=9.2)),
    ("tbl", vote()),
    ("note", "W&ouml;rtlich der Passus aus Nr.&nbsp;6 des Merkblatts. Er erg&auml;nzt "
     "&sect;&nbsp;17 Abs.&nbsp;2 der Satzung und ist der Grund, warum eine "
     "Zwischenverf&uuml;gung keine zweite Mitgliederversammlung ausl&ouml;st."))

S += top(9, "Anmeldung zum Vereinsregister",
    "Der Vorstand wird beauftragt, den Verein unverz&uuml;glich zur Eintragung in das "
    "Vereinsregister beim %s anzumelden und den Antrag auf Feststellung "
    "der satzungsm&auml;&szlig;igen Voraussetzungen nach &sect;&nbsp;60a AO beim %s "
    "zu stellen. Die Anmeldung erfolgt durch [Vor- und Nachname] als allein "
    "vertretungsberechtigtes Vorstandsmitglied." % (config.REGISTERGERICHT, config.FINANZAMT),
    ("tbl", vote()))

S += top(10, "Sonstiges und Schluss",
    "[Weitere Beschl&uuml;sse oder Hinweise, sonst: &bdquo;Keine.&ldquo;]",
    "Die Versammlungsleitung schlie&szlig;t die Versammlung um [Uhrzeit] Uhr.")

S += [Spacer(1, 8 * mm), Paragraph("%s, den ______________________" % config.SITZ, BODY),
      Spacer(1, 12 * mm), sigblock(["Versammlungsleitung", "Protokollführung"]),
      Paragraph("Unterschriften nach &sect;&nbsp;11 Abs.&nbsp;5 der Satzung. Anlagen: "
                "1 Anwesenheitsliste, 2 unterschriebene Satzung, 3 Beitragsordnung, "
                "4 Archiv- und Ausleihordnung, 5 Vertragsmuster Leihvertrag.", NOTE)]

# Anlage 1
S += [PageBreak(), Paragraph("Anlage 1 &ndash; Anwesenheitsliste", DOC_TITLE),
      Paragraph("Gr&uuml;ndungsversammlung des %s am [Datum] in Hockenheim" % V, DOC_SUB),
      Spacer(1, 5 * mm)]
rows = [["Nr.", "Name, Vorname", "Anschrift", "Geburtsdatum", "Unterschrift"]] + \
       [[str(i), "", "", "", ""] for i in range(1, 16)]
S += [grid(rows, (9, 36, 44, 22, 27), [7.5] + [11] * 15, align_center_cols=(0,))]

Doc(out("Gruendungsprotokoll-Vorlage.pdf"),
    "Gr\u00fcndungsprotokoll %s - Vorlage" % V).build(S)

