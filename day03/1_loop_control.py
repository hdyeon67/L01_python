# 반복문 제어

# break
print('== break ==')

# numbers = [1,2,3,4,5]
numbers = list(range(1,6))
print(numbers)
print(len(numbers))

print('= for와 break 예시 =')

for num in numbers:
    print(num) # 전체를 반복
    
    if num == 3:
        print('3을 만났습니다!')
        print('반복을 종료합니다.')
        break
        print('결코 출력될 수 없습니다.')

print('= while과 break 예시 =')
i = 0
while True:
    print(numbers[i])
    if numbers[i] == 3:
        print('3을 만났습니다.')
        print('반복을 종료합니다.')
        break
    i += 1 # 증감식

print('= else =')

print(numbers)
# target = int(input('숫자를 입력해 주세요 :'))
target = 3
# for num in numbers:
#     print(num)
#     if num == target:
#         print(f'{target}을 찾았습니다.')
#         break
#     print(f'{target}을 찾지 못했습니다.') # 차이점 확인하기!

# for num in numbers:
#     print(num)
#     if num == target:
#         print(f'{target}을 찾았습니다.')
#         break
# print(f'{target}을 찾지 못했습니다.') # 차이점 확인하기!

for num in numbers:
    print(num)
    if num == target:
        print(f'{target}을 찾았습니다.')
        break
else:     
    print(f'{target}을 찾지 못했습니다.')

# 반복이 break로 제어되지 않으면, 반복이 완료후 실행되는 단락


print('== continue ==')

number = 0

while number < 10:
    number += 1 # 증감식의 위치
    
    if number % 2 == 0: # 짝수
        print('넘어가!')
        continue
        print('결코 실행되지 않습니다.')
    
    print(number)
    # number += 1 # 증감식의 위치 주의!
    

print('=== pass ===')

def solution(number):
    pass

# def solution(number): # pass가 없는 경우
    # IndentationError: expected an indented block after function definition on line 83

for num in numbers:
    if num == 3:
        pass
    else:
        print('3이 아닙니다.')