from app.models.assignment import Assignment

class AssignmentsDAO:
    def get_all(self):
        return Assignment.query.all()
