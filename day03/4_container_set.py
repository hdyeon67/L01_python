# 컨테이너 자료형 집합
# 집합 (set)
# 중복이 존재하지 않는 0개 이상의 집합
numbers = {1, 2, 3, 4, 5}
print(numbers)
print(type(numbers))

# 특징 1: 순서가 존재하지 않음
# print(numbers[0]) # TypeError: 'set' object is not subscriptable

# 수학적 집합의 특성을 그대로 따름
# 교집합, 합집합, 차집합 등

# 특징 2 : 가변 자료형
# 변경 : 추가, 삭제
numbers.add(6)
print(numbers)

numbers.add(6) # 추가되는 것 처럼 보이지만, 중복을 허락하지 않기 때문에 
print(numbers)

numbers.add('10')
print(numbers)

# numbers.add(['hello!']) # TypeError: unhashable type: 'list'
# print(numbers)

# 삭제
numbers.remove("10")
print(numbers)

# numbers.remove("10") # KeyError: '10' -> 10이 없는데 삭제하라고 하였기 때문
# print(numbers)

numbers.discard("존재하지 않는 것을 삭제하려 해도 ok")
print(numbers)


# 수학적 집합의 연산
# 합집합
# 교집합
# 차집합

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

# 합집합
print(set1 | set2)
print(set1.union(set2)) # 새로운 합집합 반환
# print(set1 + set2) 
# # TypeError: unsupported operand type(s) for +: 'set' and 'set'

# 교집합
print(set1 & set2)
print(set1.intersection(set2))

# 차집합
print(set1 - set2)
print(set1.difference(set2))