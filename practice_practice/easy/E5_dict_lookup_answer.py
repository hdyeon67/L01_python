# [E5] 딕셔너리를 활용한 정보 조회 (정답)
# 목표: 키(Key)를 사용하여 딕셔너리의 값(Value)에 접근합니다.

student = {
    "name": "홍길동",
    "age": 20,
    "major": "Computer Science"
}

# [Step 1] 이름을 출력하세요.
print(f"이름: {student['name']}")

# [Step 2] 나이를 21로 수정하세요.
student["age"] = 21

# [Step 3] "grade" 키와 "A" 값을 추가하세요.
student["grade"] = "A"

# [Step 4] 전체 출력
print(student)
