try:
    num1=int(input("Enter the number:"))
    num2=int(input("Enter the number:"))
    r=num1/num2
    print("Result:",r)
except ZeroDivisionError:
       print("zero division error")
except ValueError:
      print("Value type error")
#exept:
      print("error")
