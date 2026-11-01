names = ["ali", "sara", "omar", "lina"]
scores = [82, 95, 67, 74]
passing_grade = []
for name, score in zip(names, scores):
    if score >= 75:
        passing_grade.append(name)
print(f"top student: {' '.join(passing_grade)} ")
