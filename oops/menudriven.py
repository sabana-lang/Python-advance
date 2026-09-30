#Create a class Product.
#Attributes:
#- Product ID
#- Product name
#- Price
#- Quantity
#Menu:
#1. Add product
#2. Update quantity
#3. Display all products
#4. Search product
#5. Remove product
#6. Calculate total amount
#7. Exit

class product:
    def __init__(self):
        self.productid=int(input("Enter the product id:"))
        self.productname=input("Enter the product name:")
        self.price=int(input("Enter the price :"))
        self.quantity=int(input("Enter the quantity"))
    def update_quantity(self):
        self.quantity=int(input("Enter the quantity to be updated"))
    def search_product(self):
         n=input("Enter the product u want to search:")
         if n==self.productname:
             print("Product name is found")
         else:
             print("Product name is not found")
    def calculate_amount(self):
        print("Amount =",self.price*self.quantity) 
l=[]        
while(True):
    print("1. Add product")
    print("2. Update quantity")
    print("3.Display all products")
    print("4.Search product")
    print("5.Remove product")
    print("6.Calculate total amount")
    print("7.Exit")                            
    ch=int(input("Enter the choice:"))
    if ch==1:
        p=product()
        l.append(p)
    if ch==2:
        n=input("Enter the product name:")
        for i in l:
            if i.productname==n:
                i.update_quantity()
                break
        else:
                print("Product name doesnt match")
    if ch==3:
            for i in l:
                print(i.productname)
    if ch==4:
            n=input("Enter the product name to be searched:")
            for i in l:
                if i.productname==n:
                    i.search_product()
                    break
            else:
                    print("Product not found")
    if ch==5:
                n=input("Enter the product  to be deleated :")
                for i in l:
                    if i.productname==n:
                        l.remove(i)
    if ch==6:
                n=input("Enter the product to be calculate:")
                for i in l:
                     if i.productname==n:
                          i.calculate_amount() 
                          break
                else:
                          print("Product name doesnt match") 
    if ch==7:
             exit()                                        
                        
                                                        
                    

                                                    

                

