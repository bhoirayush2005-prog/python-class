



#4.capitalize first letter 
text = text.strip()
print("capitalize first letter:",text.captalize())

#5.title case (capitalize each word)
print(text.title())

#6.count to occurence of a substring
print("  letter c occurs  ", text.count("c"),"times in text")

#7find the position of a substring
print("postion of imcc in text is",text.find("imcc"))

#8replace a substring with another substring
print("replace imcc with IMCC:",text.replace("imcc","IMCC"))

#(split the string into a list of substrings)
print("split the string:",text.split())

#10join a list of strings into a single string
list_of_strings = ["Hello", "World", "from", "IMCC"]
print("join the list of strings:", " ".join(list_of_strings))

#11 uppercase all letters in the string
print("uppercase all letters:",text.upper())

#12 lowercase all letters in the string
print("lowercase all letters:",text.lower())