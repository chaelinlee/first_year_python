def print_intro():
    print("대출 상환금 계산 서비스에 오심을 환영합니다.")
    

def get_int(message,min_num):
    num=input(message)
    while not(num.isdigit() and int(num)>=min_num):
        num=input(message)
    return int(num)

def print_result(d,p,r,y):
    print("")
    print("대출 상환금 내역을 알려드리겠습니다.")
    print("대출원금:", p, "원")
    print("연 이자율", r*100, "%로", y, "년동안 상환")
    print("1년에 한번씩 상환하시면 매년", d, "원씩 지불하셔야 합니다.")
    print("1달에 한번씩 상환하시면 매월", int(d/12), "원씩 지불하셔야 합니다.")
    print("상환 완료시까지 총 상환금액은", d * y, "원 입니다.")
    return (d,p,r,y)

def isfloat(num):
    part=num.partition(".")
    return ((part[0].isdigit() and part[2].isdigit() and len(part[0]) == len(part[2]) == 1 or \
            part[0].isdigit() and part[2] == "" and len(part[0]) == 1 or \
            part[0] == "" and part[2].isdigit() and len(part[2]) == 1))


def get_interest(message,min_num,max_num):
    num=input(message)
    while not (isfloat(num) and (float(num) >min_num and float(num)<=max_num)):
          num=input(message)
    return float(num)

    
def stop():
    cont= input('계속하시겠습니까? (y/n) ')       
    while not (cont== 'y' or cont== 'n'):
        cont= input('계속하시겠습니까? (y/n) ') 
    return cont== 'n'

def print_outtro():
    print("")
    print("저희 서비스를 이용해주셔서 감사합니다.")
    print("또 들려주세요.")

    
#main function
def loan():
    print_intro()
    while True:
        principal = get_int("대출원금(원)?(1000000 이상)",1000000)
        years = get_int("상환기간(년)? (1 이상)",1)
        interest= get_interest("이자율(%)?",0.1,9.9)/100
        compound=(1 +interest)** years
        d=int(compound* principal* interest/(compound-1))
        print_result(d, principal,interest,years)
        if stop():
            break
    print_outtro()
