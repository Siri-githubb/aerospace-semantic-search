import pdfplumber
import os

PDF_PATH = "../data/pdfs/pwt_turbine_blade_thermal_fatigue.pdf"
OUTPUT_PATH = "../data/text/pwt_turbine_blade_thermal_fatigue.txt"

all_text = ""

with pdfplumber.open(PDF_PATH) as pdf:
    for page_num, page in enumerate(pdf.pages, start=1):
        text = page.extract_text()
        if text:
            all_text += f"\n--- Page {page_num} ---\n"
            all_text += text

os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(all_text)

print("Text extraction completed!")
print(f"Saved to: {OUTPUT_PATH}")
