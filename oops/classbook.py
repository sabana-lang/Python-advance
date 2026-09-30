class Book:
    def __init__(self):
        print("Enter the book details")
        self.title=input("Enter the title:")
        self.author=input("Enter the author:")
        self.price=int(input("Enter the price:"))
        self.pages=int(input("Enter the pages:"))
        self.language=input("Enter the language:")
    def gettitle(self):
        print("The title of the book is  :",self.title)
    def getauthor(self):
        print(" The author of the book is  :",self.author)
    def getprice(self):
        print(" The price of the book is  ",self.price)            
    def settitle(self):
        self.title=input("Set new title:")
        self.gettitle()   
    def setauthor(self):
            self.author=input("Set new author:")
            self.getauthor()       
    def setprice(self):
            self.price=int(input("Set new price:"))
            self.getprice()
               
b=Book()
b.gettitle()
b.getauthor()
b.getprice()
b.settitle()
b.setauthor()
b.setprice()                    
