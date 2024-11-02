# Concept of pointers in Python variables (immutable objects)

num1 = 11      # num1 references the memory address of 11 (an immutable integer)
num2 = num1    # num2 now references the same memory address as num1 (address of 11)

print("Num 1 is", num1)    # prints the value that num1 references (output: 11)
print("Num 2 is", num2)    # prints the value that num2 references (output: 11)

print("Num 1 points to", id(num1))    # prints the memory address that num1 references
print("Num 2 points to", id(num2))    # prints the memory address that num2 references (should be the same as num1)

num1 = 22      # num1 now references a new memory address for 22 (since integers are immutable)
print("Num 1 is", num1)    # prints the value that num1 references (output: 22)
print("Num 2 is", num2)    # prints the value that num2 still references (output: 11)

print("Num 1 points to", id(num1))    # prints the new memory address that num1 references
print("Num 2 points to", id(num2))    # prints the original memory address that num2 still references


# Concept of pointers in Python dictionaries (mutable objects)

dict1 = {'value': 11}     # dict1 references a memory address holding the dictionary object
dict2 = dict1             # dict2 now references the same memory address as dict1

print("Dict 1 is", dict1)    # prints the content of dict1 (output: {'value': 11})
print("Dict 2 is", dict2)    # prints the content of dict2 (output: {'value': 11})

print("Dict 1 points to", id(dict1))    # prints the memory address that dict1 references
print("Dict 2 points to", id(dict2))    # prints the memory address that dict2 references (should be the same as dict1)

dict1['value'] = 22       # modifies the value within the dictionary object that both dict1 and dict2 reference

print("Dict 1 is", dict1)    # prints the modified content of dict1 (output: {'value': 22})
print("Dict 2 is", dict2)    # prints the modified content of dict2 (output: {'value': 22}) as both reference the same dictionary

print("Dict 1 points to", id(dict1))    # prints the same memory address as before (since dict1 was modified in place)
print("Dict 2 points to", id(dict2))    # still points to the same memory address as dict1
