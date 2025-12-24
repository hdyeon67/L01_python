# 익명함수
# lambda 
# 왜 이름이 없어? 이름 붙일 만큼 중요하지 않아서

# 기존의 방식
def add(x,y):
    answer = x + y
    return answer
result = add(1,4)
print(result)

# 익명함수를 이용한 방식
result = (lambda x, y: x + y)(1, 4)
print(result)

numbers = [1,5,3,7,10,4]
print(numbers)

numbers_new = sorted(numbers, key=lambda x:-x)
print(numbers_new)

# 리스트 형태
example = [(0, 2), (3, 5), (1, 4), (0, -1)]
# 각 요소 (앞, 뒤) 라고 했을 때, 뒤를 기준으로 오름차순 정렬

example_new = sorted(example, key=lambda x:x[1])
print(example_new)

print(type(example))
print(type(example[0]))