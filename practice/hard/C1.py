# [Challenge 1] 데이터 결합 (JOIN)
# 두 개의 다른 데이터 소스(users, orders)가 주어질 때, 
# 각 유저별 '총 주문 금액'을 합산하여 유저 이름과 총 금액을 담은 리스트를 만드시오.
# 주문 내역이 없는 유저는 0원으로 표시해야 합니다.

users = [
    {'id': 1, 'name': 'Alice'},
    {'id': 2, 'name': 'Bob'},
    {'id': 3, 'name': 'Charlie'},
    {'id': 4, 'name': 'David'}
]

orders = [
    {'user_id': 1, 'amount': 150},
    {'user_id': 2, 'amount': 200},
    {'user_id': 1, 'amount': 50},
    {'user_id': 3, 'amount': 300},
    {'user_id': 2, 'amount': 100}
]

# 결과 예시: [{'name': 'Alice', 'total': 200}, {'name': 'Bob', 'total': 300}, {'name': 'Charlie', 'total': 300}, {'name': 'David', 'total': 0}]

# 로직 작성



# print(user_totals)
