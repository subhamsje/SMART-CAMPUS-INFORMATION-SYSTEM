# SMART CAMPUS INFORMATION SYSTEM

python
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

students = []


# ==========================================
# STUDENT REGISTRATION & GRADE EVALUATION
# ==========================================

def register_student():

    usn = input("Enter USN : ")
    name = input("Enter Name : ")

    marks = []

    for i in range(3):
        mark = float(input(f"Enter Subject {i+1} Marks : "))
        marks.append(mark)

    average = sum(marks) / len(marks)

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "F"

    student = {
        "USN": usn,
        "Name": name,
        "Marks": marks,
        "Average": average,
        "Grade": grade,
        "Course": "Not Assigned"
    }

    students.append(student)

    print("\nStudent Registered Successfully")
    print("Grade Awarded :", grade)


# ==========================================
# COURSE ENROLLMENT
# ==========================================

def enroll_course():

    usn = input("Enter Student USN : ")

    for student in students:

        if student["USN"] == usn:

            print("\nAvailable Courses")
            print("1. Python Programming")
            print("2. Data Structures")
            print("3. AI Fundamentals")
            print("4. Database Systems")

            course = input("Enter Course Name : ")

            student["Course"] = course

            print("Course Enrolled Successfully")
            return

    print("Student Not Found")


# ==========================================
# DISPLAY RECORDS
# ==========================================

def display_students():

    if len(students) == 0:
        print("No Student Records Found")
        return

    print("\n========== STUDENT RECORDS ==========")

    for student in students:

        print("\nUSN      :", student["USN"])
        print("Name     :", student["Name"])
        print("Course   :", student["Course"])
        print("Marks    :", student["Marks"])
        print("Average  :", round(student["Average"], 2))
        print("Grade    :", student["Grade"])


# ==========================================
# SEARCH STUDENT
# ==========================================

def search_student():

    usn = input("Enter USN to Search : ")

    found = False

    for student in students:

        if student["USN"] == usn:

            print("\nStudent Found")
            print(student)

            found = True
            break

    if not found:
        print("Student Not Found")


# ==========================================
# SORT STUDENTS
# ==========================================

def sort_students():

    if len(students) == 0:
        print("No Records Available")
        return

    sorted_list = sorted(
        students,
        key=lambda x: x["Average"],
        reverse=True
    )

    print("\n===== RANK LIST =====")

    rank = 1

    for student in sorted_list:

        print(
            rank,
            student["Name"],
            "-",
            round(student["Average"], 2)
        )

        rank += 1


# ==========================================
# FEE CALCULATION
# ==========================================

def calculate_fee():

    tuition_fee = float(input("Enter Tuition Fee : "))
    lab_fee = float(input("Enter Lab Fee : "))
    exam_fee = float(input("Enter Exam Fee : "))

    total = tuition_fee + lab_fee + exam_fee

    print("\nTotal Fee =", total)

    return total


# ==========================================
# SAVE RECORDS
# ==========================================

def save_records():

    with open("student_records.txt", "w") as file:

        for student in students:

            file.write(
                f"{student['USN']},"
                f"{student['Name']},"
                f"{student['Course']},"
                f"{student['Average']},"
                f"{student['Grade']}\n"
            )

    print("Records Saved Successfully")


# ==========================================
# READ RECORDS
# ==========================================

def read_records():

    try:

        with open("student_records.txt", "r") as file:

            print("\n===== FILE RECORDS =====")

            for line in file:
                print(line.strip())

    except FileNotFoundError:

        print("Record File Not Found")


# ==========================================
# DIRECTORY SCANNER
# ==========================================

def scan_directory():

    path = input("Enter Folder Path : ")

    try:

        files = os.listdir(path)

        print("\nFiles Available")

        for file in files:
            print(file)

    except FileNotFoundError:

        print("Directory Not Found")

    except PermissionError:

        print("Permission Denied")

    except Exception as e:

        print("Error :", e)


# ==========================================
# PERFORMANCE ANALYTICS
# ==========================================

def performance_analytics():

    if len(students) == 0:

        print("No Student Data Available")
        return

    names = [s["Name"] for s in students]
    averages = [s["Average"] for s in students]

    marks_array = np.array(averages)

    print("\n===== ANALYTICS =====")

    print("Highest Average :", np.max(marks_array))
    print("Lowest Average  :", np.min(marks_array))
    print("Class Average   :", np.mean(marks_array))

    df = pd.DataFrame({
        "Student": names,
        "Average": averages
    })

    print("\nPANDAS DATAFRAME")
    print(df)

    plt.figure(figsize=(8,5))
    plt.bar(names, averages)

    plt.title("Student Performance Analysis")
    plt.xlabel("Students")
    plt.ylabel("Average Marks")

    plt.show()


# ==========================================
# MAIN DASHBOARD
# ==========================================

while True:

    print("\n")
    print("=" * 50)
    print("SMART CAMPUS INFORMATION SYSTEM")
    print("=" * 50)

    print("1. Student Registration")
    print("2. Course Enrollment")
    print("3. Display Student Records")
    print("4. Search Student")
    print("5. Sort Students")
    print("6. Fee Calculation")
    print("7. Save Records")
    print("8. Read Records")
    print("9. Directory Scanner")
    print("10. Performance Analytics")
    print("11. Exit")

    choice = input("\nEnter Choice : ")

    if choice == "1":
        register_student()

    elif choice == "2":
        enroll_course()

    elif choice == "3":
        display_students()

    elif choice == "4":
        search_student()

    elif choice == "5":
        sort_students()

    elif choice == "6":
        calculate_fee()

    elif choice == "7":
        save_records()

    elif choice == "8":
        read_records()

    elif choice == "9":
        scan_directory()

    elif choice == "10":
        performance_analytics()

    elif choice == "11":

        print("\nThank You")
        print("Exiting Smart Campus Information System")
        break

    else:

        print("Invalid Choice")

