# [E1] 사용자 입력과 기본 연산 (정답)
# 목표: 사용자로부터 숫자를 입력받아 간단한 계산 결과를 출력합니다.

# [Step 1] 첫 번째 숫자를 입력받으세요.
num1 = int(input("첫 번째 숫자를 입력하세요: "))

# [Step 2] 두 번째 숫자를 입력받으세요.
num2 = int(input("두 번째 숫자를 입력하세요: "))

# [Step 3] 두 숫자의 합을 계산하고 출력하세요.
add_result = num1 + num2
print(f"두 수의 합: {add_result}")

# [Step 4] 두 숫자의 곱을 계산하고 출력하세요.
mul_result = num1 * num2
print(f"두 수의 곱: {mul_result}")
