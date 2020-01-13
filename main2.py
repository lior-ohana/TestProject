from Maagar2 import database
from Classes.ClassManager import *
from Classes.Course import *
from Classes.Question import *
from Classes.Student import *
from Files.readFile import *
from Files.writeFile2 import *
from Classes.LogWriter import *
from datetime import datetime


def start():
    # TODO: add option to EXIT or to get back to the main mane

    f = open("LOG.txt", "w")  # clear the log file
    f.close()

    # reading from files the information we need
    before = datetime.now()
    lecturers = read_file_lecturer("database/Lecturers.txt")
    write_log(datetime.now(), datetime.now() - before, "read file database/Lecturers.txt")

    before = datetime.now()
    class_managers = read_file_class_manager("database/Class_Managers.txt")
    write_log(datetime.now(), datetime.now() - before, "read file database/Class_Managers.txt")

    before = datetime.now()
    students = read_file_student("database/Students.txt")
    write_log(datetime.now(), datetime.now() - before, "read file database/Students.txt")

    questions, solutions, courses = None, None, None

    found = False  # will check if the user was found
    user_type = ""  # will mark if the user is student, lecturer or class manager
    user = None  # will save the user itself
    name = ""
    want_exit = False

    print("Welcome to the Question dataBase.")
    before = datetime.now()
    while not found or not want_exit:
        want_exit = False
        write_log(datetime.now(), datetime.now() - before, "entered login menu")
        print("\nwrite \"Exit\" to exit the program.")
        print("Are you a student? Enter \"YES\" or \"NO\"")
        is_student = input().upper()
        before2 = datetime.now()
        if is_student.upper() == "EXIT":
            want_exit = True
            break
        if is_student == "YES":
            while not found and not want_exit:
                write_log(datetime.now(), datetime.now() - before2, "entered 'student login menu'")
                print("What is your name?")

                before = datetime.now()
                name = input().capitalize()
                if name.upper() == "EXIT":
                    want_exit = True
                    write_log(datetime.now(), datetime.now() - before, "user decided to exit 'student login menu'")
                    continue

                before = datetime.now()
                for x in students:
                    if x.name == name:
                        found = True
                        user_type = "student"
                        user = x
                        write_log(datetime.now(), datetime.now() - before, "user details confirmed, student logged in")
                        break  # student found stop looking
                if not found:
                    print("Name was Not found. Please Enter Again.")
                    write_log(datetime.now(), datetime.now() - before,
                              "user details was not found, error massage showed")

        while not found and not want_exit:
            print("Please enter Your name and password")
            print("Name: ")
            write_log(datetime.now(), datetime.now() - before2, "entered 'lecturer or class-manager login menu'")
            before = datetime.now()
            name = input().capitalize()
            if name.upper() == "EXIT":
                want_exit = True
                continue
            print("Password: ")
            password = input()
            write_log(datetime.now(), datetime.now() - before, "user entered name and password")

            # check if the name and password are compatible
            # check if lecturer
            before = datetime.now()
            for x in lecturers:
                if x.name == name and x.password == password:
                    write_log(datetime.now(), datetime.now() - before, "user details confirmed, lecturer logged in")
                    found = True
                    user = x
                    user_type = "lecturer"
                    break  # we found the user

            if not found:
                write_log(datetime.now(), datetime.now() - before,
                          "user details was not found, searching for class manager")
                # check if class manager:
                before = datetime.now()
                for y in class_managers:
                    if y.name == name and y.password == password:
                        write_log(datetime.now(), datetime.now() - before,
                                  "user details confirmed, class manager logged in")
                        found = True
                        user = y
                        user_type = "class_manager"
                        break  # we found the user

            if not found:
                write_log(datetime.now(), datetime.now() - before, "user details was not found, error massage showed")
                print("Name or password incorrect. Try Again")

        if not want_exit:
            # got here meaning we found the user
            print("Hello, " + name + ".\nWe are sending you to the dataBase now....")

            # getting information we needno
            before = datetime.now()
            solutions = read_file_solution("database/Solutions.txt")
            write_log(datetime.now(), datetime.now() - before, "read file database/Solutions.txt")

            before = datetime.now()
            questions = read_file_question("database/Questions.txt", solutions)
            write_log(datetime.now(), datetime.now() - before, "read file database/Questions.txt")

            before = datetime.now()
            courses = read_file_course("database/Courses.txt")
            write_log(datetime.now(), datetime.now() - before, "read file database/Courses.txt")

            # transferring the user to the dataBase
            list_of_lists = database(user, user_type, class_managers, lecturers, students, questions, solutions,
                                     courses)
            # updating information
            if len(list_of_lists) != 6:
                print("ERROR list_of_lists INVALID!")
            else:
                class_managers, lecturers, students = list_of_lists[0], list_of_lists[1], list_of_lists[2]
                questions, solutions, courses = list_of_lists[3], list_of_lists[4], list_of_lists[5]
                # reset all the user variables to "log out" of the user
                found = False  # will check if the user was found
                user_type = ""  # will mark if the user is student, lecturer or class manager
                user = None  # will save the user itself
                name = ""

    # got here meaning he wants to exit
    # then lets write to files

    # TODO: will we update class_managers? because there is no way to change that list any way

    print("Goodbye!")
    before = datetime.now()
    if questions is not None:
        write_all_questions("database/Questions.txt", questions)
        write_log(datetime.now(), datetime.now() - before, "write file database/Questions.txt")
    before = datetime.now()
    if solutions is not None:
        write_all_solutions("database/Solutions.txt", solutions)
        write_log(datetime.now(), datetime.now() - before, "write file database/Solutions.txt")

    before = datetime.now()
    write_all_students("database/Students.txt", students)
    write_log(datetime.now(), datetime.now() - before, "write file database/Students.txt")

    before = datetime.now()
    write_all_lecturers_class_managers("database/Class_Managers.txt", class_managers)
    write_log(datetime.now(), datetime.now() - before, "write file database/Class_Managers.txt")

    before = datetime.now()
    write_all_lecturers_class_managers("database/Lecturers.txt", lecturers)
    write_log(datetime.now(), datetime.now() - before, "write file database/Class_Managers.txt")

    before = datetime.now()
    if courses is not None:
        write_all_courses("database/Courses.txt", courses)
        write_log(datetime.now(), datetime.now() - before, "write file database/Courses.txt")


start()
