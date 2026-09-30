f1=open('total.txt','r')
f2=open('passed.txt','r')
s=f1.readlines()
c=f2.readlines()
for name in s:
     if name not in c:
          print(name)