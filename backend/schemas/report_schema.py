from pydantic import BaseModel


class DailyReport(BaseModel):
    company: str

    report: str