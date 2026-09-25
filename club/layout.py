from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib import colors
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Table, TableStyle, Image, Spacer)

from . import config

LOGO = str(config.LOGO)
LOGO_RATIO = 284 / 149


def logo_header(width_mm=34):
    """Logo-Flowables f\u00fcr den Kopf der ersten Seite."""
    img = Image(LOGO, width=width_mm * mm, height=width_mm * mm / LOGO_RATIO)
    img.hAlign = "CENTER"
    return [img, Spacer(1, 4 * mm)]


BODY = ParagraphStyle("body", fontName="Helvetica", fontSize=9.6, leading=14.2,
                      alignment=TA_JUSTIFY, spaceAfter=5.5)
BODY_INDENT = ParagraphStyle("bodyIndent", parent=BODY, leftIndent=13)
PARA_HEAD = ParagraphStyle("paraHead", fontName="Helvetica-Bold", fontSize=10.6,
                           leading=14, alignment=TA_CENTER, spaceBefore=15, spaceAfter=1.5)
PARA_TITLE = ParagraphStyle("paraTitle", fontName="Helvetica-Bold", fontSize=10.6,
                            leading=14, alignment=TA_CENTER, spaceAfter=8)
DOC_TITLE = ParagraphStyle("docTitle", fontName="Helvetica-Bold", fontSize=17,
                           leading=22, alignment=TA_CENTER, spaceAfter=4)
DOC_SUB = ParagraphStyle("docSub", fontName="Helvetica", fontSize=11, leading=15,
                         alignment=TA_CENTER, spaceAfter=3,
                         textColor=colors.HexColor("#333333"))
NOTE = ParagraphStyle("note", fontName="Helvetica-Oblique", fontSize=8.3, leading=11.5,
                      alignment=TA_JUSTIFY, textColor=colors.HexColor("#666666"),
                      leftIndent=13, spaceBefore=2, spaceAfter=7)
TOP_HEAD = ParagraphStyle("topHead", fontName="Helvetica-Bold", fontSize=10.2,
                          leading=14, spaceBefore=11, spaceAfter=4)


class Doc(BaseDocTemplate):
    def __init__(self, path, running_title):
        super().__init__(path, pagesize=A4, leftMargin=27 * mm, rightMargin=25 * mm,
                         topMargin=22 * mm, bottomMargin=20 * mm,
                         title=running_title, author="", subject=running_title)
        self.running_title = running_title
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height,
                      id="main", leftPadding=0, rightPadding=0, topPadding=0,
                      bottomPadding=0)
        self.addPageTemplates([PageTemplate(id="all", frames=[frame],
                                            onPage=self._decorate)])

    def _decorate(self, canvas, doc):
        canvas.saveState()
        w, h = A4
        canvas.setFont("Helvetica", 7.4)
        canvas.setFillColor(colors.HexColor("#8a8a8a"))
        if doc.page > 1:
            canvas.drawString(27 * mm, h - 14 * mm, self.running_title)
            lw = 15 * mm
            canvas.drawImage(LOGO, w - 25 * mm - lw, h - 15.3 * mm, width=lw,
                             height=lw / LOGO_RATIO, mask="auto")
            canvas.setStrokeColor(colors.HexColor("#d5d5d5"))
            canvas.setLineWidth(0.4)
            canvas.line(27 * mm, h - 15.8 * mm, w - 25 * mm, h - 15.8 * mm)
        if config.DRAFT:
            canvas.drawString(27 * mm, 12 * mm, "Entwurf, Stand %s" % config.STAND)
        canvas.drawRightString(w - 25 * mm, 12 * mm, "Seite %d" % doc.page)
        canvas.restoreState()


def note(text):
    """Kursiver Hinweis – nur in der Entwurfsfassung."""
    return [Paragraph(text, NOTE)] if config.DRAFT else []


def fname(base):
    return base + ("-Entwurf" if config.DRAFT else "") + ".pdf"


def rtitle(base):
    return base + (" - Entwurf" if config.DRAFT else "")


def out(filename):
    config.OUT_DIR.mkdir(parents=True, exist_ok=True)
    return str(config.OUT_DIR / filename)


def para(number, title, *absaetze):
    out = [Paragraph("&sect; %d" % number, PARA_HEAD), Paragraph(title, PARA_TITLE)]
    body = [a for a in absaetze if not (isinstance(a, tuple) and a[0] in ("note", "raw"))]
    single = len(body) == 1
    n = 0
    for a in absaetze:
        if isinstance(a, tuple) and a[0] == "note":
            out.extend(note(a[1]))
        elif isinstance(a, tuple) and a[0] == "raw":
            out.append(Paragraph(a[1], BODY_INDENT))
        else:
            n += 1
            out.append(Paragraph(("" if single else "(%d)&nbsp;&nbsp;" % n) + a, BODY))
    return out


def grid(data, colw, rowh=None, header=True, fs=8.4, align_center_cols=()):
    cs = ParagraphStyle("cell", fontName="Helvetica", fontSize=fs, leading=fs * 1.3)
    hs = ParagraphStyle("cellh", parent=cs, fontName="Helvetica-Bold")
    cc = ParagraphStyle("cellc", parent=cs, alignment=TA_CENTER)
    hc = ParagraphStyle("cellhc", parent=hs, alignment=TA_CENTER)
    conv = []
    for r, row in enumerate(data):
        new = []
        for c, cell in enumerate(row):
            if isinstance(cell, str) and cell:
                centered = c in align_center_cols
                st = (hc if centered else hs) if (header and r == 0) else (cc if centered else cs)
                cell = Paragraph(cell, st)
            new.append(cell)
        conv.append(new)
    data = conv
    t = Table(data, colWidths=[c * mm for c in colw],
              rowHeights=[r * mm for r in rowh] if rowh else None, repeatRows=1 if header else 0)
    st = [("FONT", (0, 0), (-1, -1), "Helvetica", fs),
          ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#999999")),
          ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
          ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4)]
    if header:
        st += [("FONT", (0, 0), (-1, 0), "Helvetica-Bold", fs),
               ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#eeeeee"))]
    for c in align_center_cols:
        st.append(("ALIGN", (c, 0), (c, -1), "CENTER"))
    t.setStyle(TableStyle(st))
    return t


def sigblock(labels, w=69):
    data = [["_" * 30] * len(labels), labels]
    t = Table(data, colWidths=[w * mm] * len(labels))
    t.setStyle(TableStyle([
        ("FONT", (0, 0), (-1, 0), "Helvetica", 9),
        ("FONT", (0, 1), (-1, 1), "Helvetica", 8),
        ("TEXTCOLOR", (0, 1), (-1, 1), colors.HexColor("#555555")),
        ("TOPPADDING", (0, 1), (-1, 1), 2)]))
    return t
