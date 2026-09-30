def file_read():
    filename=(input("Enter the filename:"))
    f=open(filename,'r')
    s=f.read()
    print(s)
    f.close()
def file_write():
    filename=(input("Enter the filename:"))
    f=open(filename,'w')
    s=input("Enter the file content:")
    f.write(s)
    f.close()
def file_append():
    filename=(input("Enter the filename:"))
    f=open(filename,'a')
    s=input("Enter the content you want to append:")
    f.write(s)
    f.close
def file_search():
    filename=input("Enter the filename:")
    f=open(filename,'r')
    s=f.read()
    word=input("Enter the word:") 
    if word in s:
        print("word found")
    else:
        print("word was not found")      
def file_delete():
    import os
    filename=(input("Enter the filename:"))
    os.remove(filename)
    print("file deleted")
while(True):    
    print("1.File read")
    print("2.file write")
    print("3.file append")
    print("4.file search")
    print("5.file delete")
    print("6.break")
    n=int(input("Enter the number:"))
    if n== 1:
        file_read()
    elif n==2:
        file_write()
    elif n==3:
        file_append()
    elif n==4:
        file_search()
    elif n==5:
        file_delete()
    else:    
        break                