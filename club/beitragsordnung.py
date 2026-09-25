# -*- coding: utf-8 -*-
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.units import mm
from . import config
from .layout import logo_header, note, out, fname, rtitle, Doc, para, grid, sigblock, BODY, NOTE, DOC_TITLE, DOC_SUB, PARA_HEAD, PARA_TITLE

V = config.VEREINSNAME
S = logo_header() + [Paragraph("Beitragsordnung", DOC_TITLE), Paragraph("des %s" % V, DOC_SUB),
     Paragraph("beschlossen von der Mitgliederversammlung am ____________________", DOC_SUB),
     Spacer(1, 6 * mm),
     *note("Diese Beitragsordnung ist nicht Bestandteil der Satzung. Sie wird nicht in das "
               "Vereinsregister eingetragen und kann durch einfachen Beschluss der Mitgliederversammlung "
               "ge&auml;ndert werden. Kursive Hinweise vor der Beschlussfassung entfernen."),
     Spacer(1, 3 * mm)]

S += para(1, "Grundlage",
    "Diese Beitragsordnung regelt auf Grundlage von &sect;&nbsp;6 der Satzung H&ouml;he, "
    "F&auml;lligkeit und Zahlungsweise der Mitgliedsbeitr&auml;ge.")

S += [Paragraph("&sect; 2", PARA_HEAD), Paragraph("Beitragss&auml;tze", PARA_TITLE),
      Paragraph("(1)&nbsp;&nbsp;Der Jahresbeitrag betr&auml;gt:", BODY), Spacer(1, 2 * mm),
      grid([["Mitgliedschaft", "Jahresbeitrag"]] + [list(r) for r in config.BEITRAEGE],
           (105, 33), [8] + [7.6] * len(config.BEITRAEGE), fs=9, align_center_cols=(1,)),
      Spacer(1, 4 * mm)]
for t in [
    "(2)&nbsp;&nbsp;Anspruch auf den erm&auml;&szlig;igten Beitrag haben Kinder und Jugendliche bis "
    "zur Vollendung des 18.&nbsp;Lebensjahres, Sch&uuml;lerinnen und Sch&uuml;ler, Auszubildende, "
    "Studierende, Personen im Freiwilligendienst sowie Empf&auml;ngerinnen und Empf&auml;nger von "
    "Sozialleistungen. Der Nachweis ist auf Verlangen einmal j&auml;hrlich vorzulegen.",
    "(3)&nbsp;&nbsp;Die Familienmitgliedschaft umfasst zwei im selben Haushalt lebende Erwachsene "
    "sowie deren Kinder bis zur Vollendung des 18.&nbsp;Lebensjahres. Jede vollj&auml;hrige Person "
    "der Familienmitgliedschaft hat ein eigenes Stimmrecht.",
    "(4)&nbsp;&nbsp;Eine Aufnahmegeb&uuml;hr wird nicht erhoben."]:
    S.append(Paragraph(t, BODY))
S.extend(note("24&nbsp;EUR bei 50 Mitgliedern sind rund 1.200&nbsp;EUR im Jahr. Vor der "
                   "Beschlussfassung gegen Versicherung, Konto, Ticketing und Material rechnen."))

S += para(3, "Entstehung und F&auml;lligkeit",
    "Der Beitrag ist ein Jahresbeitrag und wird zum %s eines jeden Jahres f&auml;llig." % config.BEITRAG_FAELLIG,
    "Bei Eintritt im laufenden Kalenderjahr wird der Beitrag anteilig f&uuml;r jeden angefangenen "
    "Monat der Mitgliedschaft erhoben. Er ist mit Beginn der Mitgliedschaft f&auml;llig.",
    "Bei Beendigung der Mitgliedschaft im laufenden Jahr erfolgt keine anteilige Erstattung.")

S += para(4, "Zahlungsweise",
    "Die Beitr&auml;ge werden im SEPA-Basislastschriftverfahren eingezogen. Mit dem Aufnahmeantrag "
    "erteilt das Mitglied dem Verein ein entsprechendes SEPA-Lastschriftmandat.",
    "Der Einzug wird dem Mitglied mindestens f&uuml;nf Kalendertage vorher angek&uuml;ndigt. Die "
    "Vorabank&uuml;ndigung kann per E-Mail erfolgen und mit der Beitragsrechnung verbunden werden.",
    "In begr&uuml;ndeten F&auml;llen kann der Vorstand die Zahlung per &Uuml;berweisung zulassen.",
    "&Auml;nderungen der Bankverbindung sind dem Verein unverz&uuml;glich mitzuteilen. Kosten, die "
    "dem Verein durch eine vom Mitglied verschuldete R&uuml;cklastschrift entstehen, k&ouml;nnen dem "
    "Mitglied in Rechnung gestellt werden.",
    ("note", "Gl&auml;ubiger-Identifikationsnummer bei der Deutschen Bundesbank beantragen, bevor "
     "das erste Mandat eingeholt wird; sie muss im Mandatstext stehen."))

S += para(5, "Erm&auml;&szlig;igung, Stundung, Erlass",
    "Der Vorstand kann Beitr&auml;ge auf Antrag in begr&uuml;ndeten Einzelf&auml;llen stunden, "
    "erm&auml;&szlig;igen oder erlassen, insbesondere bei wirtschaftlicher Bed&uuml;rftigkeit.",
    "Der Antrag ist in Textform zu stellen. Die Entscheidung wird aktenkundig gemacht und "
    "vertraulich behandelt.",
    "Niemand soll aus finanziellen Gr&uuml;nden von der Mitgliedschaft ausgeschlossen sein.")

S += para(6, "Leistungen f&uuml;r Mitglieder",
    "Mitglieder haben im Rahmen der jeweils geltenden Ordnungen Zugang zu den Angeboten des Vereins, "
    "insbesondere zu den Spieltreffs und zur Ausleihe aus dem Spielearchiv.",
    "Bei Veranstaltungen des Vereins k&ouml;nnen Mitgliedern Verg&uuml;nstigungen einger&auml;umt "
    "werden. &Uuml;ber Art und Umfang entscheidet der Vorstand f&uuml;r die jeweilige Veranstaltung.",
    "Ein Anspruch auf bestimmte Leistungen oder Verg&uuml;nstigungen besteht nicht. Der "
    "Mitgliedsbeitrag ist kein Entgelt f&uuml;r einzelne Leistungen des Vereins.",
    ("note", "Absatz&nbsp;3 sichert den echten Mitgliedsbeitrag ab. Verg&uuml;nstigungen nirgends "
     "als &bdquo;im Beitrag enthalten&ldquo; formulieren &ndash; auch nicht auf der Website."))

S += para(7, "Beitragsr&uuml;ckstand",
    "Kommt ein Mitglied mit der Zahlung in Verzug, wird es in Textform gemahnt.",
    "Nach zweimaliger erfolgloser Mahnung kann der Vorstand die Mitgliedschaft nach "
    "&sect;&nbsp;5 Abs.&nbsp;3 der Satzung beenden. Der R&uuml;ckstand bleibt geschuldet.",
    "W&auml;hrend eines Beitragsr&uuml;ckstands ruhen die Mitgliedsrechte einschlie&szlig;lich des "
    "Stimmrechts.")

S += para(8, "Inkrafttreten",
    "Diese Beitragsordnung wurde von der Mitgliederversammlung am ____________________ "
    "beschlossen und tritt am selben Tag in Kraft.",
    "&Auml;nderungen bed&uuml;rfen eines Beschlusses der Mitgliederversammlung mit einfacher "
    "Mehrheit.")

S += [Spacer(1, 10 * mm), Paragraph("%s, den ______________________" % config.SITZ, BODY),
      Spacer(1, 14 * mm), sigblock(["Vorsitzende / Vorsitzender", "Schatzmeisterin / Schatzmeister"])]

Doc(out(fname("Beitragsordnung")), rtitle("Beitragsordnung %s" % V)).build(S)

