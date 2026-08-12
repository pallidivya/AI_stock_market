from fastapi import APIRouter, UploadFile, File, Form
import os

from agents.report_agent import ReportAgent


router = APIRouter()

agent = ReportAgent()


@router.post("/")
def generate_daily_report(
    symbol: str = Form(...),
    file: UploadFile = File(...)
):
    pdf_path = f"temp_{file.filename}"

    try:
        with open(pdf_path, "wb") as buffer:
            buffer.write(file.file.read())

        result = agent.generate_report(
            symbol=symbol,
            pdf_path=pdf_path
        )

        return result.model_dump()

    finally:
        if os.path.exists(pdf_path):
            os.remove(pdf_path)