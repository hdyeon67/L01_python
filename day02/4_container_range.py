# 컨테이너 자료형
# range(start, end, step)
# 순서가 존재하는 "연속된 정수 목록"을 반환

# 특징 1: 순서가 존재
print(range(1, 11))
print(type(range(1,11)))
# 인간이 눈으로 보고 이해 가능하게 나타나지 않음

numbers = range(1, 11)
print(numbers[1]) # 인덱싱 가능
print(numbers[1:4]) # 슬라이싱 가능

# range는 보통 list로 형변환하여 확인
print(list(numbers))

# 특징 2 : 불변 자료형
# numbers[1] = 20 # 에러 발생
# TypeError: 'range' object does not support item assignment

# 주요 사용법 - for 반복문과 함께 사용
for i in range(1,11,2):
    print(i)