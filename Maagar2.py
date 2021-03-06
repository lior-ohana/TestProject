import random

from Classes.ClassManager import *
from Classes.Course import *
from Classes.Question import *
from Classes.Student import *
from Files.readFile import *
from Files.writeFile2 import *
from datetime import datetime
from Classes.LogWriter import *


def database(user, user_type, class_managers, lecturers, students, questions, solutions, courses):
    write_log(datetime.now(), datetime.now() - datetime.now(), "entered the data base")
    list2 = []
    if user_type == "class_manager":
        list2 = main_class_manager(user, lecturers, questions, solutions, courses)
        lecturers = list2[0]
        questions = list2[1]
        solutions = list2[2]
        courses = list2[3]
    elif user_type == "lecturer":
        questions, solutions = main_lecturer(user, questions, solutions)
    elif user_type == "student":
        print("the ma'agar is in development")  # the menu for the student is not ready to be used.
    return [class_managers, lecturers, students, questions, solutions, courses]


def main_class_manager(user, lecturers, questions, solutions, courses):
    write_log(datetime.now(), datetime.now() - datetime.now(), "entered the main menu for class manager")
    choice = 0
    print("welcome to class manager menu, please insert number of the action you want to do:\n")
    print("1.add new lecturer to the system\n2.update or remove lecturer\n3.add new question to the system\n"
          "4.update or remove question\n5.exit\n")
    while choice != "5":
        choice = input()
        if choice == "1":
            lecturers = add_lecture(user, lecturers)
        elif choice == "2":
            lecturers = update(lecturers)
        elif choice == "3":
            questions, solutions = add_question(questions, solutions)
        elif choice == "4":
            questions, solutions = update_or_delete_question(questions, solutions)
        elif choice == "5":
            print("Goodbye\n")
            return [lecturers, questions, solutions, courses]
        else:
            print("invalid input, try again.\n")
        print("You're back in the menu. Please choose:\n1.add new lecturer to the system\n2.update or remove lecturer\n"
              "3.add new question to the system\n""4.update or remove question\n5.exit\n")
    return [lecturers, questions, solutions, courses]


def main_lecturer(user, questions, solutions):
    write_log(datetime.now(), datetime.now() - datetime.now(), "entered the main menu for lecturer")
    choice = 0
    print("welcome to class manager menu, please insert number of the action you want to do:\n")
    print("1.add new question\n2.update or remove question info\n3.exit\n")
    while choice != "3":
        choice = input()
        if choice == "1":
            questions, solutions = add_question(questions, solutions)
        elif choice == "2":
            questions, solutions = update_or_delete_question(questions, solutions)
        elif choice == "3":
            print("Goodbye\n")
        else:
            print("invalid input, try again.\n")
        print("You're back in the menu. Please choose:\n1.add new question\n2.update or remove question info\n3.exit\n")
    return [questions, solutions]


# database will return a list of all the lists to the main, for updating the files.


def add_lecture(user, lecturers):
    write_log(datetime.now(), datetime.now() - datetime.now(), "entered the menu for add lecturer")

    temp = ""
    name_course = ""
    new_lecture = Lecturer()

    before = datetime.now()
    print("insert name for lecturer:\n")
    temp = input()
    new_lecture.name = temp
    write_log(datetime.now(), datetime.now() - before, "user entered the lecturer's name")

    before = datetime.now()
    print("insert password for lecturer:\n")
    temp = input()
    new_lecture.password = temp
    write_log(datetime.now(), datetime.now() - before, "user entered the lecturer's password")

    before = datetime.now()
    print("insert phone number for lecturer:\n")
    temp = input()
    new_lecture.phone_number = temp
    write_log(datetime.now(), datetime.now() - before, "user entered the lecturer's phone number")

    before = datetime.now()
    new_lecture.department = user.department
    write_log(datetime.now(), datetime.now() - before, "entered the lecturer's department by class managers")

    before = datetime.now()
    new_lecture.list_courses = []
    while name_course != "-1":
        print("insert courses for the lecture ; if you want to exit press -1\n")
        name_course = input()
        if name_course != "-1":
            new_lecture.list_courses.append(Course(name_course, new_lecture.department))
    write_log(datetime.now(), datetime.now() - before, "user entered the lecturer's courses")

    before = datetime.now()
    lecturers.append(new_lecture)
    write_log(datetime.now(), datetime.now() - before, "new lecturer entered the data base")

    return lecturers


def update(lecturers):
    choice = 0
    print("insert your choice for action:\n")
    print("1.update lecturer info\n 2.remove lecturer from system\n")
    choice = input()
    end = False
    name = ""
    if choice == "1":
        while not end:
            print("insert name of lecturer to update:\nwrite exit to exit.")
            name = input()
            temp = ""
            if name.capitalize() == "Exit":
                end = True
                continue
            found = False
            for x in lecturers:
                if x.name == name.capitalize():
                    print("what do you want to update:\n 1.name\n 2.password\n "
                          "3.phone number\n 4.department\n 5.courses\n")
                    found = True
                    choice2 = input()
                    if choice2 == "1":
                        print("insert new name for lecturer:\n")
                        temp = input()
                        x.name = temp
                        print("name changed.\n\nyou can update another lecturer")
                    elif choice2 == "2":
                        print("insert new password for lecturer:\n")
                        temp = input()
                        x.password = temp
                        print("password changed.\n\nyou can update another lecturer")
                    elif choice2 == "3":
                        print("insert new phone number for lecturer:\n")
                        temp = input()
                        x.phone_number = temp
                        print("phone number changed.\n\nyou can update another lecturer")
                    elif choice2 == "4":
                        print("insert new department for lecturer:\n")
                        temp = input()
                        x.department = temp
                        print("department changed.\n\nyou can update another lecturer")
                    elif choice2 == "5":
                        exit1 = False
                        while not exit1:
                            print("press 1-if you want to delete course\n"
                                  " 2-if you want to add course\n or press -1 to exit\n")
                            choice3 = input()
                            if choice3 == "1":
                                print("Enter the name of the course you want to remove\n")
                                temp = input()
                                for j in x.list_courses:
                                    if x.list_courses.name == temp:
                                        x.list_courses.remove(j)
                            if choice3 == "2":
                                print("insert the name of the course you want to add:\n")
                                temp = input()
                                x.list_courses.append(Course(temp, x.department))
                            elif choice3 == "-1":
                                exit1 = True
                            else:
                                print("you enter invalid number,try again\n")
            if not found:
                print("wrong name")

    if choice == "2":
        print("insert name of lecturer to remove:\n")
        name = input()
        temp = ""

        for x in lecturers:
            if x.name == name.capitalize():
                lecturers.remove(x)
    return lecturers


def add_solution(code_q, list_solutions):
    soul = Solution(code_q)

    print("Please enter Format: ")
    a = input()
    soul.format_s = a.capitalize()
    print("Please enter Type: ")
    b = input()
    soul.type_s = (b.capitalize())

    list_solutions.append(soul)
    return list_solutions


def add_question(list_questions, list_solutions):
    found = False
    ques = None
    code = 0
    while not found:
        code = random.randint(0, 100000)
        for i in list_questions:
            if code == i.code_q:
                found = True
        if not found:
            break

    ques = Question(code)

    # got here meaning we have valid code
    print("Please Enter Subject: ")
    temp = input().capitalize()
    ques.subject = temp
    print("Please Enter Sub_subject: ")
    temp = input().capitalize()
    ques.sub_subject = temp
    print("Please Enter Level: ")
    temp = input().capitalize()
    ques.level = temp
    print("Please Enter Type_test: ")
    temp = input().capitalize()
    ques.type_test = temp
    print("Please Enter Year: ")
    temp = input().capitalize()
    ques.year = temp
    print("Please Enter Semester: ")
    temp = input().capitalize()
    ques.semester = temp
    print("Please Enter Term_test: ")
    temp = input().capitalize()
    ques.term_test = temp
    print("Please Enter Format_q: ")
    temp = input().capitalize()
    ques.format_q = temp
    print("Please Enter if the question has a solution: (yes / no)")
    temp = input().capitalize()
    ques.is_solution = temp

    list_questions.append(ques)
    ls = []

    if temp == "Yes":
        ls = add_solution(code, list_solutions)

    return [list_questions, ls]


def update_or_delete_question(list_questions, list_solutions):
    choice = 0
    code = 0
    temp = ""
    while choice != "3":
        print("insert your choice for action:\n")
        print("1.update question info\n 2.remove question from system\n 3. exit")
        choice = input()
        if choice == "1":
            found = False
            while not found:
                print("insert question code for update\nwrite \"exit\" to exit")
                code = input()
                if code.lower() == "exit":
                    break
                for x in list_questions:
                    if x.code_q == code:
                        found = True
                        print("what do you want to update?\n 1.subject\n 2.sub subject\n"
                              " 3.level\n 4.type test\n 5.year\n 6.semester\n 7.term test\n 8.format\n 9.solution\n")
                        choice = input()
                        if choice == "1":
                            print("insert new subject for question\n")
                            temp = input()
                            x.subject = temp
                        elif choice == "2":
                            print("insert new sub subject\n")
                            temp = input()
                            x.sub_subject = temp
                        elif choice == "3":
                            print("insert new level for question\n")
                            temp = input()
                            if temp >= "1" and temp <= "10":
                                x.level = temp
                            else:
                                print("Error! level must be 1-10!\n")
                        elif choice == "4":
                            print("insert new type test for question\n")
                            temp = input()
                            x.type_test = temp
                        elif choice == "5":
                            print("insert new year for question\n")
                            temp = input()
                            x.year = temp
                        elif choice == "6":
                            print("insert new semester for question\n")
                            temp = input()
                            x.semester = temp
                        elif choice == "7":
                            print("insert new term test for question\n")
                            temp = input()
                            x.term_test = temp
                        elif choice == "8":
                            print("insert new format for question\n")
                            temp = input()
                            x.format_q = temp
                        elif choice == "9":
                            if x.is_solution == False:
                                add_solution(x.code_q, list_solutions)
                            else:
                                exit2 = False
                                while exit2 == False:
                                    print("this question already has a solution\n"
                                          " insert 1 to remove solution\n insert -1 to Exit\n")
                                    choice = input()
                                    if choice == "1":
                                        print("insert question code to remove solution:\n")
                                        code = input()
                                        for y in list_questions:
                                            if y.code_q == code:
                                                list_solutions.remove(y)
                                                y.is_solution = False
                                    elif choice == "-1":
                                        exit2 = True
                        else:
                            print("matching code was not found it the system\n ")
                if not found:
                    print("No question with that code. please try again")
        elif choice == "2":
            list_questions, list_solutions = delete_question(list_questions, list_solutions)
        elif choice != "3":
            print("invalid input")
            # if choise == "3" will end the while and return
    return [list_questions, list_solutions]


def delete_question(list_questions, list_solutions):
    print("insert question code to delete\n")
    code = input()
    for x in list_questions:
        if x.code_q == code:
            list_questions.remove(x)
            # delete solution if exist
            for s in list_solutions:
                if s.code_q == code:
                    list_solutions.remove(s)
            print("question was deleted")
            break
    return [list_questions, list_solutions]
