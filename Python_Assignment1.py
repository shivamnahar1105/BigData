# Ques -1 
''' we call Python as a general purpose and high-level programming language 
because it is human readbale and easy to work with.
'''

# Ques -2 
''' Because we don't declare variable by giving the type at the starting. Python 
language is intelligent enough that it understands what type we have written while
writing the code.'''

# Ques -3
''' 
Pros - It is easily readable and more human friendly.
     - Declaration of variable can be done dynamically.
     - No curly braces are required for indentation. It can be taken care off 
        with the help of spaces.

Cons - It needs a lot of memory space to make it simple for the developer.
     - Python is used for backed programming; due its high memory usage and slow speed, 
       it is generally not used for frontend programming or mobile app development.

'''

# Ques -4
'''
    - Can be used in data analytics, cloud computing, data science, data engineering, AI, ML.
'''

# Ques -5
'''
    - Variables are the name give to the memory locations.

    Decalration of variable - 
                                a = 10
                                b = "shivam"

'''

# Ques -6 

''' 
     user_input = input("Please give the input: ")
'''

# Ques -7
'''
    default data type -  string
'''

# Ques -8
'''
TypeCasting is the way of changing the defined data type from one data type to another.
    eg : a = 10  # o/p - 10 (int)
         b = str(a) # o/p - "10"   
'''

# Ques -9
'''
Yes, we can take more than one input, by using python in built functions such as split.
It can also be done by using loops.
'''

#Ques -10
'''
keywords are special reserved words that have specific meanings 
and purposes and can't be used for anything but those specific purposes.
'''

# Ques -11
'''
Keywords are the reserved words in Python. 
We cannot use a keyword as a variable name, function name or any other identifier.
They are used to define the syntax and structure of the Python language.
'''

# Ques -12
'''
Indentation are the spaces we give will writing the code. 
It is useful as this is the only way which helps in identifying which statment is inside which
statement.
'''

# Ques -13
''' 
we can use print() function.
'''

# Ques -14
'''
In Python, operators are special symbols
that designate that some sort of computation should be performed.
'''

# Ques -15
'''
/ - this is the division value which is the exact division.
// - gives the floor division for the operation.
'''

# Ques -16
'''
print("iNeuroniNeuroniNeuroniNeuron")
'''

# Ques -17
'''
user_choice = int(input("Enter a number"))

if user_choice % 2 == 0:
    print("It is even number.")
elif user_choice % 2 != 0:
    print("It is odd number.")
else:
    print("Invalid input")    
'''

# Ques -18
'''
Boolean operator are the operators which are used when we want either True or False.
''' 

# Ques -19
'''
    1 or 0 -  O/P will be 1
    0 and 0 - O/P will be 0
    True and False and True - O/P will be False
    1 or 0 or 0 - O/P will be 1
'''

# Ques -20
'''
Conditional statements are the statements, which helps us to define multiple conditions and 
work according to the requirement.

Eg: if, else, elif, nested if, etc.
'''

# Ques -21
'''
'if', 'elif', 'else' keywords are used when we have more than two condtions to define. 
eg : when we have to choose a month and after that we need to perform some operation i.e. diff
depending upon the month we selected.
'''

# Ques -22

# age = int(input("Please enter the age: "))

# if age >= 18:
#     print("I can vote.")
# elif age >1 and age < 18:
#     print("I can't vote")

# Ques -23

# numbers = [12, 75, 150, 180, 145, 525, 50]
# sum = 0
# for num in numbers:
#     if num%2 == 0:
#         sum += num
# print("The sum of all even number is: ",sum)       

# Ques -24

# x, y, z = input("Enter three values: ").split()
# print(x,y,z)
# if x > y and x > z:
#     print("The greatest number is: ", x)
# elif x < y and y > z:
#     print("The greatest number is: ", y)

# elif z > y and x < z:
#     print("The greatest number is: ", z)    

# Ques -25
# numbers = [12, 75, 150, 180, 145, 525, 50]

# # Sorting in ascending order
# numbers.sort()
# # print(numbers)    

# for num in numbers:
#     if num%5 == 0:
#         if num <=150:
#             print(num)
