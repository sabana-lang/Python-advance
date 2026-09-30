#Define a class named employee with attribues empid,name,age,place,salary,designation
#and methods()get salary() and showpersondetails()
#create an employee object and call the methods

class Employee:
    def __init__(self):
        print("Enter employee details")
        self.empid=int(input("Enter the employee id:"))
        self.name=input("Enter the name:")
        self.age=int(input("Enter the age:"))
        self.place=input("Enter the place:")
        self.salary=int(input("Enter the salary:"))
        self.designation=(input("Enter the designation:"))
    def get_salary(self):
        print("Salary :",self.salary) 
    def show(self):
        print("personal details:",self.name,",",self.age,",",self.place)    
emp=Employee()
emp.get_salary()  
emp.show()  
   