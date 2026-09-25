# -*- coding: utf-8 -*-
from reportlab.platypus import Paragraph, Spacer, PageBreak
from reportlab.lib.units import mm
from . import config
from .layout import logo_header, note, out, fname, rtitle, Doc, para, grid, sigblock, BODY, BODY_INDENT, NOTE, DOC_TITLE, DOC_SUB

V = config.VEREINSNAME
S = logo_header() + [Paragraph("Leihvertrag", DOC_TITLE),
     Paragraph("&uuml;ber die unentgeltliche &Uuml;berlassung einer Spielesammlung", DOC_SUB),
     Spacer(1, 7 * mm), Paragraph("zwischen", BODY), Spacer(1, 2 * mm),
     Paragraph("<b>______________________________</b>, ______________________________<br/>"
               "&ndash; nachfolgend &bdquo;Verleiher&ldquo; &ndash;", BODY_INDENT), Spacer(1, 3 * mm),
     Paragraph("und", BODY), Spacer(1, 2 * mm),
     Paragraph("<b>%s</b>, %s, vertreten durch das allein vertretungsberechtigte "
               "Vorstandsmitglied ______________________________<br/>"
               "&ndash; nachfolgend &bdquo;Verein&ldquo; &ndash;" % (V, config.SITZ), BODY_INDENT), Spacer(1, 5 * mm),
     Paragraph("Der Verein baut ein &ouml;ffentlich zug&auml;ngliches Spielearchiv nach &sect;&nbsp;2 "
               "Abs.&nbsp;3 Buchstabe&nbsp;b) seiner Satzung auf. Bis zum Aufbau eines eigenen Bestands "
               "stellt der Verleiher dem Verein Teile seiner privaten Spielesammlung unentgeltlich zur "
               "Verf&uuml;gung. Dies vorausgeschickt, vereinbaren die Parteien:", BODY)]

S += para(1, "Vertragsgegenstand",
    "Der Verleiher &uuml;berl&auml;sst dem Verein die in der Anlage&nbsp;1 aufgef&uuml;hrten Spiele "
    "und Materialien (nachfolgend &bdquo;Leihgabe&ldquo;) leihweise zur Nutzung im Rahmen der "
    "satzungsm&auml;&szlig;igen Zwecke des Vereins.",
    "Die Anlage&nbsp;1 ist Bestandteil dieses Vertrages. Sie weist zu jedem Titel den Zustand bei "
    "&Uuml;bergabe und den vereinbarten Wiederbeschaffungswert aus.",
    "Die &Uuml;bergabe erfolgt am ____________________. Der Empfang wird durch beiderseitige "
    "Unterschrift unter die Anlage&nbsp;1 best&auml;tigt.")

S += para(2, "Unentgeltlichkeit und Eigentum",
    "Die &Uuml;berlassung erfolgt unentgeltlich. Der Verein schuldet dem Verleiher f&uuml;r die "
    "Nutzung weder Miete noch ein sonstiges Entgelt.",
    "Das Eigentum an der Leihgabe verbleibt beim Verleiher. Ein Eigentums&uuml;bergang auf den "
    "Verein findet nicht statt.",
    "Der Verleiher erh&auml;lt f&uuml;r die &Uuml;berlassung keine Zuwendungsbest&auml;tigung. Die "
    "unentgeltliche &Uuml;berlassung eines Gegenstands zur Nutzung ist keine steuerlich abziehbare "
    "Zuwendung.")

S += para(3, "Nutzung durch den Verein",
    "Der Verein ist berechtigt, die Leihgabe im Rahmen seiner satzungsm&auml;&szlig;igen Zwecke zu "
    "nutzen, insbesondere bei Spieltreffs, Turnieren, Workshops, Bildungsveranstaltungen, Festivals "
    "und Kooperationsveranstaltungen mit Dritten.",
    "Die Leihgabe wird r&auml;umlich getrennt oder erkennbar abgegrenzt vom Vereinseigentum "
    "aufbewahrt und dauerhaft als Eigentum des Verleihers gekennzeichnet.",
    "Der Verein f&uuml;hrt ein Bestandsverzeichnis, aus dem sich f&uuml;r jeden Titel die "
    "Eigentumsverh&auml;ltnisse ergeben.",
    "Der Verein tr&auml;gt die Kosten der Aufbewahrung, Pflege und Instandhaltung sowie etwaiger "
    "Ersatzteilbeschaffung.")

S += para(4, "Weitergabe an Dritte",
    "Der Verleiher gestattet dem Verein ausdr&uuml;cklich, die Leihgabe im Rahmen des Ausleihbetriebs "
    "des Spielearchivs an Vereinsmitglieder und an Dritte zu &uuml;berlassen. &sect;&nbsp;603 "
    "Satz&nbsp;2 BGB findet insoweit keine Anwendung.",
    "Die Gestattung nach Absatz&nbsp;1 umfasst ausdr&uuml;cklich auch die <b>entgeltliche</b> "
    "&Uuml;berlassung an Personen, die nicht Mitglied des Vereins sind.",
    "Die aus dem Ausleihbetrieb erzielten Einnahmen stehen in voller H&ouml;he dem Verein zu. Der "
    "Verleiher hat hieran keinen Anteil und keinen Anspruch auf Auskehrung.",
    "Die Einzelheiten des Ausleihbetriebs regelt die Archiv- und Ausleihordnung des Vereins in ihrer "
    "jeweils geltenden Fassung. Der Verleiher erkennt diese an.")

S += para(5, "Sorgfaltspflicht des Vereins",
    "Der Verein behandelt die Leihgabe pfleglich und sch&uuml;tzt sie im Rahmen des Zumutbaren vor "
    "Besch&auml;digung, Verlust und Diebstahl.",
    "Der Verein pr&uuml;ft jeden Titel bei R&uuml;ckgabe aus einer Ausleihe auf Vollst&auml;ndigkeit "
    "und Zustand.",
    "Einmal j&auml;hrlich f&uuml;hren die Parteien einen Bestandsabgleich anhand der Anlage&nbsp;1 "
    "durch und halten Abg&auml;nge, Sch&auml;den und Nachtr&auml;ge schriftlich fest.")

S += para(6, "Haftung f&uuml;r Verlust und Besch&auml;digung",
    "Geht ein Titel der Leihgabe verloren oder wird er so besch&auml;digt, dass eine "
    "bestimmungsgem&auml;&szlig;e Nutzung nicht mehr m&ouml;glich ist, ersetzt der Verein dem "
    "Verleiher den in der Anlage&nbsp;1 ausgewiesenen Wiederbeschaffungswert oder beschafft auf "
    "eigene Kosten ein gleichwertiges Ersatzexemplar. Die Wahl trifft der Verein.",
    "Bei Verlust einzelner Bestandteile beschafft der Verein auf eigene Kosten Ersatz, soweit dies "
    "m&ouml;glich und wirtschaftlich vertretbar ist.",
    "Die durch die vertragsgem&auml;&szlig;e Nutzung entstehende Abnutzung, insbesondere &uuml;bliche "
    "Gebrauchsspuren an Schachteln, Karten und Spielmaterial, hat der Verleiher "
    "entsch&auml;digungslos hinzunehmen. &sect;&nbsp;602 BGB bleibt unber&uuml;hrt.",
    "&sect;&nbsp;599 BGB bleibt unber&uuml;hrt: Der Verleiher haftet dem Verein nur f&uuml;r Vorsatz "
    "und grobe Fahrl&auml;ssigkeit.")

S += para(7, "Versicherung",
    "Der Verein pr&uuml;ft, ob die Leihgabe als Fremdeigentum in seine Inhalts- und "
    "Haftpflichtversicherung eingeschlossen ist, und wirkt auf einen entsprechenden Einschluss hin.",
    "Der Verein unterrichtet den Verleiher &uuml;ber den Umfang des bestehenden Versicherungsschutzes "
    "sowie &uuml;ber wesentliche &Auml;nderungen.",
    ("note", "Fremdeigentum ist in Vereinspolicen h&auml;ufig ausgeschlossen. Beim Angebot ausdr&uuml;cklich "
     "abfragen, sonst tr&auml;gt der Verein die Ersatzpflicht aus &sect;&nbsp;6 ungedeckt."))

S += para(8, "Vertragsdauer und K&uuml;ndigung",
    "Der Vertrag beginnt mit der &Uuml;bergabe nach &sect;&nbsp;1 Abs.&nbsp;3 und wird auf unbestimmte "
    "Zeit geschlossen.",
    "Beide Parteien k&ouml;nnen den Vertrag mit einer Frist von sechs Monaten zum Ende eines "
    "Kalendermonats in Textform k&uuml;ndigen. Das Recht des Verleihers zur jederzeitigen "
    "R&uuml;ckforderung nach &sect;&nbsp;604 Abs.&nbsp;3 BGB wird hiermit abbedungen.",
    "Das Recht zur K&uuml;ndigung aus wichtigem Grund bleibt unber&uuml;hrt. Ein wichtiger Grund liegt "
    "f&uuml;r den Verleiher insbesondere vor, wenn der Verein wiederholt und trotz Abmahnung gegen "
    "&sect;&nbsp;5 verst&ouml;&szlig;t.",
    "Der Vertrag endet ferner mit der Aufl&ouml;sung des Vereins. Die Leihgabe ist in diesem Fall an "
    "den Verleiher herauszugeben; sie f&auml;llt nicht unter die Verm&ouml;gensbindung nach "
    "&sect;&nbsp;18 Abs.&nbsp;3 der Satzung.")

S += para(9, "Bestands&auml;nderungen",
    "Der Verleiher kann weitere Titel in die Leihgabe einbringen. Sie werden in die Anlage&nbsp;1 "
    "aufgenommen und von beiden Parteien gegengezeichnet.",
    "Der Verleiher kann einzelne Titel mit einer Frist von einem Monat aus der Leihgabe "
    "herausl&ouml;sen, sofern sie nicht gerade ausgeliehen sind.",
    "Der Verein kann einzelne Titel zur&uuml;ckgeben, wenn sie f&uuml;r den Archivbetrieb nicht mehr "
    "ben&ouml;tigt werden.")

S += para(10, "Umwandlung in eine Sachspende",
    "Die Parteien k&ouml;nnen jederzeit vereinbaren, dass einzelne Titel oder die gesamte Leihgabe "
    "in das Eigentum des Vereins &uuml;bergehen. Die Vereinbarung bedarf der Textform.",
    "In diesem Fall stellt der Verein eine Zuwendungsbest&auml;tigung &uuml;ber den gemeinen Wert der "
    "zugewendeten Gegenst&auml;nde aus. Der Wert ist nachvollziehbar zu ermitteln und zu "
    "dokumentieren.",
    "Mit dem Eigentums&uuml;bergang unterliegen die betroffenen Gegenst&auml;nde der "
    "Verm&ouml;gensbindung nach &sect;&nbsp;18 Abs.&nbsp;3 der Satzung. Eine R&uuml;ck&uuml;bertragung an "
    "den Zuwendenden ist ausgeschlossen.",
    ("note", "Bei einem Vorstandsmitglied, das an sich selbst bescheinigt, die Wertermittlung besonders "
     "sauber belegen &ndash; etwa &uuml;ber Marktpreise vergleichbarer Gebrauchtexemplare."))

S += para(11, "Schlussbestimmungen",
    "&Auml;nderungen und Erg&auml;nzungen dieses Vertrages bed&uuml;rfen der Textform. Dies gilt auch "
    "f&uuml;r die &Auml;nderung dieser Klausel.",
    "Sollte eine Bestimmung dieses Vertrages unwirksam sein oder werden, bleibt die Wirksamkeit der "
    "&uuml;brigen Bestimmungen unber&uuml;hrt.",
    "Dieser Vertrag wurde auf Seiten des Vereins von einem Vorstandsmitglied unterzeichnet, das "
    "nicht Eigent&uuml;mer der Leihgabe ist.",
    ("note", "Absatz&nbsp;3 vermeidet ein Insichgesch&auml;ft nach &sect;&nbsp;181 BGB. Die "
     "Mitgliederversammlung genehmigt den Vertrag nach TOP&nbsp;7 des Gr&uuml;ndungsprotokolls."))

S += [Spacer(1, 12 * mm), Paragraph("%s, den ______________________" % config.SITZ, BODY),
      Spacer(1, 15 * mm), sigblock(["Verleiher", "Für den Verein"])]

S += [PageBreak(), Paragraph("Anlage 1 zum Leihvertrag", DOC_TITLE),
      Paragraph("Inventarverzeichnis der Leihgabe", DOC_SUB), Spacer(1, 4 * mm),
      Paragraph("Verleiher: ______________________________&nbsp;&nbsp;&nbsp;&nbsp;"
                "&Uuml;bergabe am: ______________________", BODY), Spacer(1, 4 * mm),
      Paragraph("Zustand: 1 = neuwertig, 2 = gut, 3 = deutliche Gebrauchsspuren, 4 = unvollst&auml;ndig "
                "(Fehlteile in der Bemerkung vermerken). Der Wiederbeschaffungswert ist der Betrag, den "
                "der Verein nach &sect;&nbsp;6 des Vertrages im Verlustfall ersetzt.", NOTE),
      Spacer(1, 2 * mm)]
rows = [["Nr.", "Titel", "Verlag", "Zust.", "Wert EUR", "Bemerkung"]] + \
       [[str(i), "", "", "", "", ""] for i in range(1, 21)]
S += [grid(rows, (9, 46, 27, 11, 17, 28), [8] + [8.3] * 20, fs=8, align_center_cols=(0, 3, 4)),
      Spacer(1, 6 * mm),
      Paragraph("Der Verein best&auml;tigt den Empfang der vorstehend aufgef&uuml;hrten Gegenst&auml;nde "
                "im angegebenen Zustand. Bei sp&auml;teren Nachtr&auml;gen ist eine Fortschreibung dieses "
                "Verzeichnisses von beiden Parteien gegenzuzeichnen.", BODY),
      Spacer(1, 12 * mm), sigblock(["Verleiher", "Für den Verein"])]

Doc(out(fname("Leihvertrag-Spielesammlung")), rtitle("Leihvertrag Spielesammlung %s" % V)).build(S)

