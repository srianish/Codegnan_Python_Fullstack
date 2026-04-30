'''
any = int(input("Enter the number: "))
print(type(any))

any_1 = input("Enter the number: ")
print(type(any_1))

a,b = map(int,input("Enter numbers: ").split())
print(a)
print(type(a))
print(b)
print(type(b))

li = list(map(int,input("Enter the List: ").split()))
print(li)
print(type(li))

tup = tuple(map(int,input("Enter numbers: ").split()))
print(tup)
print(type(tup))

A = 10
B = 20
print("Added A and B and result is",A+B)
print(f"Added A and B and result is {A+B}")
print(f"{A} + {B} = {A+B}")

#eval:
a = eval(input("Enter: "))
print(a)
print(type(a))
b = eval(input("Enter: "))
print(b)
print(type(b))
#o/p:
Enter: 12
12
<class 'int'>
Enter: [1,2,3]
[1, 2, 3]
<class 'list'>

statements
----------
1. if statement
--> This is used to check condition is true or not
Eg:
num = 10
if num == 10:
    print(f"num is equal to 10")

2. else statement
--> 
Eg:
num = 10
if num > 9:
    print(f"num is greater 9")
else:
    print(f"num is not greater than 9")
    

a, b = map(int,input("Enter the numbers: ").split())
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")

age = int(input("Enter age: "))
if age >= 18:
    print("You are eligible to vote")
else:
    print(f"You have to wait for {18 - age} years to vote")
'''

marks = int(input("Enter marks: "))
if marks >= 35:
    print("PASS")
else:
    print("FAIL")
















