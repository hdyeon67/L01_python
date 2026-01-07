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



