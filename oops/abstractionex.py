from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def get_area(self):
        pass
    def get_perimeter(self):
        pass
class Rectangle(shape):
    def __init__(self):
      self.length=int(input("Enter the length:"))
      self.breadth=int(input("Enter the breadth:"))
    def get_area(self):
        print("Area:",self.length*self.breadth)
    def get_perimeter(self):
        print("Perimeter:",2*(self.length+self.breadth))
r=Rectangle()                  
r.get_area()
r.get_perimeter()
class Square(shape):
    def __init__(self):
        self.side=int(input("Enter the side:"))
    def get_area(self):
        print("Area:",self.side*self.side) 
    def get_perimeter(self):
        print("Perimeter:",4*(self.side))
s=Square()
s.get_area()
s.get_perimeter()               