import os
import tempfile

from fastapi import APIRouter, UploadFile, File, Form, HTTPException

from agents.financial_agent import FinancialAgent


router = APIRouter()

agent = FinancialAgent()


@router.post("/")
async def analyze_financial(
    company: str = Form(...),
    file: UploadFile = File(...)
):
    temp_path = None

    try:
        # Check that a PDF was uploaded
        if not file.filename.lower().endswith(".pdf"):
            raise HTTPException(
                status_code=400,
                detail="Please upload a PDF file."
            )

        # Read uploaded PDF
        contents = await file.read()

        # Create temporary PDF file
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as temp_file:

            temp_file.write(contents)
            temp_path = temp_file.name

        # Run Financial Agent
        result = agent.analyze(
            company_name=company,
            pdf_path=temp_path
        )

        # Return Pydantic result as JSON
        return result.model_dump()

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    finally:
        # Delete temporary PDF
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)