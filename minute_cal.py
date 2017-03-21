c1,c2= "일을 분으로 따지면", "분입니다."
while True:
    days= input("며칠? (양수만 입력받습니다) ")
    while not days.isdigit():
        days= input("며칠? (양수만 입력받습니다) ")
    if int(days)>0:
        minutes= int(days)* 24 * 60
        print(days, c1, minutes, c2)
    else:
        print('양수만 취급한니다.')
    cont=input("계속하시겠습니까?(예/아니오)")
    while not (cont=='예' or cont=='아니오'):
        cont==input("계속하시겠습니까?(예/아니오)")
    if (cont=='아니오'):
        break
    
    
    
