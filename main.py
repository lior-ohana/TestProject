from Maagar import database
from Classes.ClassManager import *
from Classes.Course import *
from Classes.Question import *
from Classes.Student import *
from Files.readFile import *
from Files.writeFile import *


def main():
    # TODO: add option to EXIT or to get back to the main mane

    # reading from files the information we need
    lecturers = read_file_lecturer("Lecturers.txt")
    class_managers = read_file_class_manager("Class_Mangers.txt")
    students = read_file_student("Students.txt")

    found = False  # will check if the user was found
    user_type = ""  # will mark if the user is student, lecturer or class manager
    user = None  # will save the user itself
    name = ""

    print("Welcome to the Question dataBase.")
    print("Are you a student? Enter \"YES\" or \"NO\"")
    is_student = input().upper()
    if is_student == "YES":
        while not found:
            print("What is your name?")
            name = input().capitalize()
            for x in students:
                if x.name == name:
                    found = True
                    user_type = "student"
                    user = x
                    break  # student found stop looking
                else:
                    print("Name was Not found. Please Enter Again.")

    while not found:
        print("Please enter Your name and password")
        print("Name: ")
        name = input()
        print("Password: ")
        password = input()

        # check if the name and password are compatible
        # check if lecturer
        for x in lecturers:
            if x.name == name and x.password == password:
                found = True
                user_type = "lecturer"
                user = x
                break  # we found the user

        if not found:
            # check if class manager:
            for x in class_managers:
                if x.name == name and x.password == password:
                    found = True
                    user_type = "class_manager"
                    user = x
                    break  # we found the user

        if not found:
            print("Name or password incorrect. Try Again")

    # got here meaning we found the user
    print("Hello," + name + ".\nWe are sending you to the dataBase now....")

    # transferring the user to the dataBase
    database(user, user_type)


