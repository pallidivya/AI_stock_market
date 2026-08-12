from tools.pdf_tool import PDFTool

text = PDFTool.extract_text("reports/apple_annual_report.pdf")

print(text[:3000])