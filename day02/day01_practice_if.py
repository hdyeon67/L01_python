# 버스 요금 계산 프로그램
# 조건문 연습문제

age = int(input('나이를 입력해 주세요 : '))
card_type = input('결제 수단을 입력해 주세요 (정기권, 일반):')

# 방법 1 : 중첩 조건문 
if card_type == '정기권':
    print('0원')
else:
    if age < 7 or age >= 65:
        print('무료')
    elif age <= 19:
        print('청소년 요금')
    else:
        print('성인 요금')
        
# 방법 2 : 다중 조건문   
if card_type == '정기권':
    print('0원')
elif age < 7 or age >= 65:
    print('무료')
elif age <= 19:
    print('청소년 요금')
else:
    print('성인 요금')