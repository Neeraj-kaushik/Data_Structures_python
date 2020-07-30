class Student():
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def display(self,name,rollno):
        print(self.name)
        print(self.rollno)
    def setage(self,age):
        self.age=age
    def setmarks(self,marks):
        self.marks=marks

name=str(input("enter the name "))
rollno=int(input("enter the roll no"))
age =int(input("enter the age"))
marks=int(input("enter the marks"))
s1=Student(name,rollno)
s1.display(name,rollno)
s1.setage(age)
s1.setmarks(marks)