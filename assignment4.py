# Read a file, split its content into words, and store them in a list.
# Print the total number of words.
# Print all unique words.



file = open("sample.txt", "r")

text = file.read()
words = text.split()

print("Total words:", len(words))

unique_words = list(set(words))
print("Unique words:", unique_words)

file.close()
