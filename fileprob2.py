#write a program to read a file and print every word on a separate line.
f=open("file2.txt",'r')
s=f.read()
for i in s.split():
    print(i)
#To reverse words
f=open("file2.txt",'r')
s=f.read()
l=s.split()
print((" ".join(l[::-1])))   

#Write a program to reverse each word individually, without changing the order of words.
f=open("file2.txt",'r')
s=f.read()
l=s.split()
for i in l:
  print(i[::-1] ,end=" ") 

#Write a program to find the longest word in a file.  
f=open('file2.txt','r')
s=f.read()
l=s.split()
longest=""
for i in l:
    if len(i)>len(longest):
       longest=i
print("The longest word is:",longest)

f=open('file2.txt','r')
s=f.read()
l=s.split()
shortest=l[0]
for i in l:
    if len(i)<len(shortest):
        shortest=i
print("Shortest:",shortest)        

#Count how many times a particular word occurs
f=open('file2.txt','r')
s=f.read()
l=s.split()
word=input("Enter the word:")
count=0
for i in l:
     if i==word:
         count+=1
print("Occurance:",count) 
        