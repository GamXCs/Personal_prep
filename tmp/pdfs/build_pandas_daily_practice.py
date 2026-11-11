from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    PageTemplate,
    PageBreak,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "output" / "pdf" / "pandas-daily-practice-guide.pdf"

NAVY = colors.HexColor("#183B56")
TEAL = colors.HexColor("#147D7E")
PALE = colors.HexColor("#EAF5F4")
GOLD = colors.HexColor("#F4B942")
INK = colors.HexColor("#20323F")
MUTED = colors.HexColor("#5D6D77")
LINE = colors.HexColor("#CCD8DC")
WHITE = colors.white


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.line(0.65 * inch, 0.48 * inch, 7.85 * inch, 0.48 * inch)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(MUTED)
    canvas.drawString(0.65 * inch, 0.28 * inch, "Pandas Daily Practice - Grad School Prep")
    canvas.drawRightString(7.85 * inch, 0.28 * inch, f"Page {doc.page}")
    canvas.restoreState()


styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="TitleCustom", parent=styles["Title"], fontName="Helvetica-Bold",
    fontSize=25, leading=29, textColor=NAVY, alignment=TA_CENTER,
    spaceAfter=8,
))
styles.add(ParagraphStyle(
    name="Subtitle", parent=styles["Normal"], fontSize=11, leading=15,
    textColor=MUTED, alignment=TA_CENTER, spaceAfter=18,
))
styles.add(ParagraphStyle(
    name="H1Custom", parent=styles["Heading1"], fontName="Helvetica-Bold",
    fontSize=16, leading=20, textColor=NAVY, spaceBefore=7, spaceAfter=8,
))
styles.add(ParagraphStyle(
    name="H2Custom", parent=styles["Heading2"], fontName="Helvetica-Bold",
    fontSize=11.5, leading=15, textColor=TEAL, spaceBefore=5, spaceAfter=5,
))
styles.add(ParagraphStyle(
    name="BodyCustom", parent=styles["BodyText"], fontSize=9.5, leading=13.5,
    textColor=INK, spaceAfter=5,
))
styles.add(ParagraphStyle(
    name="Small", parent=styles["BodyText"], fontSize=8.4, leading=11.5,
    textColor=INK,
))
styles.add(ParagraphStyle(
    name="HeaderSmall", parent=styles["BodyText"], fontName="Helvetica-Bold",
    fontSize=8.4, leading=11.5, textColor=WHITE,
))
styles.add(ParagraphStyle(
    name="CodeCustom", parent=styles["Code"], fontName="Courier", fontSize=8.2,
    leading=11, textColor=INK, backColor=colors.HexColor("#F4F7F8"),
    borderColor=LINE, borderWidth=0.5, borderPadding=6, spaceAfter=7,
))
styles.add(ParagraphStyle(
    name="Callout", parent=styles["BodyText"], fontSize=10, leading=14,
    textColor=NAVY, backColor=PALE, borderColor=TEAL, borderWidth=0.8,
    borderPadding=9, spaceAfter=10,
))


def p(text, style="BodyCustom"):
    return Paragraph(text, styles[style])


def bullet(text):
    return Paragraph(f"- {text}", styles["BodyCustom"])


def checklist(lines):
    data = [["[ ]", p(line, "Small")] for line in lines]
    table = Table(data, colWidths=[0.34 * inch, 6.7 * inch], hAlign="LEFT")
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TEXTCOLOR", (0, 0), (0, -1), TEAL),
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return table


def build():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = BaseDocTemplate(
        str(OUTPUT), pagesize=letter,
        leftMargin=0.65 * inch, rightMargin=0.65 * inch,
        topMargin=0.58 * inch, bottomMargin=0.62 * inch,
        title="Pandas Daily Practice Guide",
        author="Grad School Prep",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
    doc.addPageTemplates(PageTemplate(id="practice", frames=[frame], onPage=footer))

    story = []
    story += [
        p("Pandas Daily Practice", "TitleCustom"),
        p("A 15-25 minute retrieval routine for making labeled data analysis stick", "Subtitle"),
        p("The goal is not to memorize every method. Build one reliable mental pipeline: <b>inspect, select, transform, preserve row identity, aggregate, verify.</b>", "Callout"),
        p("The daily routine", "H1Custom"),
    ]

    routine = [
        [p("Minutes", "HeaderSmall"), p("Activity", "HeaderSmall"), p("What to do", "HeaderSmall")],
        [p("0-3", "Small"), p("Retrieve", "Small"), p("Write yesterday's pandas patterns from memory. Do not open notes yet.", "Small")],
        [p("3-6", "Small"), p("Predict", "Small"), p("Before each line, predict: DataFrame, Series, scalar, or index label? Also predict shape.", "Small")],
        [p("6-18", "Small"), p("Build", "Small"), p("Complete one small pipeline on a familiar or fresh table. Run after each meaningful step.", "Small")],
        [p("18-22", "Small"), p("Verify", "Small"), p("Check one result by hand and inspect complete rows, not isolated columns.", "Small")],
        [p("22-25", "Small"), p("Reflect", "Small"), p("Write one sentence: what returned an unexpected object or shape today?", "Small")],
    ]
    t = Table(routine, colWidths=[0.65 * inch, 0.85 * inch, 5.55 * inch], repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("GRID", (0, 0), (-1, -1), 0.45, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, colors.HexColor("#F7FAFA")]),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story += [t, Spacer(1, 10), p("Core retrieval sheet", "H1Custom")]

    patterns = [
        ("One column -> Series", 's = df["Exam1"]'),
        ("Several columns -> DataFrame", 'table = df[["Exam1", "Exam2"]]'),
        ("Derived column", 'df["StudentMean"] = df[exam_cols].mean(axis=1)'),
        ("Complete-row filter", 'selected = df.loc[df["StudentMean"] >= 85]'),
        ("Maximum row label", 'label = df["StudentMean"].idxmax()'),
        ("Complete maximum row", 'top_row = df.loc[label]'),
        ("Grouped summaries", 'summary = df.groupby("Band")["StudentMean"].agg(["count", "mean"])'),
        ("Any missing exam value", 'df[exam_cols].isna().any().any()'),
    ]
    data = [[p("Purpose", "HeaderSmall"), p("Pattern", "HeaderSmall")]] + [
        [p(name, "Small"), Paragraph(code.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"), styles["CodeCustom"])]
        for name, code in patterns
    ]
    table = Table(data, colWidths=[2.05 * inch, 5.0 * inch], repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), TEAL),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("GRID", (0, 0), (-1, -1), 0.4, LINE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, colors.HexColor("#F7FAFA")]),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    story += [table, Spacer(1, 8), p("Memory rule: <b>loc uses labels; iloc uses integer positions; idxmax returns a label.</b>", "Callout")]

    story += [p("Seven-day practice cycle", "H1Custom")]
    days = [
        ("Day 1 - Rebuild the exam report", "Without notes, load exams.csv, inspect it, derive StudentMean, recover the top complete row, filter qualifying rows, assign bands, and group by band."),
        ("Day 2 - Object and shape predictions", "Use the exam table. Before every selection or reduction, write the expected object type and shape. Confirm each prediction after running."),
        ("Day 3 - Product revenue", "Create Product, Category, Price, and UnitsSold. Derive Revenue, recover the maximum-revenue row, filter above a threshold, and group by Category."),
        ("Day 4 - Debugging day", "Intentionally use one wrong axis, one extra pair of brackets around a mask, and iloc with an idxmax label. Explain each failure, then repair it."),
        ("Day 5 - Validation retrieval", "On a small CSV, check exact columns, empty data, missing values, numeric conversion, duplicates, and a valid numeric range."),
        ("Day 6 - Chaining practice", "Write groupby and aggregation first as named intermediate variables. Then rewrite the same logic as one readable chain."),
        ("Day 7 - Fresh mini-challenge", "Use a new table and complete the pipeline without looking at examples. End with a two-sentence explanation of row identity and grouping."),
    ]
    for heading, body in days:
        story.append(KeepTogether([p(heading, "H2Custom"), p(body)]))

    story += [Spacer(1, 4), p("Fresh mini-challenge specification", "H1Custom")]
    story += [
        p("Create a small CSV with these columns: <b>Product, Category, Price, UnitsSold</b>. Use at least six rows and two categories. Then complete the following without a Python row loop:"),
        checklist([
            "Load the file and inspect shape, columns, and dtypes.",
            "Require the exact expected schema and reject missing values.",
            "Create Revenue as Price multiplied by UnitsSold.",
            "Recover the complete maximum-revenue row without sorting.",
            "Filter complete rows whose Revenue meets a threshold you choose.",
            "Create Low, Medium, and High revenue bands using Boolean masks and loc.",
            "Group by Category and calculate product count and mean Revenue.",
            "Verify one Revenue value and one group mean by hand.",
        ]),
        Spacer(1, 8),
        p("Daily prediction prompts", "H1Custom"),
        checklist([
            "What object will this expression return: DataFrame, Series, scalar, or label?",
            "What shape should the result have?",
            "Does this operation preserve complete rows and their index labels?",
            "Which axis is being reduced, and what remains afterward?",
            "Can I verify one value manually before trusting the whole result?",
        ]),
        PageBreak(),
        p("End-of-session log", "H1Custom"),
    ]

    log = [
        [p("Date", "HeaderSmall"), p("Dataset / task", "HeaderSmall"), p("One thing recalled", "HeaderSmall"), p("One shaky point", "HeaderSmall")],
    ] + [["", "", "", ""] for _ in range(8)]
    log_table = Table(log, colWidths=[0.8 * inch, 1.8 * inch, 2.25 * inch, 2.2 * inch], rowHeights=[0.33 * inch] + [0.46 * inch] * 8, repeatRows=1)
    log_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("GRID", (0, 0), (-1, -1), 0.55, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
    ]))
    story += [log_table, Spacer(1, 8), p("Success criterion", "H1Custom"), p("You are ready to move on when you can complete the mini-challenge while correctly predicting the main object types and recovering complete rows without losing identity.", "Callout")]

    doc.build(story)
    print(OUTPUT)


if __name__ == "__main__":
    build()
