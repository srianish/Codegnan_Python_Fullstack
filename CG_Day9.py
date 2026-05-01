'''#elif statement:

marks = int(input("Enter Marks: "))
if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B+")
elif marks >= 60:
    print("B")
elif marks >= 50:
    print("C+")
elif marks >= 40:
    print("C")
else:
    print("FAIL")

Nested if statement:
--> if statement inside another if statement is called
Nested if statement.
Eg:

user_info = {"ATM PIN" : "2005"}
user_pin = input("Enter 4 digits Pin Number: ")
if len(user_pin) == 4:
    if user_pin in user_info["ATM PIN"]:
        print("Welcome!")
    else:
        print("Please enter correct pin")
else:
    print("Please enter 4 digits pin")
#o/p1 -->
Enter 4 digits Pin Number: 20000
Please enter 4 digits pin
#o/p2 -->
Enter 4 digits Pin Number: 2006
Please enter correct pin
#o/p2 -->
Enter 4 digits Pin Number: 2005
Welcome!

For statement:
--> A for statement is used to iterate over items like (string,
list, tuple) with fixed number of itterations
Eg:
any = [10,11,12,13]
count = 0
for j in any:
    print(j)
for j in any:
    count +=1
    print(count)
#o/p-->
10
11
12
13
1
2
3
4

else statement in for:
--> After completing all itterations this else statement will
excute.

any = [23,24,25,26]
for j in any:
    print(j)
else:
    print("Loop finished")
#o/p -->
23
24
25
26
Loop finished

#Palindrome problem without inbuilt:
st = input("Enter string: ")
empty_ = ""
for j in st:
    empty_ = j + empty_
if empty_ == st:
    print("Palindrom")
else:
    print("Not a Palindrom")
#o/p1 -->
Enter string: charan
Not a Palindrom
#o/p -->
Enter string: madam
Palindrom
'''








































