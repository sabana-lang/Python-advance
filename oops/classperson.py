#sample code of oops
class Person:
    def __init__(self,n,a):# __init__ used to create and initialize
                           # object attributes and properties
        self.name=n
        self.age=a
    def show(self):# represent current object
        print(self.name,",",self.age)
n1=input("Enter the name:")
a1=int(input("Enter the age:")) 
n2=input("Enter the name:")
a2=int(input("Enter the age:")) 
p1=Person(n1,a1)#creates object of class person
p2=Person(n2,a2)# it will call __init__ automatically
p1.show()
p2.show()            