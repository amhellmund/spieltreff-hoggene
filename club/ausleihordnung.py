# -*- coding: utf-8 -*-
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.units import mm
from . import config
from .layout import logo_header, note, out, fname, rtitle, Doc, para, grid, sigblock, BODY, NOTE, DOC_TITLE, DOC_SUB, PARA_HEAD, PARA_TITLE

V = config.VEREINSNAME
S = logo_header() + [Paragraph("Archiv- und Ausleihordnung", DOC_TITLE), Paragraph("des %s" % V, DOC_SUB),
     Paragraph("beschlossen von der Mitgliederversammlung am ____________________", DOC_SUB),
     Spacer(1, 6 * mm),
     *note("Diese Ordnung ist nicht Bestandteil der Satzung und wird nicht in das Vereinsregister "
               "eingetragen. Sie regelt den Betrieb des Spielearchivs nach &sect;&nbsp;2 Abs.&nbsp;3 "
               "Buchstabe&nbsp;b) der Satzung. Kursive Hinweise vor der Beschlussfassung entfernen."),
     Spacer(1, 3 * mm)]

S += para(1, "Zweck und Geltungsbereich",
    "Das Spielearchiv dient der Verwirklichung des Satzungszwecks, insbesondere der Vermittlung "
    "analoger Spielkultur und der F&ouml;rderung der Volks- und Berufsbildung.",
    "Diese Ordnung regelt Bestand, Nutzung und Ausleihe des Archivs. Sie gilt f&uuml;r Mitglieder "
    "des Vereins und f&uuml;r Dritte gleicherma&szlig;en.",
    "&Uuml;ber die Ordnung beschlie&szlig;t nach &sect;&nbsp;16 Abs.&nbsp;3 der Satzung die "
    "Mitgliederversammlung.")

S += para(2, "Bestand und Eigentumsverh&auml;ltnisse",
    "Der Bestand des Archivs setzt sich zusammen aus Gegenst&auml;nden im Eigentum des Vereins und "
    "aus Gegenst&auml;nden, die dem Verein aufgrund gesonderter Leihvertr&auml;ge unentgeltlich zur "
    "Verf&uuml;gung gestellt werden.",
    "Der Verein f&uuml;hrt ein Bestandsverzeichnis. Es weist f&uuml;r jeden Titel mindestens aus: "
    "laufende Nummer, Titel, Verlag, Zustand, Wiederbeschaffungswert, Eigentumsverh&auml;ltnis und "
    "Ausleihstatus.",
    "Gegenst&auml;nde im Eigentum des Vereins werden dauerhaft und sichtbar als solche gekennzeichnet. "
    "Leihgaben werden als Fremdeigentum gekennzeichnet.",
    "Bei der Ausleihe wird zwischen Vereinseigentum und Leihgaben nicht unterschieden. Die Rechte "
    "der Leihgeber ergeben sich aus dem jeweiligen Leihvertrag.",
    ("note", "Absatz&nbsp;3 von Anfang an durchziehen &ndash; Aufkleber im Deckel. Sonst wei&szlig; nach "
     "zwei Jahren niemand mehr, was wem geh&ouml;rt."))

S += para(3, "Ausleihberechtigung",
    "Ausleihberechtigt sind Mitglieder des Vereins sowie vollj&auml;hrige Dritte.",
    "Minderj&auml;hrige k&ouml;nnen ausleihen, wenn eine schriftliche Einwilligung der gesetzlichen "
    "Vertreter vorliegt. Diese haften f&uuml;r Verlust und Besch&auml;digung.",
    "Dritte hinterlegen bei der ersten Ausleihe Name, Anschrift und eine Kontaktm&ouml;glichkeit und "
    "weisen sich einmalig aus.",
    "Ein Anspruch auf Ausleihe eines bestimmten Titels besteht nicht.")

S += [Paragraph("&sect; 4", PARA_HEAD), Paragraph("Ausleihgeb&uuml;hren", PARA_TITLE),
      Paragraph("(1)&nbsp;&nbsp;F&uuml;r die Ausleihe werden folgende Geb&uuml;hren erhoben:", BODY),
      Spacer(1, 2 * mm),
      grid([["Leistung", "Mitglieder", "Nichtmitglieder"]] + [list(r) for r in config.AUSLEIHGEBUEHREN],
           (74, 32, 32), [8] + [7.6] * len(config.AUSLEIHGEBUEHREN), fs=9, align_center_cols=(1, 2)),
      Spacer(1, 4 * mm)]
for t in [
    "(2)&nbsp;&nbsp;Die Geb&uuml;hren sind bei der Ausleihe f&auml;llig. Die Kaution wird bei "
    "vollst&auml;ndiger und unbesch&auml;digter R&uuml;ckgabe erstattet.",
    "(3)&nbsp;&nbsp;Die Nutzung des Archivbestands vor Ort bei Spieltreffs und Veranstaltungen des "
    "Vereins ist f&uuml;r alle Teilnehmenden geb&uuml;hrenfrei.",
    "(4)&nbsp;&nbsp;Der Vorstand kann Geb&uuml;hren in begr&uuml;ndeten Einzelf&auml;llen "
    "erm&auml;&szlig;igen oder erlassen. Niemand soll aus finanziellen Gr&uuml;nden von der Nutzung "
    "des Archivs ausgeschlossen sein.",
    "(5)&nbsp;&nbsp;Die Geb&uuml;hren sind so bemessen, dass sie die Kosten des Archivbetriebs decken. "
    "Eine Gewinnerzielung ist nicht bezweckt. Die Einnahmen verbleiben in voller H&ouml;he beim Verein "
    "und werden f&uuml;r satzungsm&auml;&szlig;ige Zwecke verwendet.",
    "(6)&nbsp;&nbsp;Die verg&uuml;nstigten Geb&uuml;hren f&uuml;r Mitglieder sind eine "
    "Verg&uuml;nstigung und kein Bestandteil des Mitgliedsbeitrags. Ein Anspruch hierauf besteht "
    "nicht; &sect;&nbsp;6 Abs.&nbsp;3 der Beitragsordnung bleibt unber&uuml;hrt."]:
    S.append(Paragraph(t, BODY))
S.extend(note("Die Abs&auml;tze 5 und 6 sind die steuerlich tragenden S&auml;tze: Absatz&nbsp;5 "
                   "st&uuml;tzt den Zweckbetrieb nach &sect;&nbsp;65 AO, Absatz&nbsp;6 h&auml;lt den "
                   "Mitgliedsbeitrag frei von einer Gegenleistung. Deshalb zahlen Mitglieder einen "
                   "reduzierten Betrag und nicht null."))

S += para(5, "Ausleihdauer, Verl&auml;ngerung",
    "Die Ausleihfrist betr&auml;gt 14 Tage.",
    "Die Ausleihe kann zweimal um jeweils 14 Tage verl&auml;ngert werden, sofern der Titel nicht "
    "vorgemerkt ist. Die Verl&auml;ngerung ist vor Fristablauf zu beantragen.",
    "Gleichzeitig k&ouml;nnen h&ouml;chstens drei Titel ausgeliehen werden.")

S += para(6, "Ausleihvorgang",
    "Jede Ausleihe und jede R&uuml;ckgabe wird im Bestandsverzeichnis mit Datum, Titel und "
    "ausleihender Person dokumentiert.",
    "Die ausleihende Person pr&uuml;ft den Titel bei &Uuml;bernahme auf Vollst&auml;ndigkeit und "
    "erkennbare Sch&auml;den. Beanstandungen sind sofort anzuzeigen; sp&auml;tere Beanstandungen sind "
    "ausgeschlossen.",
    "Der Verein pr&uuml;ft jeden Titel bei R&uuml;ckgabe auf Vollst&auml;ndigkeit und Zustand. Die "
    "R&uuml;ckgabe gilt erst mit dieser Pr&uuml;fung als erfolgt.",
    "Ausleihe und R&uuml;ckgabe erfolgen zu den bekanntgegebenen Zeiten, in der Regel im Rahmen der "
    "Spieltreffs.")

S += para(7, "Pflichten der ausleihenden Person",
    "Die ausleihende Person behandelt den Titel pfleglich und sch&uuml;tzt ihn vor Besch&auml;digung, "
    "N&auml;sse und Verschmutzung.",
    "Eine Weitergabe an Dritte ist nicht gestattet. Die ausleihende Person bleibt f&uuml;r den Titel "
    "verantwortlich.",
    "Ver&auml;nderungen am Spielmaterial, Beschriftungen und das Entfernen von Kennzeichnungen sind "
    "unzul&auml;ssig.",
    "Eine gewerbliche Nutzung des ausgeliehenen Materials ist ausgeschlossen.")

S += para(8, "S&auml;umnis, Verlust, Besch&auml;digung",
    "Bei &Uuml;berschreitung der Ausleihfrist f&auml;llt die S&auml;umnisgeb&uuml;hr nach "
    "&sect;&nbsp;4 an. Der Verein mahnt in Textform.",
    "Geht ein Titel verloren oder wird er so besch&auml;digt, dass eine bestimmungsgem&auml;&szlig;e "
    "Nutzung nicht mehr m&ouml;glich ist, ersetzt die ausleihende Person den im Bestandsverzeichnis "
    "ausgewiesenen Wiederbeschaffungswert oder beschafft auf eigene Kosten ein gleichwertiges "
    "Ersatzexemplar.",
    "Bei fehlenden Einzelteilen tr&auml;gt die ausleihende Person die Kosten der Ersatzbeschaffung.",
    "&Uuml;bliche Gebrauchsspuren begr&uuml;nden keine Ersatzpflicht.",
    "Solange ein Ersatzanspruch offen ist, ruht die Ausleihberechtigung.",
    ("note", "Diese Ersatzpflicht tritt neben die Ersatzpflicht des Vereins gegen&uuml;ber dem "
     "Leihgeber aus &sect;&nbsp;6 des Leihvertrages. Bleibt die ausleihende Person aus, tr&auml;gt der "
     "Verein den Schaden &ndash; daf&uuml;r die Kaution bei Nichtmitgliedern."))

S += para(9, "Pr&auml;senzbestand",
    "Der Vorstand kann einzelne Titel von der Ausleihe ausnehmen, insbesondere bei gro&szlig;em "
    "Umfang, hohem Wert, empfindlichem Material oder auf Wunsch des Leihgebers.",
    "Diese Titel stehen ausschlie&szlig;lich zur Nutzung vor Ort zur Verf&uuml;gung und werden im "
    "Bestandsverzeichnis entsprechend gekennzeichnet.")

S += para(10, "Datenschutz",
    "Der Verein verarbeitet die zur Abwicklung der Ausleihe erforderlichen Daten auf Grundlage von "
    "Art.&nbsp;6 Abs.&nbsp;1 Buchstabe&nbsp;b) DSGVO.",
    "Ausleihdaten werden sp&auml;testens zw&ouml;lf Monate nach vollst&auml;ndiger Abwicklung des "
    "Vorgangs gel&ouml;scht, sofern keine gesetzlichen Aufbewahrungspflichten oder offenen "
    "Anspr&uuml;che entgegenstehen.",
    "Im &Uuml;brigen gilt die Datenschutzordnung des Vereins.")

S += para(11, "Ausschluss von der Nutzung",
    "Der Vorstand kann Personen von der Ausleihe ausschlie&szlig;en, die wiederholt gegen diese "
    "Ordnung versto&szlig;en, insbesondere bei wiederholter S&auml;umnis oder bei schuldhafter "
    "Besch&auml;digung.",
    "Der Ausschluss ist in Textform mitzuteilen und zu begr&uuml;nden. Er ber&uuml;hrt die "
    "Mitgliedschaft im Verein nicht.")

S += para(12, "Inkrafttreten",
    "Diese Ordnung wurde von der Mitgliederversammlung am ____________________ beschlossen und "
    "tritt am selben Tag in Kraft.",
    "&Auml;nderungen bed&uuml;rfen eines Beschlusses der Mitgliederversammlung mit einfacher "
    "Mehrheit.")

S += [Spacer(1, 10 * mm), Paragraph("%s, den ______________________" % config.SITZ, BODY),
      Spacer(1, 14 * mm), sigblock(["Vorsitzende / Vorsitzender", "Schatzmeisterin / Schatzmeister"])]

Doc(out(fname("Archiv-und-Ausleihordnung")), rtitle("Archiv- und Ausleihordnung %s" % V)).build(S)

