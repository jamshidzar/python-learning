answer_key = ["a", "c", "b", "d", "a", "c"]
answers = ["a", "b", "b", "d", "c", "c"]

score = 0
wrong = []

for question, (correct, given) in enumerate(zip(answer_key, answers), start=1):
    if given != correct:
        wrong.append(str(question))
    else:
        score += 1

print(f"Score: {score}/{len(answer_key)}")
print(f"Wrong: {', '.join(wrong)}")
