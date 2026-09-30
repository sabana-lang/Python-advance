f=open('file2.txt','a+')
print("first pointer position:",f.tell())
f.write("python")
print("After write file pointer position ",f.tell())
f.seek(0)
print("After file pointer position change:",f.tell())
s=f.read()
f.close()

#import os
#os.remove("k.txt")
#print("file is deleated")
#Q1. Write a Python program to open a text file data.txt in a+ mode. Display the initial file pointer position, write "Hello" into the file, display the pointer position after writing, move the pointer to the beginning using seek(0), and display the new pointer position.
f=open('file2.txt','a+')
print("The initial file pointer position:", f.tell())
f.write(" hello")
print("The file pointer position after write:",f.tell())
f.seek(0)
s=f.read()
print(s)
f.close

#Q3. Write a Python program to open test.txt in a+ mode. Write "Welcome" into the file. Use tell() to display the pointer position before and after writing. Then use seek(0) and read the contents.
f=open("passed.txt",'w+')
print("The file pointer position:",f.tell())
f.write(" Welcome")
print("The file pointer position:",f.tell())
f.seek(0)
s=f.read()
print(s)
f.close()

#Q4. Write a Python program to open abc.txt in w+ mode. Write "Computer Science" into the file, move the file pointer to the beginning using seek(0), read and display the contents, and finally close the file.
f=open('file2.txt','w+')
f.write("computer science")
f.seek(0)
print(f.read())
f.close()