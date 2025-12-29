# [E3] 리스트 데이터 접근하기 (정답)
# 목표: 리스트에서 특정 위치의 데이터를 가져오고 수정해봅니다.

fruits = ["apple", "banana", "cherry", "durian"]

# [Step 1] 첫 번째 요소를 출력하세요.
print(fruits[0])

# [Step 2] 마지막 요소를 출력하세요.
print(fruits[-1])

# [Step 3] "banana"를 "blueberry"로 변경하세요.
# 방법 1: 인덱스 이용하여 수정
fruits[1] = "blueberry"

# 방법 2: index 메서드와 try except 문을 사용하여 수정
try:
    fruits[fruits.index("banana")] = "blueberry"
except ValueError:
    print("banana not found")

# [Step 4] 리스트 전체를 출력하세요.
print(fruits)
