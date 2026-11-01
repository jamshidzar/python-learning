from shlex import join


words = ["cat", "elephant", "dog", "giraffe", "ox"]
biggest_words = []
for i, word in enumerate(words, start=1):
    if len(word) > 3:
        biggest_words.append(str(i))

print(f"long words: {', '.join(biggest_words)}")
