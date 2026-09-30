f=open('k.txt','w') #if file exists it will erase the file contents
#and its reference to f
#else it will create a new empty file and  return its reference to f

# write(string)
f.write("hello\n")
f.write("python\n")
f.write(""" At its core, coding acts as a bridge between human logic and machine action.
 Just like a recipe guides a cook through a sequence of steps, a piece of code tells a computer how to process data, display websites, or run mobile applications.
   Popular languages like Python and JavaScript allow developers to build everything from simple games to complex artificial intelligence systems.\n""")
f.writelines(['hello\n','world\n','hi\n','python'])
f.close()