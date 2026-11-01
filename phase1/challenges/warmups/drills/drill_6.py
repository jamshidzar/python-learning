answer_key = ["b", "a", "c", "c"]
answers = ["b", "a", "c", "a"]
score = 0
wrong = []
for i, (key, answer) in enumerate(zip(answer_key, answers), start=1):
    if key == answer:
        score += 1

    else:
        wrong.append(str(i))


print(f"Score: {score}/{len(answers)}\nWrong: {', '.join(wrong)}")
