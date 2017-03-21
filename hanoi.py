def tower (n,fro,to,tmp):  #fro는 처음에 있는 막대, to는 옯겨가야할 막대,tmp는 나머지 막대하나  
    if n>1:
        tower (n-1,fro,tmp,to) # n-1개 원판를 fro에서 tmp으로 옯긴다. 
        print ("Move from",fro,"to",to)
        tower(n-1,tmp,to,fro)
    else:
        print("Move from",fro,"to",to)



def tower2(n,fro,to,tmp):
    global counter
    if n> 1:
        tower(n-1,fro,tmp,to)
        print ("Move from",fro,"to",to)
        counter +=1
        tower(n-1,tmp,to,fro)
    else:
        print("Move from",fro,"to",to)
        counter +=1
        
counter = 0
tower2(10,"A","C","B")
print("The number of moves:",counter)
