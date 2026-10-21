
file = open("sample.txt", "r")
text = file.read()

count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("Number of vowels:", count)

file.close()
