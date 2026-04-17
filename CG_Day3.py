'''
Operatores
----------
1.Arthmetic Operator
2.Assignment Operator
3.Comparision Operator
4.Logical Operator
5.Identity Operator
6.Memberships Operator
7.Bitwise Operator
---------------------------------------------------
1.Arthmetic Operator : +, -, % , *, **
Num1 = 20
Num2 = 30
Num3 = 40
print(Num1 + Num2 + Num3)    #o/p-> 90

num1 = 20
num2 = 10
print(num1 - num2)    #o/p-> 10

Dig1 = 5
Dig2 = 4
print(Dig1 % Dig2)     #o/p-> 1

dig1 = 4
dig2 = 5
print(dig1 * dig2)    #o/p-> 20

a = 3
b = 2
print(a ** b)    #o/p-> 9

Num_1 = 10.45
Num_2 = 2.0
print(Num_1 // Num_2)     #o/p-> 5.0 Note : Used to round off the value
----------------------------------------------------
2.Assignment Operator : =, +=, -=, *=, **=, //= 
num_1 = 185
num_1 += 1     #num_1 = num_1+1
print(num_1)    #o/p->186

num_1 = 185
num_1 -= 1     #num_1 = num_1-1
print(num_1)    #o/p-> 184

num_1 = 5
num_1 *= 8     #num_1 = num_1*8
print(num_1)   #o/p-> 40

num_1 = 5
num_1 **= 2     #num_1 = num_1**2
print(num_1)   #o/p-> 25

num_1 = 20
num_1 //= 2     #num_1 = num_1//2
print(num_1)   #o/p-> 10

3.Comparision Operator : ==, >, >=, <, <=
a1 = 10
a2 = 10
print(a1 == a2)    #o/p-> True

a1 = 10
a2 = 10
print(a1 != a2)    #o/p-> False

a1 = 10
a2 = 5
print(a1 >= a2)    #o/p-> True

a1 = 10
a2 = 5
print(a1 <= a2)    #o/p-> False
----------------------------------------------------
4.Logical Operator : and, or,
1)and -> 2 conditons should be true
L1 = 7
L2 = 40
print(L1 < 10 and L2 > 50)     #o/p-> False

2)or -> any one condition could be true
L_1 = 7
L_2 = 40
print(L_1 < 10 or L_2 > 50)     #o/p-> True

3)not -> reverse the result
L1 = 7
L2 = 40
print(not(L1 < 10 and L2 > 50))     #o/p-> True
-----------------------------------------------------
5.Identity Operator : is, is not
1)is -> this operator is used to check object(memory location)
Id = 10
Id = 10
print(Id is Id)     #o/p-> True

list_ = [1,2]
list_2 = [1,2]
list_3 = list_
print(list_ is list_2)      #o/p-> False
print(list_ == list_2)   #o/p-> True
print(id(list_))
print(id(list_2))
print(id(list_3))

2)is not -> to check wheather the object is not same
list_ = [1,2]
list_2 = [1,2]
list_3 = list_
print(list_ is not list_2)     #o/p-> True
----------------------------------------------------
6.Memberships Operator : in, not in
list_M = [1,2]
print(2 in list_M)      #o/p-> True

list_M = [1,2]
print(2 not in list_M)      #o/p-> False
----------------------------------------------------
7.Bitwise Operator : &, |, ^, ~, <<, >>
1)& -> Bitwise AND
5-> 0101
3-> 0011
---------
1-> 0001
print(5 & 3)     #o/p-> 1

2)| -> Bitwise OR
5-> 0101
3-> 0011
---------
7-> 0111
print(5 | 3)     #o/p-> 7

3)^ -> Bitwise XOR
5-> 0101
3-> 0011
---------
6-> 0110
print(5 ^ 3)     #o/p-> 6

4)<< --> Left shift
print(5 << 3)     #o/p-> 40

5)>> --> Right Shift
print(5 >> 3)     #o/p-> 0'''




















































































