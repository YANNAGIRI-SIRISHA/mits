class InternshipValidator:
    VALID_DOMAINS = {"Web Development", "Data Science", "Cyber Security", "UI/UX", "AI/ML"}

    def validate(self, data):
        if not data.student_name:
            raise ValueError("Student name cannot be empty.")

        if data.duration_in_months < 1 or data.duration_in_months > 12:
            raise ValueError("Internship duration must be between 1 and 12 months.")

        if data.domain not in self.VALID_DOMAINS:
            raise ValueError(f"Invalid domain: {data.domain}")
validator
