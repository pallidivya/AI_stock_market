from fastapi import APIRouter, UploadFile, File, Form

from agents.advisor_agent import AdvisorAgent


router = APIRouter()

agent = AdvisorAgent()


@router.post("/")
def analyze_advisor(
    symbol: str = Form(...),
    file: UploadFile = File(...)
):
    # Save uploaded PDF temporarily
    pdf_path = f"temp_{file.filename}"

    with open(pdf_path, "wb") as buffer:
        buffer.write(file.file.read())

    result = agent.analyze(
        symbol,
        pdf_path
    )

    return result.model_dump()