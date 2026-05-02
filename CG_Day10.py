'''
#while statement
---------------
--> This while statement will keep on excuting untill unless
condition.

num = 1
while num<=5:
    print(num)
    num += 1

range()
------
--> This range() will generate sequence numbers upto the limit.
syntax--> range(starting, ending, step)

choose = int(input("Enter the limit: "))
for j in range(1, choose+1):
    print(j)

for i in range(2,11):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

control statements:
-----------------
1) break
-------
--> This break statement will exit if the condition becomes true.
and never enters intlo next loops.
Eg:
any = ["NTR", "Prabhas", "Ram", "pawan"]
for i in any:
    if i == "Ram":
        print(i)
        break
#o/p-->
Ram

2) continue
----------
Eg:
any = ["NTR", "Prabhas", "Ram", "Pawan"]
for i in any:
    if i == "Ram":
        continue
    print(i)
#o/p-->
NTR
Prabhas
Pawan

3) pass
------
--> Pass is a place holder, holds the space not to get any
syntax error.

Eg:
a = 9
b = 90
if a >= b:
    pass


#Prime problem
num = int(input("Enter Number: "))
cou = 0
for i in range(1,num+1):
    if num % i == 0:
        cou += 1
if cou == 2:
    print(f"{num} is Prime")
else:
    print(f"{num} is not prime")

Nested loop:

'''
for i in range(2,11):
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(f"{j} is prime")
    else:
        print(f"{j} is not prime")


























































