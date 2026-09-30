class Parent:
    def m1(self):
        print("In parent class method1")
    def m2(self):
        print("In parent class method2")
class child(Parent):
    def m1(self):
         super().m1()
         print("in child class m1")
    def m3(self):
         print("in child class m3")
c=child()
c.m1()
c.m2() 
c.m3()           