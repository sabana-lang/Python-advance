try:
 n=int(input("Enter the number:"))
 if n<=0:
   raise ValueError("Number should be positive")
 else:
   print(n)
except ValueError as e:
   print(e)   