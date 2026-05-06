'''
#Functions:
----------
--> This is a block of code that can be reusable.
--> A function can only run when it is called.
--> def is the keyword used to def the function.
def func_name(parameters):
-------------
-------------
func_name(arguments)
num = 9
def even_odd(num):
    if num % 2 == 0:
        print(f"{num} is even number")
    else:
        print(f"{num} is odd number")
even_odd(num)
even_odd(12)
#o/p-->
9 is odd number
12 is even number

#Required arguments:
-------------------
--> Function must call with no of arguments, that means
function expects 2 arguments, we have to call function with
2 arguments not less or not more.


def sum_num(num1,num2):
    print(num1 - num2)
sum_num(20,10)
#o/p--> 10

#Default Arguments:
------------------
--> By default, value is taken from the calling function.

def name_func(name = "Ram"):
    print(f"hi {name}")
name_func("Charan")
name_func("Raju")
name_func()
#o/p-->
hi Charan
hi Raju
hi Ram

#Keyword Arguments:
-------------------
--> Here, we can send arguments with key = value syntax.
By this, the order of arguments does not matter.

def num_func(num2, num1, num):
    print(num+num1+num2)
num_func(num = 10, num1 = 20, num2 = 30)
#o/p--> 60

#Variable Length Arguments:
-------------------------
--> Adding a star(*) before the parameter name in the function,
recive a tuple of arguments and can be acess items with indexes.

def names(*name):
    print(name[1])
names("Charan", "Prabha", "Tarak", "Bunny")
#o/p--> Prabha
'''




































