
file = open("sample2.txt", "r")

lines = file.readlines()

print("Total lines:", len(lines))
print("Second line:", lines[1])
print("Fourth line:", lines[3])

file.close()
