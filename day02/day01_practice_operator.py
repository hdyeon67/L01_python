# 커피 구매와 거스름돈 계산 프로그램
# 연산자 연습 목적
money = int(input('현재 잔액을 입력해 주세요 : ')) # 현재 보유 금액

# 코드 입력
price = 2000
# 몫 (//)
count = money // price

# 나머지 (%)
chage = money % price

print(f'구매 가능한 아메리카노 : {count}잔')
print(f"거스름돈 : {chage}원")