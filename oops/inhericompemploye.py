class company:
    def __init__(self):
        self.companyname=input("Enter the company name:")
        self.location=input("Enter the location:")
    def  display_company(self):
        print("The name of the company:",self.companyname,"Location:",self.location)
class Employee(company):
      def __init__(self):
           super().__init__()
           self.empid=int(input("Enter the employee id:"))
           self.name=input("Enter the name:")
           self.designation=(input("Enter the designation:")) 
           self.salary=int(input("Enter the salary:"))
      def display_details(self):
           super().display_company()
           print("Employee id:",self.empid,"Name:",self.name,"Designation:",self.designation,"Salary:",self.salary)      
      def update_salary(self):
           self.salary=(self.salary*1.1)
           print("Updated salary is:",self.salary)
e=Employee()
e.display_details()
e.update_salary()