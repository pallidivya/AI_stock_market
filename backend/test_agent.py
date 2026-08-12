from agents.report_agent import ReportAgent

agent = ReportAgent()

result = agent.generate_report(
    symbol="AAPL",
    pdf_path="reports/apple_annual_report.pdf"
)

print(type(result))
print()
print(result)
print()
print(result.model_dump())