class Student:
    def __init__(self):
        print("Give the student details")
        sum=0
        self.rollno=int(input("Enter the roll number:"))
        self.name=input("Enter the name: ")
        self.mark1=int(input("Enter the first mark:"))
        self.mark2=int(input("Enter the second mark:"))
        self.mark3=int(input("Enter the third mark:"))
        self.sum=self.mark1+self.mark2+self.mark3
    def display(self):
        print("Roll No:",self.rollno)
        print("Total marks of the student:",self.sum)  
s1=Student()
s1.display()
s2=Student()
s2.display()
