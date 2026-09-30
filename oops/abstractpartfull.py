from abc import ABC ,abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
    def  __init__(self):
         self.name=input("Enter the name:")
         self.age=int(input("Enter the age:"))
         self.empid=int(input("Enter the empid:"))
class fulltime(Employee):
    def __init__(self):
        print("Full time persons details")
        super().__init__()
        self.monthysalary=int(input("Enter the monthly salary:"))
    def calculate_salary(self):
        print("Full time Salary:",self.monthysalary) 
p1=fulltime()
p1.calculate_salary()

class partime(Employee):
    def __init__(self):
        print("Part time persons details")
        super().__init__()
        self.workhour=int(input("Enter the hours:"))
        self.rate=int(input("Enter the rate "))
    def calculate_salary(self):
        print("Total part time salary:",self.workhour*self.rate)    
p2=partime()
p2.calculate_salary()                  
    
