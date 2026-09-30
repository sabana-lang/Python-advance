class account:
   def __init__(self):
       self.accname=input("Enter the name:")
       self.accnumber=int(input("Enter the number:"))
       self.accbalance=int(input("Enter the account balance:"))
      
   def showbalance(self):
       print("The current balance is:",self.accbalance)  

   def withdraw (self):
       amount=int(input("Enter the withdrwal amount:")) 
       if (amount>self.accbalance):
            print("Insufficient fund")
       else:
            self.accbalance=self.accbalance-amount     
            self.showbalance()
   def deposit(self):
        dep=int(input("Enter the amount you want to deposit:"))
        self.accbalance=self.accbalance+dep
        self.showbalance()        

l=[]   
while(True):    
 print("1.create a new account:")
 print("2.withdraw")
 print("3.deposit")
 print("4.showbalance")
 print("5.exit")
 ch=int(input("Enter the choice:"))
 if ch ==1:
    a=account()
    l.append(a)
 if ch==2:
    for i in l:
        ac=int(input("Enter the ac no:"))
        if i.accnumber==ac:
            i.withdraw()
            break
        else:
            print("Account not found")    
 if ch==3:
    for i in l:
        ac=int(input("Enter the ac no:"))
        if i.accnumber==ac:
            i.deposit()
            break
        else:
            print("Account not found")    
 if ch==4:
    for i in l:
        ac=int(input("Enter the ac no:"))
        if i.accnumber==ac:
            i.showbalance()
            break
        else:
            print("Account  not found")    
 if ch==5: 
    break              
