# 멤버십 연산자
# in / not in 
# 특정 값이 "컨테이너 자료형"에 포함이 되어 있는지 검사

# 리스트와 멤버십 연산자
numbers = [1, 2, 3, 4, 5]
print(type(numbers))

print(3 in numbers)
print(3 not in numbers)

# 질문
# print(3 in 3) # TypeError: argument of type 'int' is not iterable

# 예시 1. 3이 있는지를 확인하는 코드
for num in numbers:
    if num == 3:
        print('3이 있습니다.')
        break

# 예시 2. 멤버십 연산자
if 3 in numbers:
    print('3이 있습니다.')

# 딕셔너리와 멤버십 연산자
colors = {'Red':'빨강', 'Blue':'파랑', 'Yellow':'노랑'}
print(colors)
print(type(colors))

# 질문
print('빨강' in colors) # False
print('Red' in colors) # True
# => key 모음에 포함될 때만 True

# values에서 존재여부를 검사하고 싶을 때,
# colors.values() 메소드 사용하면 된다!
print(colors.values())
print('빨강' in colors.values())