sentence = "the cat and the hat and the bat"

set_sentence = set(sentence.split())
print(len(set_sentence))

#sorted

list_sentence = list(set_sentence)
list_sentence.sort()
print("-".join(list_sentence))



pairs = [("a", 1), ("b", 2), ("c", 3)]
dic ={}

for letter,num in pairs:
    dic[num] = letter

print(dic)