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

# Ques -26
'''
string is data type in python.
declaring of string: 
a = ""
'''

# Ques - 27

# example_string = "Shivam"

# # Accessing string through the index.
# print(example_string[0])

# Ques -28

# string = "Big Data iNeuron"
# desired_output = string.split(' ')
# print("desired_output = " , desired_output[2])

# Ques -29

# string = "Big Data iNeuron"
# split_string = string.split(' ')
# required_string = split_string[2]

# desired_output = ""

# i = -1
# for words in range(len(required_string)):
#     desired_output += required_string[i]
#     i -= 1

# print("desired_output = ",desired_output)    
   
# Ques -30

# string = "Big Data iNeuron"
# desired_output = ""

# i = -1
# for words in range(len(string)):
#     desired_output += string[i]
#     i -= 1

# print("desired_output = ",desired_output) 

# Ques -31
'''
aString = ''
print aString
del aString
'''

#Ques -32
'''
An escape character is a backslash \ followed by the character you want to insert.
\n = line change 
\t = tab space 
'''

# Ques -33

# a = "iNeuron's Big Data Course"
# print(a)

# Ques -34
'''
List is a data type in python, which isbascially used for collection of heterogenous items.
It is mutable.
'''
# Ques -35

# create_list = []


# Ques -36

# demo_list = [23, 44, 'shivam', 'satyam']

# # Accessing element from the list.

# print(demo_list[2])

# Ques -37

# lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]

# print(lst[4][2])

# Ques -38

# lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]

# print(len(lst))

# Ques -39

# lst = ["Welcome", "to", "Data", "course"]

# lst.insert(2, 'Big')
# print(lst)

# Ques -40

'''
Tuple is also a data type in python. It is immutable where as the list is mutable.
'''

# Ques -41
'''
creating a tuple 
empty_tuple = ()
'''

# Ques -42
'''
demo_tuple = ('shivam', 'nahar')

demo_tuple[1] = 'satyam'

print(demo_tuple)

We won't be able to add an item to the tuple as it is immutable.
'''

# Ques -43
''' 
tup1 = (1,2,3)
tup2 = (4,5)
tup1.append(tup2)

We won't be able to append an item to the tuple as it is immutable.
'''

# Ques -44

# tup1 = (1,2,3,'shivam')
# print("Count of the tup1 = ",len(tup1))

# Ques -45
'''
sets is one of the data type in python, which contains only unique elements.
'''

# Ques -46
'''
x = set() # creating a empty set.
'''

# Ques -47

# a_set = {1,2,3,'shivam'}
# a_set.add('iNeuron')
# print(a_set)

# Ques -48
'''
a_set = {1,2,3,'shivam'}
a_set.add('iNeuron','satyam')
print(a_set)

we won't be able to add multiple elements with add. As it takes exactly one argument.
'''

# Ques -49
'''
update() can add multiple elements to set while add() can add only one element.
'''

# Ques -50
'''
The clear() method removes all elements in a set.
'''

# Ques -51
'''
Frozen set is just an immutable version of a Python set object.
'''
# Ques -52
'''
Frozen set is just an immutable version of a Python set object. 
While elements of a set can be modified at any time, 
elements of the frozen set remain the same after creation.
'''
# Ques -53
 
# Union is accumulating all the values of sets together.

# set1 = {1,2,3}
# set2 = {5,6,7}
# print(set1 | set2 )

# Ques -54

# intersection means the common values in the given sets.
# set1 = {1,2,3}
# set2 = {2,6,7}
# print(set1 & set2 )

# Ques -55


# Ques -56
'''
Dictionary has a key value pair i.e. a kind of mapping, which is not visible in any
other data type.
'''
# Ques -57
'''
declare a dictionary 

dict1 = {}
'''

# Ques -58 
'''
o/p will be <class 'dict'>
'''

# Ques -59

# dict1 = {}

# dict1['Player'] = 'Lebron James'
# dict1['Game'] = 'Basketball'
# print(dict1)

# Ques -60
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# for keys, values in thisdict.items():
#     print(values)

# Ques -61

# myfamily = {

#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,

#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
# }

# print(myfamily['child2'])

# Ques -62
'''
The get() method returns the value of the item with the specified key.
'''

# Ques -63
''' 
The items() method returns a view object.
The view object contains the key-value pairs of the dictionary, as tuples in a list.

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

print(x)
'''

# Ques -64
''' 
The pop() method removes the item at the given index from the list and returns the removed item.

# create a list of prime numbers
prime_numbers = [2, 3, 5, 7]

# remove the element at index 2
removed_element = prime_numbers.pop(2)

print('Removed Element:', removed_element)
print('Updated List:', prime_numbers)

# Output: 
# Removed Element: 5
# Updated List: [2, 3, 7]
'''

# Ques -65
''' 
The keys() method returns a view object.
The view object contains the keys of the dictionary, as a list.
'''

# Ques -66
''' 
The keys() method returns a view object.
The view object contains the keys of the dictionary, as a list.

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()

print(x)
'''

# Ques -67
''' 
The values() method returns a view object.
The view object contains the values of the dictionary, as a list.
'''

# Ques -68
''' 
Loops are the process which helps us to define a condition so that we can do large jobs
which needs similar operation.
'''

# Ques -69
''' 
There are two loops in python for & while.
'''

# Ques -70
''' 
for loops -  it is used when we know how long the tasks should run.

while loops -  it is used when we do not know how the long loop should run.
'''

# Ques -71
''' 
The continue keyword is used to end the current iteration in a for loop (or a while loop),
and continues to the next iteration.
'''

# Ques -72
''' 
The break statement in Python terminates the current loop
and resumes execution at the next statement
'''

# Ques -73
''' 
The pass statement is used as a placeholder for future code. When the pass statement is executed, 
nothing happens, but you avoid getting an error when empty code is not allowed.
'''

# Ques -74
''' 
Range() is used to define the range of numbers we want and the difference between
the subsequent numbers.
'''

# Ques -75

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# for keys, values in thisdict.items():
#     print(keys, values)

# Ques -76

# def factorial(n):

#     if n == 0 or n == 1:
#         answer = 1
#         print(f"The factorial of {n} is : {answer}")

#     else:
#         num = 1
#         for i in range (n+1):
#             i = i+1
#             num = num*i

#         print(f"The factorial of {n} is : {num}")    
    
# factorial(n)

# Ques -77

# def simple_interest(principal,rate,time):
#     simple_interest = (principal * rate * time )/ 100
#     print(f"Simple Interest is : {simple_interest}")

# p = int(input("Enter the principal value: "))
# r = int(input("Enter the rate : "))
# t = int(input("Enter the time in years : "))

# simple_interest(p, r, t)

# Ques -78

# def compound_interest(principal,rate,time):
#     # Amount = principal ((1 + rate/100) ** time )
#     a = (1 + rate/100) ** time 
#     Amount = principal * a
#     print(f"compound Interest is : {Amount}")

# p = int(input("Enter the principal value: "))
# r = int(input("Enter the rate : "))
# t = int(input("Enter the time in years : "))

# compound_interest(p, r, t)

# Ques -79

# number = int(input("Enter the number : "))


# def prime_numbers(number):
#     if number == 2:
#         print(f"{number} is an even prime number.")
#     elif number == 1:
#         print(f"{number} is not a prime number.") 
#     elif number <= 0:
#         print("Please enter a value greater than 1.") 
#     else:          
#         for i in range(2,number):
#             if number%i == 0:
#                 print(f"{number} is not a prime number.")
#                 break
#         print(f"{number} is a prime number.")

# prime_numbers(number)

# Ques -80

##### Armstrong number
# number = int(input("Enter the number : "))

# def Armstrong(number):
#     temp = number
#     sum = 0
#     while temp > 0:
#         r = temp%10
#         sum = sum + (r*r*r)
#         temp = temp//10
#     if number == sum:
#         print(f"{number} is an armstrong number.")
#     else:
#         print(f"{number} is not an armstrong number.")        
         

# Armstrong(number)    

# Ques -81

#### Fibonacci Number

# Program to display the Fibonacci sequence up to n-th term

# nterms = int(input("How many terms? "))

# # first two terms
# n1, n2 = 0, 1
# count = 0

# # check if the number of terms is valid
# if nterms <= 0:
#    print("Please enter a positive integer")
# # if there is only one term, return n1
# elif nterms == 1:
#    print("Fibonacci sequence upto",nterms,":")
#    print(n1)
# # generate fibonacci sequence
# else:
#    print("Fibonacci sequence:")
#    while count < nterms:
#        print(n1)
#        nth = n1 + n2
#        # update values
#        n1 = n2
#        n2 = nth
#        count += 1

# Ques -82

# ## Making the kist dynamically.
# my_list = []
# num = int(input("how many numbers in the list required ? "))
# for i in range(num):
#     my_list.append(i)

# print(my_list)    

# ## Interchange the first and the last element of the list.

# a = my_list[0]
# my_list[0] = my_list[-1]
# my_list[-1] = a

# print(f"New list is: {my_list}")

## Ques -84

# my_list = [76, 84 , 23 , 45, 106, 199, 143, 584]
# largest = my_list[0]

# for num in range(len(my_list)-1):
    
#     if my_list[num+1] > largest:
#         largest = my_list[num+1]
#     else:
#         continue
# print(largest)

# Ques -85

# my_list = [76, 84 , 23 , 45, 106, 199, 143, 584]

# sum = 0
# for num in my_list:     
#     sum = sum + num

# print(f" The total sum of the given list is : {sum}")    
    
# Ques -86


# def reverse_string(my_input):
#     y = "" #empty string

#     a = len(my_input)
#     print(my_input)
#     for i in range(a):
#         y = y + my_input[(a - 1)-i]
#     print(y)

#     if y == my_input:
#         print(f"The {my_input} is a pallindrome string.")
#     else:
#         print(f"The {my_input} is not a pallindrome string.")    

# chosen = input("Enter the string to be reversed: ")

# reverse_string(chosen)

# Ques -87

# def remove_char(s, i):
#     a = s[ : i]
#     b = s[i + 1: ]

#     return a+b

# string = "Pythonisgood"
# # Remove ith index element
# i = 5
# print(remove_char(string,i-1))

# Ques -88

# Chosen = input("Enter the string: ")
# substring = input("Enter the substring to check: ")

# if substring in Chosen:
#     print(f"{substring} is present in the {Chosen}")
# else:
#     print(f"{substring} is not present in the {Chosen}")    

# Ques - 89

# def string_k(k, str):
     
#     # create the empty string
#     string = []
     
#     # split the string where space is comes
#     text = str.split(" ")
     
#     # iterate the loop till every substring
#     for x in text:
         
#         # if length of current sub string
#         # is greater than k then
#         if len(x) > k:
             
#             # append this sub string in
#             # string list
#             string.append(x)
             
#      # return string list
#     return string
 
 
# # Driver Program    
# k = 3
# str ="geek for geeks"
# print(string_k(k, str))



# Ques - 90

# test_dict = {'gfg': [5, 6, 7, 8],
#              'is': [10, 11, 7, 5],
#              'best': [6, 12, 10, 8],
#              'for': [1, 2, 5]}
 
# # printing original dictionary
# print("The original dictionary is : " + str(test_dict))
 
# # Extract Unique values dictionary values
# # Using set comprehension + values() + sorted()
# res = list(sorted({ele for val in test_dict.values() for ele in val}))
 
# # printing result
# print("The unique values list is : " + str(res))

# Ques -91

# dict1 = {'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}
# dict2 = {'Lebron': 6, 'Kobe Bryant': 24, 'Steph Curry': 30, 'Michal Jordan': 23}

# print({**dict1, **dict2})

# Ques -92

# data = [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
# # Output : {'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}
# print(dict(data))


# Ques -93

# list1 = [9, 5, 6]

# result = [ (x, x**3 ) for x in list1 ]
# print(result)

# Ques -94

# test_tuple1 = (7, 2)
# test_tuple2 = (7, 8)

# result = [ (x,y) for x in test_tuple1 for y in test_tuple2 ]
# final_result = result + [ (y,x) for x in test_tuple1 for y in test_tuple2]
# print(final_result) 




# Ques -95

# tup1 =  [('for', 24), ('Geeks', 8), ('Geeks', 30)] 

# def takeelement(ele):
#     return ele[1]

# tup1.sort(key = takeelement)
# print(tup1)

# Ques -96

## rows = int(input("Enter number of rows: "))

# a = "*"
# for i in range(5):

#     for j in range(i+1): 
#         c = a
#         print(c, end = "")
#     c = a + "*"
#     print("\r")

# Ques -97

# height = 5
# for row in range(1, height+ 1):
#     print(" " * (height - row) +"*" * row)

# Ques -98
# n = int(input("Enter the number of rows: "))  
# m = (2 * n) - 2
# for i in range(0, n+1):  
#     for j in range(0, m):  
#         print(end=" ")  
#     m = m - 1  # decrementing m after each loop  
#     for j in range(0, i + 1):  
#         # printing full Triangle pyramid using stars  
#         print("* ", end=' ')  
#     print(" ")     



# Ques - 99

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

# rows = 5
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print('')


# Ques -100

## A 
## B B 
## C C C 
## D D D D 
## E E E E E 

# rows = int(input("Enter number of rows: "))

# ascii_value = 65

# for i in range(rows):
#     for j in range(i+1):
#         alphabet = chr(ascii_value)
#         print(alphabet, end=" ")
    
#     ascii_value += 1
#     print("\n")
