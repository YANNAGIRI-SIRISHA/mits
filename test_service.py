import pytest
from service import InternshipService

class Dummy:
    def __init__(self, student_name, domain, duration_in_months):
        self.student_name = student_name
        self.domain = domain
        self.duration_in_months = duration_in_months

def test_valid_internship():
    service = InternshipService()
    data = Dummy("Alice", "Web Development", 6)
    result = service.assign_internship(data)
    assert result.id == 1
    assert result.student_name == "Alice"

def test_invalid_duration():
    service = InternshipService()
    data = Dummy("Bob", "Web Development", 0)
    with pytest.raises(ValueError):
        service.assign_internship(data)

def test_invalid_domain():
    service = InternshipService()
    data = Dummy("Carol", "Rocket Science", 6)
    with pytest.raises(ValueError):
        service.assign_internship(data)
