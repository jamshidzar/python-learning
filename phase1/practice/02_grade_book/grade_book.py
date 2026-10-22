"""
Student Grade Book: a CLI app to add students, record their grades,
and see averages, letter grades and who is passing.
"""


def add_student(grade_book):
    name = input("Student name: ").strip().title()

    if name == "":
        print("Name can't be empty.")
        return
    if any(ch.isdigit() for ch in name):
        print("Name can't contain numbers.")
        return
    if name in grade_book:
        print(f"{name} is already in the grade book.")
        return

    grade_book[name] = []
    print(f"Added {name}.")


def add_grade(grade_book):
    if not grade_book:
        print("No students yet. Add a student first.")
        return

    name = input("Student name: ").strip().title()
    if name not in grade_book:
        print(f"{name} is not in the grade book.")
        return

    try:
        grade = int(input("Grade (0-100): ").strip())
    except ValueError:
        print("Grade must be a whole number from 0 to 100.")
        return

    if not 0 <= grade <= 100:
        print("Grade must be a whole number from 0 to 100.")
        return

    grade_book[name].append(grade)
    print(f"Added {grade} to {name}.")


def show_students(grade_book):
    print("\n--- STUDENTS ---")

    if not grade_book:
        print("No students yet.")
        return

    for name, grades in grade_book.items():
        if grades:
            grades_text = ", ".join(str(g) for g in grades)
            print(f"{name}: {grades_text}")
        else:
            print(f"{name}: no grades yet")


def main():
    grade_book = {}

    while True:
        print("\n=== GRADE BOOK ===")
        print("1. Add student")
        print("2. Add grade")
        print("3. Show students")
        print("4. Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student(grade_book)
        elif choice == "2":
            add_grade(grade_book)
        elif choice == "3":
            show_students(grade_book)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-4.")


main()
