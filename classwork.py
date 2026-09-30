#write a program to read a text file and displays the number of lines in a file
f=open('k.txt','r')
s=f.readlines()
print(len(s))

#write a program to display the number of words in a file
f=open('k.txt','r')
s=f.read()
c=s.split()
print(len(c))

#write a program to update the second line in a file 
f=open('k.txt','r')
s=f.readlines()
s[1]="class\n"
print(s[1])
f.close()
f=open('k.txt','w')
f.writelines(s)
f.close()

#write a program to display last 5 lines in a file
f=open('k.txt','r')
s=f.readlines()
print(s[-5:])

f=open('k.txt','r')
s=f.read()
if ("class") in s:
             print("The word is found in the sting")
else        :
             print("The word was not found in the string")

f=open('k.txt','r')
s=f.read()
count_isdigit=0
count_isalpha=0
count_isspace=0
for i in s:
           if i.isdigit():
               count_isdigit +=1
           elif i.isalpha():
               count_isalpha +=1
           elif i.isspace():
               count_isspace += 1
print("letters:",count_isalpha)
print("digits:",count_isdigit)
print("spaces:",count_isspace)                   
f.close() 

f=open('k.txt','r')
s=f.read()
print(" ".join(s.split()[::-1]))
f.close()