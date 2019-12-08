from Classes.ClassManager import *
from Classes.Course import *
from Classes.Question import *
from Classes.Student import *


def write_lecturer_class_manager(user):
    f = None
    if type(user) == type(ClassManager):
        f = open("Class_Mangers.txt", "a")
    if type(user) == type(Lecturer):
        f = open("Lecturers.txt", "a")
    else:
        return -1

    f.write("Name:"+user.name + " Phone:"+user.phone + " Department:"+user.department)
    for i in range(1, len(user.list_courses)):
        f.write(" Course" + str(i) + ":" + user.list_courses[i])
    f.close()
    return 1


def write_student(user):
    if type(user) != type(Student):
        return -1
    f = open("Students.txt", "a")
    f.write("Name:"+user.name)
    f.close()
    return 1


def write_course(course1):
    if type(course1) != type(Course):
        return -1
    f = open("Courses.txt", "a")
    f.write("Name:"+course1.name+" Department:"+course1.dep)
    f.close()
    return 1


def write_solution(solution1):
    if type(solution1) != type(Solution):
        return -1
    f = open("Solutions.txt", "a")
    f.write("Code_q:"+solution1.code_q+"Format_s:"+solution1.format_s + "Type:"+solution1.type)
    f.close()
    return 1


def write_question(question1):
    if type(question1) != type(Question):
        return -1
    f = open("Questions.txt", "a")
    f.write("Code_q:"+question1.code_q+"Subject:"+question1.subject+"Sub_subject:"+question1.sub_subject+"Level:" +
            question1.level+"Type_test:"+question1.type_test+"Year:"+question1.year+"Semester:"+question1.semester +
            "Term_test:"+question1.term_test+"Format_q:"+question1.format_q+"Is_solution:"+question1.is_solustion)
    f.close()
    return 1

