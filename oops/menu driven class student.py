class Student:
    def __init__(self):
        self.rollno=int(input("Enter the Roll No:"))
        self.name=input("Enter the name:")
        self.mark=int(input("Enter the mark:"))
    def updatemark(self):
        self.mark=int(input("Please enter the mark to be updated:"))

    def display(self):
        print("Roll No:",self.rollno,"Name:",self.name,"Mark:",self.mark)    
         
    def search(self):
        n=int(input("Please enter the rollno to be searched:"))
        if n==self.rollno:
            print("The rollno is found")  
            
        else:
            print("Rollno not found")
l=[]
while(True):
    print("1.Add student")
    print("2.Update mark")
    print("3.Display all student by roll no")
    print("4.Search student by roll no:")
    print("5.Delete student")    
    print("6.exit")  
    ch=int(input("Enter the choice:"))
    if ch==1:
        s=Student()
        l.append(s)
    if ch==2:
        n=int(input("Enter the rollno:"))
        for i in l:
            if (i.rollno==n ):  
                 i.updatemark()
                 break
            else:
                print("Rollno not found")
    if ch==3:
        n=int(input("Enter the rollno:"))
        for i in l:
                    if (i.rollno==n ):  
                         i.display()
                         break
                    else:
                        print("Rollno not found")
    if ch==4:
         
         for i in l:
                    if (i.rollno==n ):  
                         i.search()
                         break
                    else:
                        print("Rollno not found")
    if ch==5:
         n=int(input("Enter the roll no to be deleted:"))
         if i.rollno==n:
          l.remove(i)   
          print("Roll no deleted")
          
         else:
              ("rollno not found")
    if ch==6:
         exit()                      
                             

