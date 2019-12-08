from Classes.Student import Student


class Lecturer(Student):
    def __init__(self, name=None, password=None, phone_number=None, department=None, list_courses=None):
        """
        init lecturer
        param name: name of the lecturer
        param password: password for the lecturer
        param phone_number: phone number of the lecturer
        param dep: department of the lecturer
        param list_courses: list of the courses that lecturer teach
        """
        self.password = password
        self.phone_number = phone_number
        self.list_courses = list_courses.copy()
        self.department = department
        super().__init__(name)
