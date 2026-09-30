import math
while(True):
 try:
    n=int(input("Enter the number:"))
    print(math.factorial(n))
    break
 except ValueError as e:
     print(e)
     print(type(e))

try:
    f=open('c.txt','r')
    print(f.read())
    f.close()
except FileNotFoundError:
    print("File does not exist")

try:
    d={"name":"arun","age":23,"place":"ekm"}           
    n=input("Enter a key:")
    print("Value:",d[n])
except KeyError as f:
     print(f)
     print(type(f))
