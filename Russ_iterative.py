def russian_mult(a,b):
    result=0
    if b<1:
        return 0
    while b>0:
        a=a+a
        b=b//2
        if b%2==1:
            result=result+a
       
    return result    
