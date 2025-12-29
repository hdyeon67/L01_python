# [Challenge 2] 이상치 탐지 및 필터링 - 정답
import math

data = [10, 12, 11, 13, 9, 10, 100, 11, 12, 8, 10, 110, 9, 10]

# 1. 평균 계산
mean = sum(data) / len(data)

# 2. 표준편차 계산
variance = sum((x - mean)**2 for x in data) / len(data)
std_dev = math.sqrt(variance)

# 3. 이상치 경계 설정
lower_bound = mean - 2 * std_dev
upper_bound = mean + 2 * std_dev

# 4. 필터링
cleaned_data = []
outliers = []

for x in data:
    if lower_bound <= x <= upper_bound:
        cleaned_data.append(x)
    else:
        outliers.append(x)

print("정상 데이터:", cleaned_data)
print("이상치:", outliers)
# 예상 결과: 정상 데이터는 10 내외의 값들, 이상치는 [100, 110]
