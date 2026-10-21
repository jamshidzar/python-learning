# word_counter.py

text = """
Python is great. Python is easy to learn,
and Python is used for backend work.
Backend developers love Python! Is it the best?
"""

stop_words = {"is", "to", "and", "for", "it", "the"}

# 2. Clean the words
words = [word.strip(".,!?").lower() for word in text.split()]

# 3. Remove boring words
meaningful_words = [word for word in words if word not in stop_words]

# 4. Count each word
word_counts = {}
for word in meaningful_words:
    word_counts[word] = word_counts.get(word, 0) + 1

# 5. Unique words
unique_words = {word for word in meaningful_words}

# 6. Popular words
popular_words = {word: count for word, count in word_counts.items() if count >= 2}

# 7. Report
print(f"Total words: {len(meaningful_words)}")
print(f"Unique words: {len(unique_words)}")
print()
print("Words used 2+ times:")
for word, count in popular_words.items():
    print(f"{word}: {count}")
