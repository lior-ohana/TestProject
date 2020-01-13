from Classes.ClassManager import *
from Classes.Course import *
from Classes.Question import *
from Classes.Student import *



def read_file_lecturer(name_file1):
    file = open(name_file1, "r")
    info_file = file.read()
    list_row = info_file.splitlines()  # save list of all the rows in the file
    list_lecture = []  # list of all the lecture
    index_il = 0  # index of the list

    for x in list_row:
        x = x.split(' ')  # save list of all the words in row[i] of the file
        index = 1  # index 1 to take the word after word "name:" -index of the words in row
        name_l = ""
        dep_l = ""
        name_c = ""  # name of the course

        # name of the lecture
        while x[index] != "Password:":
            name_l += x[index] + ' '
            index = index + 1
        list_lecture.append(Lecturer(name_l.strip().capitalize()))  # create object Lecturer

        # password of the lecture
        index = index + 1
        list_lecture[index_il].password = x[index]

        # phone of the lecture
        index = index + 2
        list_lecture[index_il].phone_number = x[index]

        # department of the lecture
        index = index + 2
        while x[index] != "Course1:":
            dep_l += x[index]
            index = index + 1
        list_lecture[index_il].department = dep_l
        index = index + 1

        courses_len = len(x) - index
        list_lecture[index_il].list_courses = []
        # add course to the list of the courses
        for i in range(1, courses_len // 2 + 2):  # until the end of the words in the row
            while index != len(x):
                if x[index] != ("Course" + str(i + 1) + ":"):
                    name_c = name_c + x[index]
                else:
                    list_lecture[index_il].list_courses.append(Course(name_c,dep_l))
                index = index+1
            list_lecture[index_il].list_courses.append(Course(name_c,dep_l))  # entering the last course
        index_il = index_il + 1

    file.close()

    return list_lecture


def read_file_class_manager(name_file1):
    file = open(name_file1, "r")
    info_file = file.read()
    list_row = info_file.splitlines()  # save list of all the rows in the file
    list_class_manager = []  # list of all the lecture
    index_im = 0  # index of the list

    for x in list_row:
        x = x.split(' ')  # save list of all the words in row[i] of the file
        index = 1  # index 1 to take the word after word "name:" -index of the words in row
        name_l = ""
        dep_l = ""
        name_c = ""  # name of the course

        # name of the lecture
        while x[index] != "Password:":
            name_l += x[index] + ' '
            index = index + 1
        list_class_manager.append(Lecturer(name_l.strip().capitalize()))  # create object Lecturer

        # password of the lecture
        index = index + 1
        list_class_manager[index_im].password = x[index]

        # phone of the lecture
        index = index + 2
        list_class_manager[index_im].phone_number = x[index]

        # department of the lecture
        index = index + 2
        while x[index] != "Course1:":
            dep_l += x[index]
            index = index + 1
        list_class_manager[index_im].department = dep_l
        index = index + 1

        courses_len = len(x) - index
        list_class_manager[index_im].list_courses = []
        # add course to the list of the courses
        for i in range(1, courses_len // 2 + 2):  # until the end of the words in the row
            while index != len(x):
                if x[index] != ("Course" + str(i + 1) + ":"):
                    name_c = name_c + x[index]
                else:
                    list_class_manager[index_im].list_courses.append(Course(name_c,dep_l))
                index = index+1
            list_class_manager[index_im].list_courses.append(Course(name_c,dep_l))  # entering the last course
        index_im = index_im + 1

    file.close()

    return list_class_manager


def read_file_student(name_file1):
    file = open(name_file1, "r")
    info_file = file.read()
    list_row = info_file.splitlines()  # save list of all the rows in the file
    list_student = []  # list of all the students
    index_sl = 0  # index course

    for x in list_row:
        x = x.split()  # save list of all the words in row[i] of the file
        name_s = ""  # name of the student
        for i in range(1, len(x)):
            name_s = name_s + x[i]
        list_student.append(Student(name_s.capitalize()))
        index_sl = index_sl + 1

    file.close()
    return list_student


def read_file_course(name_file1):
    file = open(name_file1, "r")
    info_file = file.read()
    list_row = info_file.splitlines()  # save list of all the rows in the file
    list_course = []
    index_c = 0  # index course

    for x in list_row:
        index = 1  # index 1 to take the word after word "name:" -index of the words in row
        x = x.split(' ')  # save list of all the words in row[i] of the file
        name_c = ""
        dep_c = ""

        # name of the course
        while x[index] != "Department:":
            name_c += x[index] + ' '
            index = index + 1
        list_course.append(Course(name_c.strip().capitalize()))

        index = index + 1

        department_len = len(x) - index

        # department of the course
        for i in range(1, department_len + 1):
            dep_c = dep_c + x[index]
        list_course[index_c].department = dep_c

        index_c = index_c + 1

    file.close()
    return list_course


def read_file_question(name_file1, list_solution):
    file = open(name_file1, "r")
    info_file = file.read()
    list_row = info_file.splitlines()  # save list of all the rows in the file
    list_question = []
    index_q = 0  # index course

    for x in list_row:
        index = 1  # index 1 to take the word after word "Code_q:" -index of the words in row
        x = x.split()  # save list of all the words in row[i] of the file
        sub1 = ""
        sub_subject = ""
        level = ""
        type_test = ""
        year = ""
        semester = ""
        term = ""
        format_q = ""

        # code of the question
        list_question.append(Question(x[index]))
        index = index + 2

        # the subject of the question
        while x[index] != "Sub_subject:":
            sub1 = sub1 + x[index] + ' '
            index = index + 1
        list_question[index_q].subject = sub1.strip()

        index = index + 1

        # the sub theme of the question
        while x[index] != "Level:":
            sub_subject = sub_subject + x[index] + ' '
            index = index + 1
        list_question[index_q].sub_subject = sub_subject.strip()

        index = index + 1

        # level of the question
        while x[index] != "Type_test:":
            level = level + x[index] + ' '
            index = index + 1
        list_question[index_q].level = level.strip()

        index = index + 1

        # the type of the test
        while x[index] != "Year:":
            type_test = type_test + x[index] + ' '
            index = index + 1
        list_question[index_q].type_test = type_test.strip()

        index = index + 1

        # the year of the test
        while x[index] != "Semester:":
            year = year + x[index] + ' '
            index = index + 1
        list_question[index_q].year = year.strip()

        index = index + 1

        # the semester of the test
        while x[index] != "Term_test:":
            semester = semester + x[index] + ' '
            index = index + 1
        list_question[index_q].semester = semester.strip()

        index = index + 1

        # term
        while x[index] != "Format_q:":
            term = term + x[index] + ' '
            index = index + 1
        list_question[index_q].term_test = term.strip()

        index = index + 1

        # the format of the question
        while x[index] != "Is_solution:":
            format_q = format_q + x[index] + ' '
            index = index + 1
        list_question[index_q].format_q = format_q.strip()

        index = index + 1
        list_question[index_q].is_solution = x[index]

        if x[index].capitalize() != "False":
            for j in list_solution:
                if j.code_q == list_question[index_q].code_q:
                    list_question[index_q].solution = j
                    break
                    # TODO: check if possible to have more than one solution
        index_q = index_q + 1

    file.close()
    return list_question


def read_file_solution(name_file1):
    file = open(name_file1, "r")
    info_file = file.read()
    list_row = info_file.splitlines()  # save list of all the rows in the file
    list_solution = []
    index_s = 0
    index = 1

    for x in list_row:
        x = x.split(" ")
        # format of the solution
        list_solution.append(Solution(x[index]))
        index = index + 2
        # format of the solution
        list_solution[index_s].format_s = x[index]
        index = index + 2
        # type of the solution
        list_solution[index_s].type_s = x[index]
        index_s += 1
        index = 1

    file.close()

    return list_solution
