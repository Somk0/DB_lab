from app.dao.assignments_dao import AssignmentsDAO

class AssignmentsService:
    def __init__(self):
        self.dao = AssignmentsDAO()

    def get_all(self):
        return self.dao.get_all()
