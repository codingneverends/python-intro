#Hello World
#-------------------------------------------------------------------------------------------------------------------#
'''
print("Hello World")
'''
#-------------------------------------------------------------------------------------------------------------------#

#Read and Write
#-------------------------------------------------------------------------------------------------------------------#
''''
a = input("Enter Something : ")
print(a)
'''
#-------------------------------------------------------------------------------------------------------------------#

#Arithmetic hadling - lvl 0 -- raw
#-------------------------------------------------------------------------------------------------------------------#
'''
print(4+5)
'''
#-------------------------------------------------------------------------------------------------------------------#

#Arithmetic hadling - lvl 0 -- string
#-------------------------------------------------------------------------------------------------------------------#
'''
a = input("Enter Some number1 : ")
b = input("Enter Some number2 : ")
print(a+b)
'''
#-------------------------------------------------------------------------------------------------------------------#

#Determining type
#-------------------------------------------------------------------------------------------------------------------#
'''
a = input("Enter Some number1 : ")
print(type(a))
'''
#-------------------------------------------------------------------------------------------------------------------#

#Arithmetic hadling - lvl 1 -- int
#-------------------------------------------------------------------------------------------------------------------#
'''
a = int(input("Enter Some number1 : "))
b = int(input("Enter Some number2 : "))
print(a+b)
'''
#-------------------------------------------------------------------------------------------------------------------#

#Arithmetic hadling - lvl 2 -- float
#-------------------------------------------------------------------------------------------------------------------#
'''
a = float(input("Enter Some number1 : "))
b = float(input("Enter Some number2 : "))
print(a+b)
'''
#-------------------------------------------------------------------------------------------------------------------#

#Arithmetic hadling - lvl 2 -- float
#-------------------------------------------------------------------------------------------------------------------#
'''
a = int(input("Enter Some number1 : "))
b = float(input("Enter Some number2 : "))
print(a+b)
print(type(a),type(b))
'''
#-------------------------------------------------------------------------------------------------------------------#

#True and False
#-------------------------------------------------------------------------------------------------------------------#
'''
print(3>10)
print(3<10)
print(True)
'''
#-------------------------------------------------------------------------------------------------------------------#

#If
#-------------------------------------------------------------------------------------------------------------------#
'''
mark = float(input("Enter mark : "))
if mark >= 20:
    print("pass")
if mark < 20:
    print("fail")
'''
#-------------------------------------------------------------------------------------------------------------------#

#If Else
#-------------------------------------------------------------------------------------------------------------------#
'''
mark = float(input("Enter mark : "))
if mark >= 20:
    print("pass")
else:
    print("fail")
'''
#-------------------------------------------------------------------------------------------------------------------#

#List Handling - intro
#-------------------------------------------------------------------------------------------------------------------#
'''
marks = [10,20,30,40,50]
print(marks)
'''
#-------------------------------------------------------------------------------------------------------------------#

#List Handling - adding entry
#-------------------------------------------------------------------------------------------------------------------#
'''
marks = [10,20,30,40,50]
marks.append(60)
marks.append(70)
print(marks)
'''
#-------------------------------------------------------------------------------------------------------------------#

#List Handling - Acessing Specific entry
#-------------------------------------------------------------------------------------------------------------------#
'''
marks = [10,20,30,40,50]
print(marks[0])
print(marks[4])
'''
#-------------------------------------------------------------------------------------------------------------------#


#List Handling - Acessing Specific entry
#-------------------------------------------------------------------------------------------------------------------#
'''
marks = [10,20,30,40,50]
print(marks)
marks[0]=50
marks[1]=30
marks[4]=60
print(marks)
'''
#-------------------------------------------------------------------------------------------------------------------#

#For
#-------------------------------------------------------------------------------------------------------------------#
'''
for i in range(10):
    print(i+1)
'''
#-------------------------------------------------------------------------------------------------------------------#

#For Loop and Lists
#-------------------------------------------------------------------------------------------------------------------#
'''
marks = [10,20,30,40,50]
for i in marks:
    print(i)
'''
#-------------------------------------------------------------------------------------------------------------------#

#List Sum -- For
#-------------------------------------------------------------------------------------------------------------------#
'''
sumofmarks = 0
marks = [10,20,30,40,50]
for mark in marks:
    sumofmarks = sumofmarks + mark
print(sumofmarks)
'''
#-------------------------------------------------------------------------------------------------------------------#

#List Sum -- inbuilt function
#-------------------------------------------------------------------------------------------------------------------#
'''
marks = [10,20,30,40,50]
sumofmarks = sum(marks)
print(sumofmarks)
'''
#-------------------------------------------------------------------------------------------------------------------#

#List Length
#-------------------------------------------------------------------------------------------------------------------#
'''
marks = [10,20,30,40,50]
lengthofmarks = len(marks)
print(lengthofmarks)
'''
#-------------------------------------------------------------------------------------------------------------------#

#List Average -- For
#-------------------------------------------------------------------------------------------------------------------#
'''
marks = [10,20,30,40,50]
sumofmarks = 0
for mark in marks:
    sumofmarks = sumofmarks + mark
#sumofmarks = sum(marks)
lengthofmarks = len(marks)
average = sumofmarks/lengthofmarks
print(average)
'''
#-------------------------------------------------------------------------------------------------------------------#

#While
#-------------------------------------------------------------------------------------------------------------------#
'''
i = 0
while i < 10:
    print(i+1)
    i = i+1
'''
#-------------------------------------------------------------------------------------------------------------------#


#List Sum -- While
#-------------------------------------------------------------------------------------------------------------------#
'''
sumofmarks = 0
marks = [10,20,30,40,50]
marklen = len(marks)
mark_index = 0
while mark_index < marklen:
    sumofmarks = sumofmarks + marks[mark_index]
    mark_index = mark_index + 1
print(sumofmarks)
'''
#-------------------------------------------------------------------------------------------------------------------#


#Custom function
#-------------------------------------------------------------------------------------------------------------------#
'''
def SUM(_list):
    _sum = 0
    for _entry in _list:
        _sum = _sum + _entry
    return _sum
marks = [10,20,30,40,50]
print(sum(marks))
print(SUM(marks))
'''
#-------------------------------------------------------------------------------------------------------------------#

#Classes
#-------------------------------------------------------------------------------------------------------------------#
''''''
class Person:
    def __init__(self,age,name):
        self.age = age
        self.name = name
    def saysomething(self,anothername):
        print("Hii , I am "+self.name+". Nice to meet you "+anothername)

person = Person(20,"Ram")
person.saysomething("Raju")
''''''
#-------------------------------------------------------------------------------------------------------------------#
