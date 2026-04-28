'''
Tuple
------
--> Tuple is a collection of different data types that
represent by () and the items in the tuple is sperated by comma.
--> And tuple is immutable

any = [1,"Python",2,[10,11],(20,30)]
print(any)
print(any[2])

any1 = (1,2,3,4)
any2 = (10,11,12)
print(any1 + any2)                           #(1, 2, 3, 4, 10, 11, 12)

Dictionary
---------
--> Dict is a collection of key : a  value pair, where keys are
immutable(string, int and tuple) and values or any data type
and this is represented by {}
Methods
-------
1.keys()
-----
--> This method is used to access only keys in the dict.
Syntax: dict.keys()
Eg:
my = {"Name" : "Ram",
      "Age" : 40,
      "Edu" : "B.Tech"
    }
print(my.keys())                  #dict_keys(['Name', 'Age', 'Edu'])

3.values()
-------
--> This method is used to access only values in the dict.
Syntax: dict.values()
Eg:
my = {"Name" : "Ram",
      "Age" : 40,
      "Edu" : "B.Tech"
    }
print(my.values())             #dict_values(['Ram', 40, 'B.Tech'])

4.items()
------
--> This method is used to access key : value pair in the dict
Syntax: dict.items()
Eg:
my = {"Name" : "Ram",
      "Age" : 40,
      "Edu" : "B.Tech"
    }
print(my.items()) #dict_items([('Name', 'Ram'), ('Age', 40), ('Edu', 'B.Tech')])

5.clear()
-------
--> This clear() method is used to delete all the items in the dict
Syntax: dict.clear()
Eg:
my = {"Name" : "Ram",
      "Age" : 40,
      "Edu" : "B.Tech"
    }
print(my.clear())                                                         #None

update()
---------
--> This method is used to add new item(key : value) into
the dict
Syntax: dict.update({key : value})
Eg:
my = {"Name" : "Ram",
      "Age" : 40,
      "Edu" : "B.Tech"
    }
my.update({"Role" : "Python Dev"})
print(my)
#o/p--> {'Name': 'Ram', 'Age': 40, 'Edu': 'B.Tech', 'Role': 'Python Dev'}
'''


















