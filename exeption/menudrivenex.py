while(True):
    try:
        print("!.addition")
        print("2.subtraction")
        print("3.multiplication")
        print('4.division')
        print('5.exit')
    ch=int(input("Enter your choice"))
    n = int(input("Enter number"))
    m = int(input("Enter a number"))
        s=n+m
        d=n-m
        p=n*m
        q=n/m
    except ZeroDivisionError:
        print("Zero Division Error")
    except ValueError:
        print("Value Error")
    except:
        print("Error")
    else:

        if ch==1:
            print("Result",s)
        elif ch==2:
            print("Result",d)

        elif ch==3:
            print("Result",p)

        elif ch==4:
            print("Result",q)

        else:
            exit()


