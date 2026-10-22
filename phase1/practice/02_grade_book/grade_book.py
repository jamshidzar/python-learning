"""
Student Grade Book: a CLI app to add students, record their grades,
and see averages, letter grades and who is passing.
"""

PASSING_GRADE = 60


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


def average(grades):
    return sum(grades) / len(grades)


def letter_grade(avg):
    if avg >= 90:
        return "A"
    if avg >= 80:
        return "B"
    if avg >= 70:
        return "C"
    if avg >= 60:
        return "D"
    return "F"


def show_report(grade_book):
    print("\n--- REPORT ---")

    if not grade_book:
        print("No students yet.")
        return

    # Step 3: one line per student, and collect averages for the summary
    averages = {}
    for name, grades in grade_book.items():
        if grades:
            avg = average(grades)
            averages[name] = avg
            print(f"{name}: {avg:.1f} ({letter_grade(avg)})")
        else:
            print(f"{name}: no grades yet")

    if not averages:
        return

    # Step 4: class summary
    passing = [name for name, avg in averages.items() if avg >= PASSING_GRADE]
    class_avg = average(list(averages.values()))

    top_name = ""
    top_avg = -1
    for name, avg in averages.items():
        if avg > top_avg:
            top_name = name
            top_avg = avg

    print("\n--- SUMMARY ---")
    if passing:
        print(f"Passing: {', '.join(passing)}")
    else:
        print("Passing: none")
    print(f"Class average: {class_avg:.1f}")
    print(f"Top student: {top_name} ({top_avg:.1f})")


def main():
    grade_book = {}

    while True:
        print("\n=== GRADE BOOK ===")
        print("1. Add student")
        print("2. Add grade")
        print("3. Show students")
        print("4. Report")
        print("5. Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student(grade_book)
        elif choice == "2":
            add_grade(grade_book)
        elif choice == "3":
            show_students(grade_book)
        elif choice == "4":
            show_report(grade_book)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-5.")


main()
