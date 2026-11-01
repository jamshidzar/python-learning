answer_key = ["b", "a", "c", "c"]
answers = ["b", "c", "c", "a"]

score = 0
wrong = []

for question, (correct, given) in enumerate(zip(answer_key, answers), start=1):
    if given == correct:
        score += 1
    else:
        wrong.append(str(question))

print(f"Score: {score}/{len(answer_key)}")
print(f"Wrong: {', '.join(wrong)}")
