from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")
pdf = FPDF(orientation='P', unit="mm", format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():
    pdf.add_page()

    # set the header for the main page
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], border=False, ln=1, align="L")

    for yl in range(20, 298, 20):
        pdf.set_text_color(100, 100, 100)
        pdf.line(x1=10, y1=yl, x2=200, y2=yl)

    # set the footer on the main page
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    if row["Pages"] > 1:
        for i in range(row["Pages"] - 1):
            pdf.add_page()

            # set the additional lines on additional pages
            for yl in range(20, 298, 20):
                pdf.set_text_color(100, 100, 100)
                pdf.line(x1=10, y1=yl, x2=200, y2=yl)

            # set the footer on the additional pages
            pdf.ln(277)
            pdf.set_font(family="Times", style="I", size=8)
            pdf.set_text_color(180, 180, 180)
            pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("test.pdf")
