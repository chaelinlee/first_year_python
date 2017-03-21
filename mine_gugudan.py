def gugudan1():
    for a in range(2,10):
        for b in range(1,10):
            if b%3==1:
                print(a,"x",b,"=",str(a*b).rjust(2),end='  ')
            elif b%3==2:
                print(a,"x",b,"=",str(a*b).rjust(2),end='  ')
            elif b%3==0:
                print(a,"x",b,"=",str(a*b).rjust(2))
        print("")

def gugudan2():
    for c in range(0,2):
        for b in range(1,10):
            if c==0:
                for a in range(2,6):
                    print(a,"x",b,"=",str(a*b).rjust(2)," ",end=" ")
            else:        
                for a in range(6,10):
                    print(a,"x",b,"=",str(a*b).rjust(2)," ",end=" ")
            print("")
        print("")     
