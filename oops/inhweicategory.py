class category:
    def __init__(self):
        self.category_name=input("Enter a category: ")
    def show_category(self):
        print("The category is:",self.category_name) 
class product(category):
    def __init__(self):
        super().__init__()
        self.product_name=input("Enter the product name:")
        self.price=int(input("Enter the price:"))
        self.quantity=int(input("Enter the quantity:"))
    def total_price(self):
            print("The total price is",self.quantity*self.price)
p=product()
p.total_price()
p.show_category()
      