# 사용자 정의함수 len_func 작성
# numbers = [2,45,6,8,2543,8,32,6,2,6,8]
# # 1단계 : 정의
# def len_func(container):
#     count = 0
#     for _ in container:
#         count += 1
#     return count

# # 2단계 : 호출
# print(len_func(numbers))

# 트리형 별 찍기 함수 작성
# 주석 추가, 구체적이고 상세하게 작성
# def print_tree(num): # 트리 높이(num)를 입력받아 트리형 별을 출력하는 함수
#     for i in range(1, num + 1): # 1부터 num까지 반복
#         print('*' * (num - i) + ' ' * (2 * i - 1) + '*' * (num - i)) # 공백과 별을 조합하여 트리형 별 출력 # 공백은 (num - i)개, 별은 (2 * i - 1)개 출력

# print_tree(int(input('트리 높이 입력 : '))) 

# def print_stars(num):
#     for i in range(1, num + 1):
#         print('*' * i)
        
# print_stars(int(input('별 개수 입력 : ')))

#  for문을 사용하여 아래 내용을 확인해 보세요.
# 최고 매출이 일어난 일차(1부터 시작)와 해당 금액
# 최저 매출이 일어난 일차와 해당 금액
# sales = [2000, 3000, 4000, 1000, 1500, 3800, 200, 2900, 1300]
# max_sales = sales[0]
# min_sales = sales[0]
# max_day = 1
# min_day = 1

# for i in range(len(sales)):
#     if sales[i] > max_sales:
#         max_sales = sales[i]
#         max_day = i + 1
#     if sales[i] < min_sales:
#         min_sales = sales[i]
#         min_day = i + 1

# print(f"최고 매출일차: {max_day}, 금액: {max_sales}")
# print(f"최저 매출일차: {min_day}, 금액: {min_sales}")

# 주어진 2차원 리스트를 기준에 따라서 정렬하시오. lambda 표현식 사용
# (1) [앞쪽, 뒤쪽] 이라고 할 때, 뒤 쪽이 '작은' 순서로 정렬하되 
# (2) 만약 같다면 앞쪽이 '큰' 순서대로 정렬하시오.
nums = [[70, 30], 
        [70, 10], 
        [20, 30], 
        [50, 90], 
        [40, 80], 
        [80, 90], 
        [10, 60]]
sorted_nums = sorted(nums, key=lambda x: (x[1], -x[0]))
print(sorted_nums)