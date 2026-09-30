#Q8. Write a program to open numbers.txt in w+ mode and write "1234567890". Use seek() to move the pointer to position 5, read the remaining contents, and display the pointer position using tell().
#Q9. Write a program to open data.txt in a+ mode. Write "Python\nDjango" into the file. Move the pointer to the beginning and use readlines() to display all the lines.
#Q10. Write a program to check whether k.txt exists using the os.path.exists() function. If it exists, delete it using os.remove(). Otherwise, display "File does not exist".
#Q11. Write a program to open abc.txt in w+ mode, write "Programming", display the pointer position, move the pointer back by using seek(0), read the first 5 characters, and display the final pointer position.
f=open('numbers.txt','w+')
f.write("12345679")
f.seek(5)
s=f.read()
print(s)
print("The file file pointer position:",f.tell())
f.close()
#Q11. Write a program to open abc.txt in w+ mode, write "Programming", display the pointer position, move the pointer back by using seek(0), read the first 5 characters, and display the final pointer position.
f=open("abc.txt",'w+')
f.write("Programming")
print("The file pointer position:",f.tell())
f.seek(0)
s=f.read()
print(s[:5])
print("The file pointer position:",f.tell())
f.close()
#1 4 9 16 25 36
for i in range(1,7):
    print(i**2,end=" ")
#Q2. Print:
#5 10 15 20 25 30
for i in range(1,7):
    print(i*5)
#Q3. Print:
#100 90 80 70 60 50 40
for i in range(100,39,-10):
    print(i,end=" ")
#Q4. Print:
#2 4 8 16 32 64
n=2
for i in range(5):
    n=n*2
    print(n,end=" ")
#Q5. Print:
#🟡 Level 2 — Series with logic
#Q6. Print:
#1 2 6 24 120
for i in range(1,8):
    print(i**2,end=" ")

l=[0, 5, 0, 2, 8, 0, 7]
new=[]
zero=0
for i in l:
      if i !=0:
          new.append(i)
      else:
          zero+=1 
for i in range(zero):
    new.append(0)
print(new)    

L = [1, 2, 2, 3, 4, 3, 5, 1]
new=[]
for i in L:
    if L.count(i)>1 and i not in new:
        new.append(i)
print(new)        


s="pythhonn"
new=[]
for i in s:
     if i not in new:
         new.append(i)
print(new)         

num=191
reverse=0
temp=num
while(num>0):
    digit=num%10
    reverse =reverse*10+digit
    num //= 10
if temp== reverse:
    print("palindrome")   
else:
    print("not palindrome")    

def fact(a):
    for i in  range(1,a+1):
        if a % i==0:
            print(i)
fact(12)                

L = [1, 2, 1, 3, 2, 1, 4, 3, 2]
d={}
for i in L:
     if i  in d:
         d[i] +=1
     else:
         d[i] =1
print(d)         