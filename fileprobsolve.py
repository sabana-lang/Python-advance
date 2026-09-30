#Write a program to read a text file and display the number of lines in the file.
f=open('passed.txt','r')
s=f.readlines()
print(len(s))
#Write a program to read a text file and display the number of words.
f=open("passed.txt",'r')
s=f.read()
print(len(s.split()))
#Q3
#Write a program to read a file and display the number of characters in it.
f=open("passed.txt",'r')
s=f.read()
count=0
for i in s:
    if i.isalpha():
        count +=1
print(count)
f.close()        
#Q4
#Write a program to display the first 3 lines of a text file.
f=open("passed.txt",'r')
s=f.readlines()
print(s[:3])
#Q5
#Write a program to display the last 3 lines of a text file.
f=open("passed.txt",'r')
s=f.readlines()
print(s[-3:])
#Q6
#Write a program to check whether the word "python" exists in a file.
f=open("passed.txt",'r')
s=f.read()
if "python" in s:
        print ("The word is found")
else:
     print("The word is not found")        
#Q7
#Write a program to check whether a word entered by the user exists in a file.
f=open("passed.txt",'r')
s=f.read()
n=input("Enter the number:")
if n in s:
     print("The word is found")
else:
     print("The word is not found")


#write a program to count the number of digits present in a text file.
#Q9
#Write a program to count the number of alphabets present in a text file.
#Q10
#Write a program to count the number of spaces present in a text file.
f=open("passed.txt",'r')
s=f.read()
count_di=0
count_spa=0
count_alpha=0
for i in s:
     if i.isdigit():
          count_di +=1
     if i.isspace():
          count_spa +=1
     if i.isalpha():
          count_alpha +=1
print("letters:",count_alpha)
print("Spaces:",count_spa)
print("Digit:",count_di)  

#Q12#Write a program to count uppercase and lowercase letters separately.
f=open('passed.txt','r')
s=f.read()
count_upper=0
count_lower=0
for i in s:
     if i.isupper():
          count_upper+=1
     if i.islower():
          count_lower+=1
print("Uppercase:",count_upper)
print("Lowercase:",count_lower)               

#Q13
#Write a program to count the number of:
#- vowels
#- consonants
#- digits
#- spaces
#in a file

f=open('passed.txt','r')
s=f.read()
count_vowel=0
count_consonant=0
count_digits=0
count_spaces=0
vowels=['a','e','i','o','u']
for i in s :
     if i.lower() in vowels:
          count_vowel+=1
     elif i.isalpha():
          count_consonant+=1
     elif i.isdigit():
          count_digits+=1
     elif i.isspace():
          count_spaces+=1
print("Vowels:",count_vowel,"Consonants:",count_consonant,"Digits:",count_digits,"Spaces:",count_spaces)                         
#Q14
#Write a program to display all the lines of a file except the first line.
f=open('passed.txt','r')
s=f.readlines()
print(s[1:])

#Q15
#Write a program to display all the lines of a file except the last line.
f=open('passed.txt','r')
s=f.readlines()
print(s[:-1])

#Q16
#Write a program to display the second line of a file.
f=open('passed.txt','r')
s=f.readlines()
print(s[1])
#Q17
#Write a program to display the second-last line of a file.
f=open('passed.txt','r')
s=f.readlines()
print(s[-2])



#Q18
#Write a program to replace the third line of a file with:
#Python Programming
f=open('passed.txt','r')
s=f.readlines()
s[2]="python programming\n"
print(s[2])
f.close()
f=open('passed.txt','w')
f.writelines(s)
f.close()

#Write a program to replace a line whose number is entered by the user.
f=open('passed.txt','r')
s=f.readlines()
i=int(input("Enter the line:"))
ch=input("Enter the new line word:")
s[i]=ch
print(s[i])
f.close()
f=open('passed.txt','w')
f.writelines(s)
f.close()

f=open("file2.txt",'r')
s=f.read()
print(s.split(),"\n")