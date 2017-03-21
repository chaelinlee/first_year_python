def gugudan1():
    for i in range(2,10):
        for j in range(1,10):
            if j % 3 == 0:
                print(i,"x",j,"=",str(i*j).rjust(2))
            else:
               print(i,"x",j,"=",str(i*j).rjust(2),end="  ")
        print()

        
def gugudan2():
    for k in [2,6]: #이건 range(2,7,4)와 동일하다. 2와 6일때 실행한다는 의미 
        for i in range(1,10):
            for j in range(k,k+2): #k=2일때는 한줄에 2,3,4,5까지 하고
                                   #k=6일때는 6,7,8,9까지 한다는 의미   
                print(j,"x",i,"=",str(j*i).rjust(2),end=" ")
            print()
        print()    
