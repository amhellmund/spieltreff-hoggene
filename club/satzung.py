# -*- coding: utf-8 -*-
from reportlab.platypus import Paragraph, Spacer, KeepTogether
from reportlab.lib.units import mm
from . import config
from .layout import logo_header, note, out, fname, rtitle, Doc, para, grid, BODY, NOTE, DOC_TITLE, DOC_SUB

V = config.VEREINSNAME
S = logo_header() + [Paragraph("Satzung", DOC_TITLE), Paragraph("des %s" % V, DOC_SUB),
     Paragraph("mit Sitz in %s" % config.SITZ, DOC_SUB), Spacer(1, 6 * mm),
     *note("Das Datum der Errichtung in &sect;&nbsp;19 wird in der Gr&uuml;ndungsversammlung "
               "eingetragen. Kursive Hinweise und die Fu&szlig;zeile &bdquo;Entwurf&ldquo; vor der "
               "Einreichung entfernen."), Spacer(1, 3 * mm)]

S += para(1, "Name, Sitz, Gesch&auml;ftsjahr",
    "Der Verein f&uuml;hrt den Namen &bdquo;%s&ldquo;. Er soll in das Vereinsregister "
    "eingetragen werden und f&uuml;hrt nach der Eintragung den Zusatz &bdquo;e.&nbsp;V.&ldquo;" % V,
    "Der Verein hat seinen Sitz in %s." % config.SITZ,
    "Das Gesch&auml;ftsjahr ist das Kalenderjahr. Das erste Gesch&auml;ftsjahr ist ein "
    "Rumpfgesch&auml;ftsjahr und endet am 31.&nbsp;Dezember des Gr&uuml;ndungsjahres.")

S += para(2, "Zweck des Vereins",
    "Der Verein mit Sitz in %s verfolgt ausschlie&szlig;lich und unmittelbar "
    "gemeinn&uuml;tzige Zwecke im Sinne des Abschnitts &bdquo;Steuerbeg&uuml;nstigte Zwecke&ldquo; "
    "der Abgabenordnung." % config.SITZ,
    "Zweck des Vereins ist die F&ouml;rderung der Volks- und Berufsbildung "
    "(&sect;&nbsp;52 Abs.&nbsp;2 Satz&nbsp;1 Nr.&nbsp;7 AO), die F&ouml;rderung der Jugendhilfe "
    "(&sect;&nbsp;52 Abs.&nbsp;2 Satz&nbsp;1 Nr.&nbsp;4 AO) sowie die F&ouml;rderung von Kunst und "
    "Kultur (&sect;&nbsp;52 Abs.&nbsp;2 Satz&nbsp;1 Nr.&nbsp;5 AO).",
    "Der Satzungszweck wird verwirklicht insbesondere durch:",
    ("raw", "a)&nbsp;&nbsp;die Durchf&uuml;hrung regelm&auml;&szlig;iger, f&uuml;r die "
     "&Ouml;ffentlichkeit zug&auml;nglicher Spieltreffs, bei denen analoge Gesellschafts- und "
     "Brettspiele angeleitet, erkl&auml;rt und gemeinsam gespielt werden;"),
    ("raw", "b)&nbsp;&nbsp;den Aufbau, die Pflege und die Bereitstellung eines &ouml;ffentlich "
     "nutzbaren Spielearchivs sowie dessen Ausleihe;"),
    ("raw", "c)&nbsp;&nbsp;die Durchf&uuml;hrung von Bildungsveranstaltungen, Workshops, "
     "Vortr&auml;gen, Autorenlesungen und Turnieren zur Vermittlung von Spielkultur, "
     "Spielgestaltung und den damit verbundenen sozialen, gestalterischen und "
     "mathematischen Kompetenzen;"),
    ("raw", "d)&nbsp;&nbsp;Angebote der offenen Kinder- und Jugendarbeit sowie die "
     "Zusammenarbeit mit Schulen, Kinderg&auml;rten, Jugendeinrichtungen und "
     "Senioreneinrichtungen;"),
    ("raw", "e)&nbsp;&nbsp;die Ausrichtung &ouml;ffentlicher Veranstaltungen und Festivals zur "
     "Vermittlung und Verbreitung analoger Spielkultur;"),
    ("raw", "f)&nbsp;&nbsp;die Aus- und Fortbildung ehrenamtlicher Spielleiterinnen und "
     "Spielleiter."),
    ("note", "Streicht, was ihr im ersten Jahr nicht anbietet. Buchstabe d) zieht erweiterte "
     "F&uuml;hrungszeugnisse und ein Schutzkonzept nach sich. Die Buchstaben c) und e) tragen "
     "die Zweckbetriebseigenschaft des Festivalprogramms."))

S += para(3, "Selbstlosigkeit",
    "Der Verein ist selbstlos t&auml;tig; er verfolgt nicht in erster Linie eigenwirtschaftliche "
    "Zwecke.",
    "Mittel des Vereins d&uuml;rfen nur f&uuml;r die satzungsm&auml;&szlig;igen Zwecke verwendet "
    "werden. Die Mitglieder erhalten keine Zuwendungen aus Mitteln des Vereins.",
    "Es darf keine Person durch Ausgaben, die dem Zweck des Vereins fremd sind, oder durch "
    "unverh&auml;ltnism&auml;&szlig;ig hohe Verg&uuml;tungen beg&uuml;nstigt werden.",
    ("note", "W&ouml;rtlich aus der Mustersatzung nach Anlage&nbsp;1 zu &sect;&nbsp;60 AO. Nicht "
     "umformulieren."))

S += para(4, "Erwerb der Mitgliedschaft",
    "Mitglied des Vereins kann jede nat&uuml;rliche und jede juristische Person werden.",
    "Der Verein hat ordentliche Mitglieder und F&ouml;rdermitglieder. F&ouml;rdermitglieder "
    "unterst&uuml;tzen den Verein ideell und finanziell; sie haben kein Stimmrecht in der "
    "Mitgliederversammlung.",
    "Die Mitgliedschaft wird auf schriftlichen oder in Textform gestellten Aufnahmeantrag "
    "erworben. Der Aufnahmeantrag ist an den Vorstand zu richten. Bei Minderj&auml;hrigen ist "
    "die Zustimmung der gesetzlichen Vertreter erforderlich.",
    "&Uuml;ber den Aufnahmeantrag entscheidet der Vorstand. Ein Aufnahmeanspruch besteht "
    "nicht. Die Ablehnung muss nicht begr&uuml;ndet werden.")

S += para(5, "Beendigung der Mitgliedschaft",
    "Die Mitgliedschaft endet durch Austritt, Ausschluss, Tod oder bei juristischen Personen "
    "durch Verlust der Rechtsf&auml;higkeit.",
    "Der Austritt ist gegen&uuml;ber dem Vorstand in Textform zu erkl&auml;ren. Er ist unter "
    "Einhaltung einer Frist von vier Wochen zum Ende eines Kalenderjahres zul&auml;ssig.",
    "Ein Mitglied kann durch Beschluss des Vorstands ausgeschlossen werden, wenn es "
    "trotz zweimaliger Mahnung mit der Zahlung des Beitrags im R&uuml;ckstand ist oder wenn es "
    "in erheblichem Ma&szlig; gegen die Interessen des Vereins verst&ouml;&szlig;t. Dem Mitglied "
    "ist zuvor Gelegenheit zur Stellungnahme zu geben. Gegen den Ausschluss steht dem "
    "Mitglied die Berufung an die Mitgliederversammlung zu, die binnen eines Monats nach "
    "Zugang des Beschlusses in Textform einzulegen ist.",
    "Mit Beendigung der Mitgliedschaft erl&ouml;schen alle Anspr&uuml;che gegen den Verein. "
    "Bereits entrichtete Beitr&auml;ge werden nicht erstattet.")

S += para(6, "Mitgliedsbeitr&auml;ge",
    "Der Verein erhebt von seinen Mitgliedern Beitr&auml;ge.",
    "H&ouml;he, F&auml;lligkeit und Zahlungsweise der Beitr&auml;ge sowie etwaige "
    "Erm&auml;&szlig;igungen und Aufnahmegeb&uuml;hren regelt eine Beitragsordnung, die von "
    "der Mitgliederversammlung beschlossen wird. Die Beitragsordnung ist nicht Bestandteil "
    "dieser Satzung.",
    "Der Vorstand kann Beitr&auml;ge in begr&uuml;ndeten Einzelf&auml;llen stunden, "
    "erm&auml;&szlig;igen oder erlassen.")

S += para(7, "Organe des Vereins",
    "Organe des Vereins sind der Vorstand und die Mitgliederversammlung.")

S += para(8, "Vorstand",
    "Der Vorstand besteht aus der oder dem Vorsitzenden, der oder dem stellvertretenden "
    "Vorsitzenden und der Schatzmeisterin oder dem Schatzmeister.",
    "Vorstand im Sinne des &sect;&nbsp;26 BGB sind die in Absatz&nbsp;1 genannten Personen. "
    "Jedes Vorstandsmitglied ist allein zur Vertretung des Vereins berechtigt.",
    "Der Vorstand wird von der Mitgliederversammlung f&uuml;r die Dauer von zwei Jahren "
    "gew&auml;hlt. Er bleibt bis zur wirksamen Neuwahl im Amt. Wiederwahl ist "
    "zul&auml;ssig. Scheidet ein Vorstandsmitglied vorzeitig aus, kann der Vorstand f&uuml;r "
    "die restliche Amtszeit ein Ersatzmitglied berufen.",
    "W&auml;hlbar sind nur Vereinsmitglieder. Die &Auml;mter k&ouml;nnen nicht in einer Person "
    "vereinigt werden.",
    "Der Vorstand fasst seine Beschl&uuml;sse in Sitzungen, die auch fernm&uuml;ndlich oder "
    "mittels elektronischer Kommunikation abgehalten werden k&ouml;nnen, oder im "
    "Umlaufverfahren in Textform. Er ist beschlussf&auml;hig, wenn mindestens zwei seiner "
    "Mitglieder mitwirken. Beschl&uuml;sse werden mit einfacher Mehrheit gefasst; bei "
    "Stimmengleichheit entscheidet die Stimme der oder des Vorsitzenden.",
    "Der Vorstand f&uuml;hrt die laufenden Gesch&auml;fte des Vereins und ist f&uuml;r alle "
    "Angelegenheiten zust&auml;ndig, die nicht durch Satzung der Mitgliederversammlung "
    "zugewiesen sind.",
    "Im Innenverh&auml;ltnis gilt: Rechtsgesch&auml;fte mit einem Gesch&auml;ftswert von mehr "
    "als %s&nbsp;Euro im Einzelfall bed&uuml;rfen eines vorherigen Beschlusses des "
    "Vorstands. Diese Beschr&auml;nkung gilt ausschlie&szlig;lich im Innenverh&auml;ltnis und "
    "ber&uuml;hrt die Vertretungsmacht der Vorstandsmitglieder gegen&uuml;ber Dritten nicht." % config.INNENBINDUNG_EUR)

S += para(9, "Mitgliederversammlung",
    "Die ordentliche Mitgliederversammlung findet einmal j&auml;hrlich statt.",
    "Die Mitgliederversammlung ist insbesondere zust&auml;ndig f&uuml;r:",
    ("raw", "a)&nbsp;&nbsp;die Entgegennahme des Rechenschaftsberichts des Vorstands und des "
     "Berichts der Kassenpr&uuml;fer;"),
    ("raw", "b)&nbsp;&nbsp;die Entlastung des Vorstands;"),
    ("raw", "c)&nbsp;&nbsp;die Wahl und Abberufung des Vorstands und der Kassenpr&uuml;fer;"),
    ("raw", "d)&nbsp;&nbsp;die Beschlussfassung &uuml;ber die Beitragsordnung und die "
     "Archiv- und Ausleihordnung;"),
    ("raw", "e)&nbsp;&nbsp;&Auml;nderungen der Satzung und die Aufl&ouml;sung des Vereins;"),
    ("raw", "f)&nbsp;&nbsp;die Entscheidung &uuml;ber Berufungen gegen Ausschlussbeschl&uuml;sse."),
    "Eine au&szlig;erordentliche Mitgliederversammlung ist einzuberufen, wenn das Interesse "
    "des Vereins es erfordert oder wenn mindestens ein Viertel der stimmberechtigten "
    "Mitglieder dies unter Angabe des Zwecks in Textform verlangt.")

S += para(10, "Einberufung und Durchf&uuml;hrung",
    "Die Mitgliederversammlung wird vom Vorstand unter Einhaltung einer Frist von zwei "
    "Wochen unter Angabe der Tagesordnung einberufen. Die Einladung erfolgt in Textform. Hat "
    "das Mitglied dem Verein eine E-Mail-Adresse mitgeteilt, wird die Einladung an diese "
    "E-Mail-Adresse versandt; andernfalls an die zuletzt mitgeteilte Postanschrift. Die Frist "
    "beginnt mit dem auf die Absendung folgenden Tag. Die Einladung gilt dem Mitglied als "
    "zugegangen, wenn sie an die zuletzt von ihm mitgeteilte Adresse gerichtet ist.",
    "Der Vorstand kann bei der Einberufung vorsehen, dass Mitglieder an der Versammlung ohne "
    "Anwesenheit am Versammlungsort im Wege der elektronischen Kommunikation teilnehmen und "
    "ihre Rechte aus&uuml;ben k&ouml;nnen. Er kann ferner vorsehen, dass die Versammlung "
    "ausschlie&szlig;lich im Wege der elektronischen Kommunikation abgehalten wird. Die "
    "Zugangsdaten sind mit der Einladung mitzuteilen.",
    "Antr&auml;ge zur Tagesordnung sind bis eine Woche vor der Versammlung beim Vorstand in "
    "Textform einzureichen. &Uuml;ber die Behandlung sp&auml;ter eingehender Antr&auml;ge "
    "entscheidet die Versammlung.",
    "Die Versammlung wird von der oder dem Vorsitzenden geleitet, bei Verhinderung von der "
    "oder dem stellvertretenden Vorsitzenden.")

S += para(11, "Beschlussfassung",
    "Jede ordnungsgem&auml;&szlig; einberufene Mitgliederversammlung ist ohne R&uuml;cksicht "
    "auf die Zahl der erschienenen Mitglieder beschlussf&auml;hig.",
    "Jedes ordentliche Mitglied hat eine Stimme. Das Stimmrecht ist nicht &uuml;bertragbar. "
    "Mitglieder unter 16 Jahren haben kein Stimmrecht.",
    "Beschl&uuml;sse werden mit einfacher Mehrheit der abgegebenen g&uuml;ltigen Stimmen "
    "gefasst. Stimmenthaltungen bleiben au&szlig;er Betracht. Bei Stimmengleichheit gilt ein "
    "Antrag als abgelehnt.",
    "Satzungs&auml;nderungen bed&uuml;rfen einer Mehrheit von zwei Dritteln, &Auml;nderungen "
    "des Vereinszwecks und die Aufl&ouml;sung des Vereins einer Mehrheit von drei Vierteln "
    "der abgegebenen g&uuml;ltigen Stimmen.",
    "Die Versammlungsleitung bestimmt zu Beginn der Versammlung eine Protokollf&uuml;hrerin "
    "oder einen Protokollf&uuml;hrer. &Uuml;ber den Verlauf der Versammlung und die gefassten "
    "Beschl&uuml;sse ist ein Protokoll aufzunehmen, das von der Versammlungsleitung und der "
    "Protokollf&uuml;hrung zu unterzeichnen ist.")

S += para(12, "Kassenpr&uuml;fung",
    "Die Mitgliederversammlung w&auml;hlt f&uuml;r die Dauer von zwei Jahren zwei "
    "Kassenpr&uuml;ferinnen oder Kassenpr&uuml;fer, die weder dem Vorstand angeh&ouml;ren "
    "noch Angestellte des Vereins sein d&uuml;rfen.",
    "Sie pr&uuml;fen die Kassen- und Buchf&uuml;hrung des Vereins einmal j&auml;hrlich "
    "rechnerisch und sachlich und berichten der Mitgliederversammlung.")

S += para(13, "Ehrenamt, Verg&uuml;tungen, Aufwandsersatz",
    "Die Vereins- und Organ&auml;mter werden grunds&auml;tzlich ehrenamtlich ausge&uuml;bt.",
    "Mitglieder und Mitarbeitende haben einen Anspruch auf Ersatz der ihnen im Auftrag des "
    "Vereins tats&auml;chlich entstandenen und nachgewiesenen Aufwendungen. Der Vorstand "
    "kann durch Beschluss die Erstattung im Rahmen der steuerlichen H&ouml;chsts&auml;tze "
    "pauschalieren.",
    "Die Mitgliederversammlung kann beschlie&szlig;en, dass f&uuml;r die T&auml;tigkeit im "
    "Verein oder in den Vereinsorganen eine angemessene Verg&uuml;tung oder eine "
    "Aufwandsentsch&auml;digung im Rahmen der steuerlichen Freibetr&auml;ge nach "
    "&sect;&nbsp;3 Nr.&nbsp;26 und Nr.&nbsp;26a EStG gezahlt wird.",
    "Der Vorstand ist erm&auml;chtigt, im Rahmen der finanziellen M&ouml;glichkeiten "
    "Arbeitsvertr&auml;ge, Dienstvertr&auml;ge und Auftragsverh&auml;ltnisse zur "
    "Erf&uuml;llung der Vereinszwecke abzuschlie&szlig;en.")

S += para(14, "Haftungsbeschr&auml;nkung",
    "Der Verein haftet gegen&uuml;ber seinen Mitgliedern nur f&uuml;r Sch&auml;den, die von "
    "Organmitgliedern oder Mitarbeitenden des Vereins vors&auml;tzlich oder grob "
    "fahrl&auml;ssig verursacht wurden.",
    "Organmitglieder und besondere Vertreter haften dem Verein f&uuml;r einen bei der "
    "Wahrnehmung ihrer Pflichten verursachten Schaden nur bei Vorsatz oder grober "
    "Fahrl&auml;ssigkeit; &sect;&sect;&nbsp;31a, 31b BGB bleiben unber&uuml;hrt.")

S += para(15, "Datenschutz",
    "Zur Erf&uuml;llung der satzungsgem&auml;&szlig;en Aufgaben verarbeitet der Verein "
    "personenbezogene Daten seiner Mitglieder. Die Verarbeitung erfolgt nach den "
    "Bestimmungen der Datenschutz-Grundverordnung und des Bundesdatenschutzgesetzes.",
    "Das N&auml;here regelt eine Datenschutzordnung, die der Vorstand beschlie&szlig;t.")

S += para(16, "Ordnungen",
    "Zur Regelung der internen Abl&auml;ufe kann sich der Verein Ordnungen geben, "
    "insbesondere eine Beitragsordnung, eine Archiv- und Ausleihordnung, eine "
    "Gesch&auml;ftsordnung und eine Datenschutzordnung.",
    "Ordnungen sind nicht Bestandteil dieser Satzung und werden nicht in das "
    "Vereinsregister eingetragen. Sie d&uuml;rfen dieser Satzung nicht widersprechen.",
    "Die Beitragsordnung und die Archiv- und Ausleihordnung beschlie&szlig;t die "
    "Mitgliederversammlung; alle &uuml;brigen Ordnungen beschlie&szlig;t der Vorstand.")

S += para(17, "Satzungs&auml;nderungen",
    "&Auml;nderungen der Satzung beschlie&szlig;t die Mitgliederversammlung nach "
    "&sect;&nbsp;11 Abs.&nbsp;4 dieser Satzung.",
    "Sollten &Auml;nderungen der Satzung aufgrund von Beanstandungen des Registergerichts oder "
    "des zust&auml;ndigen Finanzamts notwendig sein, ist der Vorstand erm&auml;chtigt, in einer "
    "eigens daf&uuml;r einberufenen Vorstandssitzung die notwendige &Auml;nderung der Satzung "
    "zu beschlie&szlig;en. Er hat die Mitglieder hier&uuml;ber in der n&auml;chsten "
    "Mitgliederversammlung zu unterrichten.")

S += para(18, "Aufl&ouml;sung und Verm&ouml;gensbindung",
    "Die Aufl&ouml;sung des Vereins beschlie&szlig;t die Mitgliederversammlung nach "
    "&sect;&nbsp;11 Abs.&nbsp;4 dieser Satzung.",
    "Sofern die Mitgliederversammlung nichts anderes beschlie&szlig;t, sind die Mitglieder "
    "des Vorstands gemeinsam vertretungsberechtigte Liquidatoren.",
    "Bei Aufl&ouml;sung des Vereins oder bei Wegfall steuerbeg&uuml;nstigter Zwecke f&auml;llt "
    "das Verm&ouml;gen des Vereins an %s, die es unmittelbar und ausschlie&szlig;lich "
    "f&uuml;r gemeinn&uuml;tzige Zwecke, %s, zu verwenden hat." % (config.BEGUENSTIGTE, config.BEGUENSTIGTE_ZWECK),
    ("note", "Einverst&auml;ndnis der Stadt Hockenheim vor der Gr&uuml;ndungsversammlung einholen."))

S += para(19, "Gr&uuml;ndung und Inkrafttreten",
    "Diese Satzung wurde in der Gr&uuml;ndungsversammlung am ____________________ in Hockenheim "
    "errichtet und beschlossen.",
    "Sie tritt mit ihrer Beschlussfassung in Kraft; die Regelungen zur Rechtsf&auml;higkeit "
    "gelten ab der Eintragung in das Vereinsregister.")

# Unterschriften: unmittelbar im Anschluss, kein eigenes Blatt
rows = [["Nr.", "Name, Vorname, Anschrift, Geburtsdatum", "Unterschrift"]] + \
       [[str(i), "", ""] for i in range(1, 9)]
sig = grid(rows, (9, 62, 62), [7.5] + [12.5] * 8, align_center_cols=(0,))
S += [Spacer(1, 4 * mm), KeepTogether([
    Paragraph("Die vorstehende Satzung wurde in der Gr&uuml;ndungsversammlung beraten und "
              "einstimmig angenommen.", BODY),
    Paragraph("%s, den ______________________" % config.SITZ, BODY),
    Spacer(1, 3 * mm), sig]),
    *note("Mindestens sieben Unterschriften, Datum nicht vergessen.")]

Doc(out(fname("Satzung")), rtitle("Satzung %s" % V)).build(S)

