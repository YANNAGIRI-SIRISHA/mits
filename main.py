from fastapi import FastAPI, HTTPException
from models import Internship
from service import InternshipService
from pydantic import BaseModel

app = FastAPI()
service = InternshipService()

class InternshipRequest(BaseModel):
    student_name: str
    domain: str
    duration_in_months: int

@app.post("/internships")
def create_internship(data: InternshipRequest):
    try:
        internship = service.assign_internship(data)
        return internship
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
