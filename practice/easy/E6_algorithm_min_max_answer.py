# [E6] 반복문과 조건문으로 최대값 찾기 (정답)
# 목표: 내장 함수 max()를 쓰지 않고, 로직으로 최대값을 찾아봅니다.

scores = [85, 92, 78, 95, 88]

# [Step 1] 첫 번째 값을 최대값 후보로 정합니다.
max_score = scores[0]

# [Step 2] 반복문을 통해 비교합니다.
for s in scores:
    if s > max_score:
        max_score = s

# [Step 3] 최종 최대값을 출력합니다.
print(f"최대값: {max_score}")
