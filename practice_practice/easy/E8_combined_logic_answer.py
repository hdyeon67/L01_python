# [E8] 반복문과 조건문을 섞은 실전 로직 (정답)
# 목표: 리스트에서 짝수만 골라내어 그 합계를 구합니다.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# [Step 1] 변수 준비
even_sum = 0

# [Step 2 & 3 & 4] 반복문과 조건문 결합
for n in numbers:
    if n % 2 == 0:
        even_sum += n

# [Step 5] 출력
print(f"짝수 합계: {even_sum}")
