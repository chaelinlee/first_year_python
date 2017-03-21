def fastmult(m,n):
    k=0
    while n>0:
        if n%2==0:
          m,n= m+m,n//2
        else:
         k,n=k+m,n-1
         
    return k  
