age = 23
""" The following line is syntactically incorrect because the interpreter is confused about how to execute the + operator with it including multiple data types, two of which are strings and one of which is an integer.  
message = "Happy " + age + "rd Birthday!"
"""

#cast the integer variable as a string
message = "Happy " + str(age) + "rd Birthday!"
print(message)