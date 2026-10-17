# Mini Project 2: Student Marks and Grade Report

n = int(input("Enter number of students: "))

if n <= 0:
    print("Invalid number of students.")
else:
    total_marks = 0.0
    passed = 0
    failed = 0

    for _ in range(n):
        name = input("Enter student name: ")
        marks = float(input("Enter marks out of 100: "))

        while marks < 0 or marks > 100:
            print("Invalid marks. Enter a value from 0 to 100.")
            marks = float(input("Enter marks again: "))

        total_marks += marks

        if marks >= 75:
            grade = "A"
        elif marks >= 60:
            grade = "B"
        elif marks >= 50:
            grade = "C"
        elif marks >= 40:
            grade = "D"
        else:
            grade = "Fail"

        if marks >= 40:
            passed += 1
        else:
            failed += 1

        print(f"{name} - Marks: {marks:g}, Grade: {grade}")

    print(f"Class Average: {total_marks / n:.2f}")
    print(f"Pass Count: {passed}")
    print(f"Fail Count: {failed}")
