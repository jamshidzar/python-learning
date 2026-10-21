students = ("Ali", "Sara", "Omar", "Nadia")
math = (85, 92, 58, 74)
python = (90, 88, 62, 70)

averages = []
for rank, (student, m, p) in enumerate(zip(students, math, python), start=1):
    average = (m + p) / 2
    averages.append(average)

    if average >= 60:
        status = "PASS"
    else:
        status = "FAIL"

    print(f"{rank}. {student}: {average} {status}")

print(f"Class average: {sum(averages) / len(averages):.1f}")
