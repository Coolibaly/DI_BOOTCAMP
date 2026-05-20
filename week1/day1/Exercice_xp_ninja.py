# Exercise 1: Outputs (Predictions + verification)

print("Exercise 1: Outputs (Predictions + verification)\n")

# 3 <= 3 < 9  -> True (both comparisons are True)
print(3 <= 3 < 9)

# 3 == 3 == 3 -> True (all comparisons are True)
print(3 == 3 == 3)

# bool(0) -> False (0 is falsy)
print(bool(0))

# bool(5 == "5") -> False (int vs string not equal)
print(bool(5 == "5"))

# bool(4 == 4) == bool("4" == "4") -> True == True -> True
print(bool(4 == 4) == bool("4" == "4"))

# bool(bool(None)) -> bool(False) -> False
print(bool(bool(None)))

# Mixed boolean + arithmetic
x = (1 == True)      # True
y = (1 == False)     # False
a = True + 4         # 5 (True = 1)
b = False + 10       # 10 (False = 0)

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)


# Exercise 2: Longest sentence without "A"

print("\nExercise 2: Longest sentence without 'A'\n")

# Store the longest valid sentence
longest_sentence = ""

while True:
    sentence = input("Enter a sentence without the letter 'A' (or type 'quit'): ")

    if sentence.lower() == "quit":
        break

    # Check if sentence contains 'A' or 'a'
    if "a" in sentence.lower():
        print("Invalid: sentence contains the letter 'A'. Try again.")
        continue

    # Update longest sentence if needed
    if len(sentence) > len(longest_sentence):
        longest_sentence = sentence
        print("Congratulations! New longest sentence achieved.")
    else:
        print("Good attempt, but not the longest yet.")



# Exercise 3: Paragraph analysis

print("\nExercise 3: Paragraph analysis\n")

paragraph = """
Python is a powerful programming language. It is widely used in data science, web development, and automation.
Many developers choose Python because it is easy to read and learn. Python also has a large community.
"""

# Character count (including spaces)
char_count = len(paragraph)

# Sentence count (split by ".")
sentences = paragraph.split(".")
sentence_count = len([s for s in sentences if s.strip() != ""])

# Word count
words = paragraph.replace("\n", " ").split()
word_count = len(words)

# Unique words (case insensitive)
unique_words = set(word.lower().strip(".,") for word in words)
unique_word_count = len(unique_words)

# Non-whitespace characters
non_whitespace = len(paragraph.replace(" ", "").replace("\n", ""))

# Average words per sentence
avg_words_per_sentence = word_count / sentence_count

# Non-unique words
non_unique_words = word_count - unique_word_count

# Display results
print("\n--- Paragraph Analysis ---")
print("Characters:", char_count)
print("Sentences:", sentence_count)
print("Words:", word_count)
print("Unique words:", unique_word_count)
print("Non-whitespace characters:", non_whitespace)
print("Average words per sentence:", avg_words_per_sentence)
print("Non-unique words:", non_unique_words)