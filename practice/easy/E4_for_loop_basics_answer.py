# [E4] 반복문을 이용한 합계 구하기 (정답)
# 목표: 리스트에 들어있는 모든 숫자의 합계를 직접 계산해봅니다.

numbers = [10, 20, 30, 40, 50]

# [Step 1] 합계를 저장할 변수를 만드세요.
total = 0

# [Step 2] for 문을 사용하여 각 숫자를 더하세요.
for num in numbers:
    total += num

# [Step 3] 결과를 출력하세요.
print(f"합계: {total}")
