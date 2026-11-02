
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import os

doc = Document()

# Page margins
section = doc.sections[0]
section.top_margin = Inches(0.7)
section.bottom_margin = Inches(0.7)
section.left_margin = Inches(0.8)
section.right_margin = Inches(0.8)

# Default font
style = doc.styles["Normal"]
style.font.name = "Arial"
style.font.size = Pt(10)

# Title
title = doc.add_heading("WEEK 2 – DATA CLEANING & PREPROCESSING", 0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

subtitle = doc.add_paragraph(
    "Logistics Internship Project"
)
subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.add_paragraph("")

doc.add_heading("1. Project Overview", level=1)
doc.add_paragraph(
    "The objective of this project was to clean and preprocess "
    "the logistics supply chain dataset. The work included data "
    "inspection, missing value analysis, duplicate checking, "
    "removal of unnecessary columns, date conversion and outlier analysis."
)

doc.add_heading("2. Dataset Description", level=1)
doc.add_paragraph(
    "The project used the DataCo Supply Chain dataset, containing "
    "180,519 records and 53 original columns. The dataset includes "
    "order, customer, product, sales, delivery and shipping information."
)

doc.add_heading("3. Data Inspection", level=1)
doc.add_paragraph(
    "The dataset was loaded using Python Pandas. Initial inspection "
    "was performed to understand the number of rows, columns, data "
    "types, missing values and duplicate records."
)
doc.add_paragraph("Original Rows: 180,519")
doc.add_paragraph("Original Columns: 53")
doc.add_paragraph("Exact Duplicate Rows: 0")

doc.add_heading("4. Missing Values and Duplicate Analysis", level=1)
doc.add_paragraph(
    "Missing values were identified in Product Description, Order "
    "Zipcode, Customer Last Name and Customer Zipcode columns. "
    "The exact duplicate check found zero duplicate rows."
)

doc.add_heading("5. Data Cleaning", level=1)
doc.add_paragraph(
    "A total of 10 unnecessary or personal-information-related "
    "columns were removed from the working dataset. These included "
    "customer email, password, names, street, customer identifiers "
    "and selected zipcode fields, along with product description."
)
doc.add_paragraph(
    "The cleaned dataset contains 180,519 rows and 43 columns. "
    "The original dataset was kept unchanged."
)

doc.add_heading("6. Date Conversion", level=1)
doc.add_paragraph(
    "The order_date_dateorders and shipping_date_dateorders "
    "columns were converted from string to datetime format using "
    "Pandas. Both columns were converted successfully with zero "
    "invalid dates."
)

doc.add_heading("7. Outlier Analysis", level=1)
doc.add_paragraph(
    "The Interquartile Range (IQR) method was used to identify "
    "potential outliers in selected numerical columns."
)

table = doc.add_table(rows=1, cols=2)
table.style = "Light Shading Accent 1"

headers = table.rows[0].cells
headers[0].text = "Column"
headers[1].text = "Outlier Count"

outlier_data = [
    ("Sales", "488"),
    ("Order Profit Per Order", "18,942"),
    ("Days for Shipping Real", "0"),
    ("Order Item Quantity", "0"),
    ("Product Price", "2,048"),
]

for name, count in outlier_data:
    cells = table.add_row().cells
    cells[0].text = name
    cells[1].text = count

doc.add_paragraph(
    "Potential outliers were identified but not removed because "
    "extreme values may represent genuine business transactions."
)

doc.add_heading("8. Final Data Quality Results", level=1)

final_table = doc.add_table(rows=1, cols=2)
final_table.style = "Light Shading Accent 1"

final_table.rows[0].cells[0].text = "Metric"
final_table.rows[0].cells[1].text = "Final Result"

results = [
    ("Total Rows", "180,519"),
    ("Total Columns", "43"),
    ("Missing Values", "0"),
    ("Duplicate Rows", "0"),
    ("Invalid Dates", "0"),
]

for metric, value in results:
    cells = final_table.add_row().cells
    cells[0].text = metric
    cells[1].text = value

doc.add_heading("9. Tools and Technologies Used", level=1)
doc.add_paragraph(
    "Python, Pandas, NumPy, Visual Studio Code and Microsoft Word."
)

doc.add_heading("10. Conclusion", level=1)
doc.add_paragraph(
    "The data cleaning and preprocessing task was completed "
    "successfully. The dataset was reduced from 53 to 43 columns, "
    "date columns were converted successfully, and the final quality "
    "check reported zero missing values and zero duplicate rows. "
    "Potential outliers were documented for further analysis. "
    "The cleaned dataset is now ready for further logistics data analysis."
)

doc.add_paragraph("")
p = doc.add_paragraph("Prepared by: Rishi Vaidya")
p.alignment = WD_ALIGN_PARAGRAPH.RIGHT

# Save report
os.makedirs("reports", exist_ok=True)
output_path = "Week2_Report.docx"
doc.save(output_path)

print("Week 2 Report generated successfully!")
print("Saved at:", os.path.abspath(output_path))
