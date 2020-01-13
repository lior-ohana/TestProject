from Classes.Lecturer import Lecturer


class ClassManager(Lecturer):
    def __init__(self, name=None, password=None, phone_number=None, department=None, list_courses=None):
        """
        init classManger
        param name: name of the classManger
        param password: password for the classManger
        param phone_number: phone number of the classManger
        param dep: department of the classManger
        param list_courses: list of the courses that classManger teach
        """
        super().__init__(name, password, phone_number, department, list_courses)
