'''
#List:
-----
--> List is a collecion of different data types
and it is represented by [] separated by comma.

any = [186,"Ram",[1,2]]
print(any)                                  #o/p--> [186, 'Ram', [1, 2]]

any = [1,"Python",[2,"Ram Charan",186],4]
print(any[2])                                    #[2, 'Ram Charan', 186]
print(any[2][1])                                                #Ram Charan
print(any[2][1][5])                                                            #h

any = [1,"Python",2,3,[32,["This is python class"],78,"Iam looking"]]
print(any[4][1][0][11])                                         #o/p--> h

#immutable:
------------
im = "Global Star Ram Charan"
print(im.replace("Global", "Mega"))     #Mega Star Ram Charan
print(im)                               #Global Star Ram Charan

#mutable:
---------
li = [1,2,3,4]
li.append(10)
print(li)                                                        #[1, 2, 3, 4, 10]

#Methods:
---------
1. append() #syntax: var_name.append()
----------
--> This  method is used to add  new item into list,
it will go and add directly to the last index position.
Eg:
ad = [1,2,3,4]
ad.append(10)
print(ad)                                                       #[1, 2, 3, 4, 10]
ad.append([0,1,2])
print(ad)                                        #[1, 2, 3, 4, 10, [0, 1, 2]]

2. extend() #syntax: var_name.extend()
----------
--> This method is aslo used to add new item into the list,
but this extend add as each position to each index in the list.
Eg:
ex = [1,2]
ex.append(10)
ex.extend([5,6])
print(ex)                                                       #[1, 2, 10, 5, 6]

3. pop() #syntax: var_name.pop()
-------
--> This is used to delete an item from the list,
this pop() removes the value based on the index position mentioned in the parameters.
--> If nothing is mentioned it will remove last index postion value.
Eg:
po = [1,2,3,7]
po.pop(7)              #IndexError: pop index out of range.
po.pop(2)
print(po)                                                                   #[1,2,7]

4. remove() #syntax: var_name.remove()
----------
-->

Eg:
rem = [1,2,3,4]
rem.remove(4)
print(rem)                                                               #[1, 2, 3]

5.slicing() #syntax: var_name[starting index : ending index]
---------
-->

Eg:
slic = [6,7,8,9,10,11,12,13]
print(slic[2:5])                                                  #[8,9,10]

6.len() #syntax: len(var_name)
------
-->

Eg:
any1= "Ram Charan"
any2 = [1,2,3,4,5]
print(len(any1))
print(len(any2))
'''












































