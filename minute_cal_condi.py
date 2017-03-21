c1,c2= "일을 분으로 따지면", "분입니다."
days= input("며칠? (양수만 입력받습니다)")
if int(days)>0:
    minutes= int(days)* 24 * 60
    print(days, c1, minutes, c2)
else:
    print('양수만 취급한니다.')
