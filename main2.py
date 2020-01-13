from Maagar2 import database
from Classes.ClassManager import *
from Classes.Course import *
from Classes.Question import *
from Classes.Student import *
from Files.readFile import *
from Files.writeFile2 import *


def start():
    # TODO: add option to EXIT or to get back to the main mane

    # reading from files the information we need
    lecturers = read_file_lecturer("database/Lecturers.txt")
    class_managers = read_file_class_manager("database/Class_Managers.txt")
    students = read_file_student("database/Students.txt")
    questions, solutions, courses = None, None, None

    found = False  # will check if the user was found
    # user_type = ""  # will mark if the user is student, lecturer or class manager
    user = None  # will save the user itself
    name = ""
    want_exit = False

    print("Welcome to the Question dataBase.")
    while not want_exit:
        print("write \"Exit\" to exit the program.\n")
        print("Are you a student? Enter \"YES\" or \"NO\"")
        is_student = input().upper()
        if is_student.upper() == "EXIT":
            want_exit = True
            continue
        if is_student == "YES":
            while not found and not want_exit:
                print("What is your name?")
                name = input().capitalize()
                if name == "Exit":
                    want_exit = True
                    continue
                for x in students:
                    if x.name == name:
                        found = True
                        user_type = "student"
                        user = x
                        break  # student found stop looking
                    else:
                        print("Name was Not found. Please Enter Again.")

        while not found and not want_exit:
            print("Please enter Your name and password")
            print("Name: ")
            name = input().capitalize()
            if name.upper() == "EXIT":
                want_exit = True
                continue
            print("Password: ")
            password = input()

            # check if the name and password are compatible
            # check if lecturer
            for x in lecturers:
                if x.name == name and x.password == password:
                    found = True
                    user = x
                    user_type = "lecturer"
                    break  # we found the user

            if not found:
                # check if class manager:
                for y in class_managers:
                    if y.name == name and y.password == password:
                        found = True
                        user = y
                        user_type = "class_manager"
                        break  # we found the user

            if not found:
                print("Name or password incorrect. Try Again")

        if not want_exit:
            # got here meaning we found the user
            print("Hello, " + name + ".\nWe are sending you to the dataBase now....")

            # getting information we needno


            solutions = read_file_solution("database/Solutions.txt")
            questions = read_file_question("database/Questions.txt", solutions)
            courses = read_file_course("database/Courses.txt")

            # transferring the user to the dataBase
            list_of_lists = database(user, user_type, class_managers, lecturers, students, questions, solutions, courses)
            # updating information
            if len(list_of_lists) != 6:
                print("ERROR list_of_lists INVALID!")
            else:
                class_managers, lecturers, students = list_of_lists[0], list_of_lists[1], list_of_lists[2]
                questions, solutions, courses = list_of_lists[3], list_of_lists[4], list_of_lists[5]

    # got here meaning he wants to exit
    # then lets write to files

    # TODO: will we update class_managers? because there is no way to change that list any way

    print("Goodbye!")
    if questions is not None:
        write_all_questions("database/Questions.txt", questions)
    if solutions is not None:
        write_all_solutions("database/Solutions.txt", solutions)
    write_all_students("database/Students.txt", students)
    write_all_lecturers_class_managers("database/Class_Mangers.txt", class_managers)
    write_all_lecturers_class_managers("database/Lecturers.txt", lecturers)
    if courses is not None:
        write_all_courses("database/Courses.txt", courses)


start()
