# 반복문
# for 문 : 반복 횟수가 정해져 있는 경우 

# 기본 사용법
# for 변수 in 컨테이너:
    # 반복 코드

# 간단 질문!
# for i in True: # 순회할 수 없는 것은 올 수가 없다.
#     print('정답입니다!')
# TypeError: 'bool' object is not iterable

# for i in 5: # 에러 발생
#     print('5번 반복됩니다.')
# TypeError: 'int' object is not iterable

for i in range(5):
    print('5번 반복됩니다.')


# 1. 리스트 순회
names = ['jun','kyle','alex','ken']

for name in names:
    print(f'안녕하세요! {name}님')

# 반복횟수는?
print(len(names))
# Return the number of items in a container.

# 2. 문자열 순회
subject = 'python'
print(len(subject))

for character in subject:
    print(character)
    
# 3. 조건문 활용
numbers = list(range(1,11))
print(numbers)

for number in numbers:
    if number % 2 == 0:
        print(f"{number}는 짝수입니다.")
    else:
        print(f'{number}는 홀수입니다.')

# 간단 질문
print(number) # 정답 : 10