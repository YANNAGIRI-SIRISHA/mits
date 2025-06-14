from pydantic import BaseModel

class Internship(BaseModel):
    id: int
    student_name: str
    domain: str
    duration_in_months: int
