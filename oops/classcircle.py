class Circle:
    def __init__(self):
        self.radius=int(input("Enter the number:"))
    def getarea(self):
        
        print("Area of the circle is:",3.14*(self.radius)**2)
    def getperimeter(self):
        print("The perimeter of the circle is :",2*3.14*self.radius)
c=Circle()
c.getarea()
c.getperimeter()            
