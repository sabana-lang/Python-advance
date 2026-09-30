#31. Write a program to count the frequency of each word in a text file.
f=open('file2.txt','r')
s=f.read()
l=s.split()
d={}
count=0
for i in l:
     if i not in d:
        d[i]=1
     else:
         d[i]+=1
print(d)            

# 31 Write a program to display all duplicate words in a text file.
f=open('file2.txt','r')
s=f.read()
l=s.split()
seen=[]
dup=[]
for i in l:
     if i in seen:
         if i  not in dup:
            dup.append(i)
     else:       
           seen.append(i)
print(dup)           

f=open('file2.txt','r')
s=f.read()
l=s.split()
d={}

for i in l:
     if i not in d:
        d[i]=1  
     else:
         d[i]+=1
for i in d:
    if d[i]==1:
       print(i)   
f.close()       

#40. Write a program to count and display the number of lines, words, and characters in a text file.       
f=open('file2.txt','r')
s=f.read()
print(len(s))
l=s.split()
print(len(l))      

      