
class Person:
    def __init__(self):
        self.name=input("Enter name:")
        self.age=int(input("Enter age:"))
    def show(self):
        print("Name:",self.name,"Age:",self.age)    
class Student(Person):
    def __init__(self):
        super().__init__()
        self.rollno=int(input("Enter the rollno:"))
        self.course=(input("Enter the course:"))
        self.mark=int(input("enter the mark:"))
    def show(self):
        super().show()
        print("roll no:",self.rollno,"course:",self.course,"mark:",self.mark)
    def update(self):
        self.mark=int(input("enter the mark to be updated:"))
                   
s=Student()        
s.show()
s.update()