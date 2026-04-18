'''
mutable data type
----------------
--> I can modify directly on the variable, which the data type have taken
eg--> list, dict(dictnory)
----------------------------------------------------------------
immutable
---------
--> Where can be modifed directly on the variable assign to the data type
eg--> int, string

1)integer or in --> Storing number or digit in the variable is called int
num_1 = 10

2)float --> Storing decimal value in the variable is called float
num_2 = 1=9.05 

3)string or str --> String is a collection of char that are inclosed in ' ', " ", ''' '''
                      --> It is immutable data type

4)indexing
----------
--> This is used to get  a particular substring, item from string, list and tuple by calling with index position
syntax :
variable_name[index_position]

5)concatenation
--------------
--> A + symbol acts as different way, if we are adding 2 integers it acts like addition
in other cases such as list, string and tuple it acts like concateation
eg :
num_1 = 185
num_2 = 1
print(num_1 + num_2)

name_1 = "Mega PowerStar"
name_2 = " RAM CHARAN"
print(name_1 + name_2)

--------------------------------------------------------------------
string methods
-------------
1)replace()
--> Used to replace or change old sub string with a new string

syntax :
variable_name.replace("old string" , "new string")
eg :
any = ("Peddi worldwide release on April30")
print(any.replace("April30" , "June4"))     #o/p--> Peddi worldwide release on June4

2)split()
--> This method used to separate the string using a substring and it will split into
list such as before the substring is one index and after the substring is another index.

syntax:
variable_name.split("substring")

3)strip()
--> This method is used to remove from 1st index position or from last

4)join()
syntax :
"substring".join(variable_name)


5)lower()
syntax :
variable_name.lower()

6)upper()
variable_name.upper()

7)capitalize()'''

num = int(input("enter a number: "))
print(f"{num} is a number")



















































