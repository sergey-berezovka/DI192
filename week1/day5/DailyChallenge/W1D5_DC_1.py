# 1 Sorting
# Step 1
user_input = input("Enter words separated by commas: ")
# Step 2
words = user_input.split(",")
# Step 3
words.sort()
# Step 4:
sorted_words = ",".join(words)
# Step 5:
print(sorted_words)

# Challenge 2: Longest Word
def longest_word(sentence):
    words = sentence.split()
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest
print(longest_word("I am studiing at the \"Developers Institute\""))





