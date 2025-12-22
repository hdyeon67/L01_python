# 컨테이너 자료형
# 문자열 (string)
# 0개 이상의 문자를 순서가 있게 저장하는 컨테이너 자료형

subject = "python"
print(subject)
word = 'hello'
print(type(subject)) # 문자열

# + 연산 : 문자열 + 문자열
print(word + subject) 
# => 문자열끼리 바로 이어 붙인다.

# * 연산 : 문자열 * 반복횟수(int)
print(subject * 3)

# 특징 1: 순서가 존재한다.
# 인덱스 (위치)로 값을 확인 가능
print(subject[0])
print(subject[-1])
# 슬라이싱 가능
print(subject[1:3])

# 특징 2 : 불변 자료형 (immutable)
# 불가능하다, 변경이

# subject[0] = 'P' # 에러발생
# TypeError: 'str' object does not support item assignment

# 변경한 것처럼 보이는 케이스
print(id(subject))
print(subject[1:]) # 슬라이싱

# 재할당
subject = 'P' + subject[1:] # "+" 연산 : 문자 + 슬라이싱

print(subject)
print(id(subject))


print(len(subject))
# len() 내장 함수를 통해 컨테이너 아이템의 갯수를 확인할 수 있다!
# Return the number of items in a container.

print(len([1,2,3,4,5]))

print(len((1,2,3,4,5)))

# 컨테이너 자료형과 기초 자료형과의 차이
# print(len(3.14)) # 에러발생
# print(len(True))
print(len('True'))