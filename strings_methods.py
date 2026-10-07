



# #4.capitalize first letter 
# text = text.strip()
# print("capitalize first letter:",text.captalize())

# #5.title case (capitalize each word)
# print(text.title())

# #6.count to occurence of a substring
# print("  letter c occurs  ", text.count("c"),"times in text")

# #7find the position of a substring
# print("postion of imcc in text is",text.find("imcc"))

# #8replace a substring with another substring
# print("replace imcc with IMCC:",text.replace("imcc","IMCC"))

# #(split the string into a list of substrings)
# print("split the string:",text.split())

# #10join a list of strings into a single string
# list_of_strings = ["Hello", "World", "from", "IMCC"]
# print("join the list of strings:", " ".join(list_of_strings))

# #11 uppercase all letters in the string
# print("uppercase all letters:",text.upper())

# #12 lowercase all letters in the string
# print("lowercase all letters:",text.lower())

# #concat 3 strings
# string1 = "Ha"
# string2 = "ha"
# string3 = "HA"
# print("concat 3 strings:", string1 + string2 + string3)

# #find occurence of a letter in a string
# string = input("enter your name:")
# print("occurence of a in your name is:", string.count("a"))

# #replace a letter from a string with another letter
# string = input("enter your name:")
# print("after replacement:", string.replace("a","Z"))

# #split  a string
# string = "ayush"
# name = [string[:3],string[3:5]]
# print("name")


# #sort the string 
# string = "ayush"
# sorted_string = sorted(string)
# print("sorted_string")


#create a list of 10 numbers and display the sum of last 4 elements
list = [1,2,3,4,5,6,7,8,9,10]
str = sum(list[:-4])
print(str)
# remove the items from the list located at 2nd and 5th position
print("list before removing items:", list)
# remove the 5th item first, then the 2nd item to avoid index shifting
removed_items = [list.pop(4), list.pop(1)]
print("removed items:", removed_items)
print("list after removing items:", list)


#print the difference between highest and smalllest number of the list

print("difference between highest and smallest number:", max(list) - min(list))
#append the new element in the list which is half of the item of 3rd position in the list

list.append(list[2]/2)
print("list after appending the new element:", list)
