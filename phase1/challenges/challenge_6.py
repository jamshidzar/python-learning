scores = {"ali": 82, "sara": 95, "omar": 67}

tuple_scores = tuple(sorted((score for score in scores.values()), reverse=True))

print(tuple_scores)