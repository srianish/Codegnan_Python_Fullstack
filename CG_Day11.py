'''
#Patterns Program
----------------

num =int(input("Enter Number: "))
for j in range(1,num+1):
    for i in range(1,j+1):
        print(i, end = "")
    print()

#reverse triangle:
num =int(input("Enter Number: "))
for j in range(num,0,-1):
    for i in range(1,j+1):
        print(i, end = "")
    print()

num =int(input("Enter Number: "))
for j in range(num,0,-1):
    for i in range(1,j+1):
        print(" ", end = "")
    print()
for k in range(j+1):
    print(j, end = "")

#Pyramid:
num =int(input("Enter Number: "))
for i in range(num):
    for j in range(num-i-1,0,-1):
        print(" ", end = "")
    for k in range(i+1):
        print("* ",end = "")
    print()
'''
#Calculator:
num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
choice = int(input("\n1.Add \n2.Sub \n3.Mul \n4.Div \n5.Que: "))
if choice == 1:
    print(num1 + num2)
elif choice ==2:
    print(num1 - num2)
elif choice == 3:
    print(num1 * num2)
elif choice ==4:
    print(num1 % num2)
elif choice ==5:
    print(num1 // num2)




































