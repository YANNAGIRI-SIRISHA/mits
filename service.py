from models import Internship
from validator import InternshipValidator

class InternshipService:
    def __init__(self):
        self._db = []
        self._id_counter = 1
        self.validator = InternshipValidator()

    def assign_internship(self, data) -> Internship:
        self.validator.validate(data)

        internship = Internship(
            id=self._id_counter,
            student_name=data.student_name,
            domain=data.domain,
            duration_in_months=data.duration_in_months
        )
        self._db.append(internship)
        self._id_counter += 1
        return internship

    def list_all(self):
        return self._db
