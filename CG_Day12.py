'''
li = eval(input("Enter List: "))
empt = []
for i in li:
    if i not in empt:
        empt.append(i)
print(empt)

li = eval(input("Enter List: "))
max1 = 0
max2 = 0
for i in li:
    if i > max1:
        max2 = max1
        max1 = i
print(max2)
'''
























