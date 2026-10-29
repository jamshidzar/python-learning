students = ["ali", "sara", "omar", "lina"]
scores = [82, 95, 67, 74]

for i, (student, score) in enumerate(zip(students, scores), start=1):
    if score >= 70:
        print(f"{i}. {student}: {score} - Passed")
    else:
        print(f"{i}. {student}: {score} - Failed")
