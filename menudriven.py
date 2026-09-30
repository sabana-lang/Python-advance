def add():
   n1=int(input("Enter the number:"))
   n2=int(input("Enter the number:"))
   s=n1+n2
   print("Sum",s)
def sub():
    n1=int(input("Enter the number:"))
    n2=int(input("Enter the number:"))
    s=n1-n2
    print("Difference",s)
def mul():
      n1=int(input("Enter the number:"))
      n2=int(input("Enter the number:")) 
      s=n1*n2
      print("multiplication",s)
def div():
         n1=int(input("Enter the number:"))
         n2=int(input("Enter the number:")) 
         s=n1/n2
         print("division",s)
while(True):
     print("1.add")
     print("2.sub")
     print("3.mul")
     print("4.div")
     print("5.break")
     num=int(input("Enter the choice:"))
     if num==1:
       add()
     elif num==2:
       sub()
     elif num==3:
       mul()
     elif num==4:
       div()
     else:
        break       
