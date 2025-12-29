# [Challenge 1] 데이터 결합 (JOIN) - 정답

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

# 1. 유저 ID별 총액을 저장할 딕셔너리 생성 (0으로 초기화)
totals_by_id = {}
for user in users:
    totals_by_id[user['id']] = 0

# 2. 주문 내역 순회하며 합산
for order in orders:
    uid = order['user_id']
    if uid in totals_by_id:
        totals_by_id[uid] += order['amount']

# 3. 유저 이름과 결합하여 최종 결과 리스트 생성
user_totals = []
for user in users:
    user_totals.append({
        'name': user['name'],
        'total': totals_by_id[user['id']]
    })

print(user_totals)
