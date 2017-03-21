def russian_mult(a,b):
    if not b==1:
        if b%2==0:
            return 0+ russian_mult(a+a,b//2)
        if b%2==1:
            return a+russian_mult(a+a,b//2)
    
    return a
