# 대출 상환금 계산 서비스
# 대출금 상환금액을 계산해주는 프로그램
#
# 입력: 원금(principal) - 백만이상 정수만 허용
#      상환기간(years) - 1이상 정수만 허용
#      연이자율(interest rate) - 0.1~9.9 범위의 정수 또는 부동소수점수 만 허용
# 출력: 연상환금, 월상환금, 상환금 총액
#
# 작성자: 이채린
# 작성날짜: 2015년 3월 24일 (version 1.0)

print("대출 상환금 계산 서비스에 오심을 환영합니다.")

# 입력
p= input("대출원금이 얼마인가요?(백만이상) ")
while not(p.isdigit() and int(p) >= 1000000):
     p= input("대출원금이 얼마인가요?(백만이상) ")
     
y=input("상황기간은 몇년인가요? (1년이상 연단위) ")
while not (y.isdigit() and int(y)>= 1):
     y=input("상황기간은 몇년인가요? (1년이상 연단위) ")

r=input("이자율은 몇 %인가요? (0.0~9.9) ")
(f,m,b)= r.partition(".")
while not ((f.isdigit() and b.isdigit() or f.isdigit() and b=="" or f=="" and b.isdigit() or r.isdigit()) and len(b)<=1 and 0.0< float(r)<=9.9):
     r=input("이자율은 몇 %인가요? (0.0~9.9) ")
     (f,m,b)=r.partition(".")
r=float(r)/100

# 상환금 계산
print("\n대출 상환금 내역을 알려드리겠습니다.")
print("대출원금:"+str(p)+"원")
d=(1+float(r))**int(y)*int(p)*float(r)/((1+float(r))**int(y)-1)
print("연 이자율"+str(r*100)+"%로"+str(y)+"년동안 상환")
print('1년동안 한번씩 상환하시면 매년',int(d),'원씩 지불하셔야 합니다.')
print('1달에 한번씩 상환하시면',int(d/12),'원씩 지불하셔야 합니다.')
print('상환 완료시까지 총 상환금액은',int(d)*int(y),'원 입니다.\n')


# 출력
print("저희 서비스를 이용해주셔서 감사합니다.")
print("또 들려주세요.")
