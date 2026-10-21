# #create dictionary with student details
# students = {
#     101: {"name": "John", "age": 20, "grade":[85, 90, 95]},
#     102: {"name": "Alice", "age": 22, "grade":[55,72,98]},
#     103: {"name": "Bob", "age": 21, "grade": [10,20,30]},
#     104: {"name": "Charlie", "age": 23, "grade":[60,80,70]}
#     105: {"name": "David", "age": 24, "grade":[75,85,95]}
# }


# #calculate average grade for each student and flag pass or fail
# for sid, details in students.items():
#     avg_grade = sum(details["grade"]) / len(details["grade"])
#     details["average_grade"] = avg_grade
#     details["passed"] = avg_grade >= 50

# #print names of passed students
# print("Students who passed:")    
# for sid, details in students.items():
#     if details["passed"]:
#         print(f" - {details['name']}")