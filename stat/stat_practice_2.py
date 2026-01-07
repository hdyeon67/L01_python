# 기술통계의 활용

prices = [300000, 350000, 400000, 450000, 500000, 550000, 600000, 5000000]

print('=== (1) 중앙값의 적용 ===')
print(prices) # 리스트

# 리스트를 정렬하는 방법 2가지
# 1) 내장함수 sorted 사용 -> 새로운 리스트 반환
# 2) 리스트 메서드 .sort() -> 기존의 리스트 변경

prices.sort() # 오름차순 정렬
print(len(prices))

# 짝수 갯수의 중앙값 구하기
median_price = (prices[3] + prices[4]) / 2
print(f'중앙값 : {median_price}')

# 평균은?
mean_price = sum(prices) / len(prices)
print(f'평균 : {mean_price}')

print('=> 중앙값을 사용해야 하는 이유 : 이상치의 영향을 덜 받기 때문')

# 최빈값 (mode) 구하기
print('=== (2) 최빈값 구하기 === ')
subjects = ["Python", "Java", "Python", "C++", "Python", 
            "Java", "C++", "Python", "Data Science", 
            "Data Science", "Python"]

# 딕셔너리 이용하는 방법
subjects_cnt = {} # 딕셔너리 (순서X, 변경O, 중복X-> key의 경우)

for subject in subjects:
    if subject not in subjects_cnt.keys():
        subjects_cnt[subject] = 1 # 초기화
    else:
        subjects_cnt[subject] += 1 # 1씩 증가

print(subjects_cnt)

# 최고 과목 찾기
best_sub = ""
best_cnt = 0

for sub, cnt in subjects_cnt.items():
    if cnt > best_cnt:
        best_cnt = cnt
        best_sub = sub

print(f'최빈과목은 {best_sub}, 나타난 횟수는 {best_cnt}회')

print('=== (3) 범위와 사분위수 범위 === ')
# 산포도

# 범위 : 최댓값 - 최소값
# 사분위수 범위 : IQR = Q3 - Q1 (중앙값 기준 +-25% 즉, 가운데 50% 변동성만 설명)

scores = [55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 37, 40, 20, 10, 90]
print(scores)

scores_range = max(scores) - min(scores)
print(f"범위 : {scores_range}")

# Q1 = 25% 위치
# Q2 = 중앙값
# Q3 = 75% 위치

# step 1: 리스트 정렬
scores.sort()
print(scores)

print(len(scores))

print(scores[len(scores)//2]) # 중앙값 Q2
Q1 = scores[3]
Q3 = scores[-4]

IQR = Q3 - Q1
print(f'IQR : {IQR}') # 이상치가 존재하는 경우,

print("=== (4) 분산과 표준편차의 이해 ===")

A = [70, 75, 80, 85, 90]
B = [70, 80, 80, 80, 90]

A_mean = sum(A) / len(A)
B_mean = sum(B) / len(B)

print(f'A의 평균 : {A_mean}')
print(f'B의 평균 : {B_mean}')
print('=> 중심경향치(평균)이 똑같다!')
print()

# 산포도 
# 분산
A_var = 0 # 시작을 위해 정의

for a in A:
    A_var += (a - A_mean) ** 2

A_var = A_var / len(A)
A_std = A_var ** 0.5
print(f'A의 분산 {A_var} / A의 표준편차 {round(A_std,2)}')

B_var = 0

for b in B:
    B_var += (b - B_mean) ** 2

B_var = B_var / len(B)
B_std = B_var ** 0.5
print(f'B의 분산 {B_var} / B의 표준편차 {round(B_std,2)}')
