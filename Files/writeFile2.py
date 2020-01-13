from Classes.ClassManager import *
from Classes.Course import *
from Classes.Question import *
from Classes.Student import *

"""
def write_lecturer_class_manager(file, user):
    if not type(user) == type(ClassManager()) and not type(user) == type(Lecturer()):
        return -1

    file.write("Name: "+ str(user.name.capitalize()) + "Password: "+ str(user.password) + " Phone: "+str(user.phone_number) + " Department: "+str(user.department))
    for i in range(1, len(user.list_courses)):
        file.write(" Course" + str(i) + ": " + str(user.list_courses[i]))

    return 1


def write_student(file, user):
    if type(user) != type(Student()):
        return -1
    file.write("Name: "+ str(user.name.capitalize()))
    return 1


def write_course(file, course1):
    if type(course1) != type(Course()):
        return -1
    file.write("Name: "+str(course1.name)+"Department: "+str(course1.dep))
    return 1


def write_solution(file, solution1):
    if type(solution1) != type(Solution()):
        return -1
    file.write("Code_q: "+str(solution1.code_q)+" Format_s: "+str(solution1.format_s) + " Type: "+str(solution1.type_s))
    return 1


def write_question(file, question1):
    if isinstance(type(question1),type(Question())):
       return -1
    file.write(" Code_q: " + str(question1.code_q) + " Subject: " + str(question1.subject) + " Sub_subject: " + str(question1.sub_subject) +
               " Level: " + str(question1.level) + " Type_test: "+str(question1.type_test)+" Year: "+str(question1.year)+" Semester: "+str(question1.semester) +
               " Term_test: "+str(question1.term_test)+" Format_q: "+str(question1.format_q)+" Is_solution: "+str(question1.is_solution))
    return 1
"""

def write_all_questions(file_name, list_of_questions):
    f = open(file_name, "w").close()  # clear the file
    f = open(file_name, "a")

    for q in list_of_questions:
        f.write(" Code_q: " + str(q.code_q) + " Subject: " + str(q.subject) + " Sub_subject: " + str(q.sub_subject) +
                " Level: " + str(q.level) + " Type_test: " + str(q.type_test) + " Year: " + str(q.year) + " Semester: "
                + str(q.semester) + " Term_test: " + str(q.term_test) + " Format_q: " + str(q.format_q) +
                " Is_solution: " + str(q.is_solution))
        f.write("\n")

    f.close()
    return 1


def write_all_solutions(file_name, list_of_solutions):
    f = open(file_name, "w").close()  # clear the file
    f = open(file_name, "a")
    for s in list_of_solutions:
        f.write("Code_q: " + str(s.code_q) + " Format_s: " + str(s.format_s) + " Type: " + str(s.type_s))
        f.write("\n")
    f.close()


def write_all_students(file_name, list_of_students):
    f = open(file_name, "w").close()  # clear the file
    f = open(file_name, "a")
    for s in list_of_students:
        s.write("Name: " + str(s.name.capitalize()))
        f.write("\n")
    f.close()


def write_all_lecturers_class_managers(file_name, list_of_lecturers):
    f = open(file_name, "w").close()  # clear the file
    f = open(file_name, "a")
    for s in list_of_lecturers:
        f.write("Name: " + str(s.name.capitalize()) + " Password: " + str(s.password) + " Phone: " + str(
            s.phone_number) + " Department: " + str(s.department))
        for i in range(0, len(s.list_courses)):
            f.write(" Course" + str(i+1) + ": " + str(s.list_courses[i].name))
        f.write("\n")
    f.close()


def write_all_courses(file_name, list_of_courses):
    f = open(file_name, "w").close()  # clear the file
    f = open(file_name, "a")
    for c in list_of_courses:
        f.write("Name: " + str(c.name) + " Department: " + str(c.dep))
        f.write("\n")
    f.close()
