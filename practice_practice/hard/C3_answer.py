# [Challenge 3] 다중 그룹화 및 집계 (Group By) - 정답

logs = [
    {'region': 'Seoul', 'category': 'Electronics', 'sales': 100},
    {'region': 'Busan', 'category': 'Food', 'sales': 50},
    {'region': 'Seoul', 'category': 'Food', 'sales': 30},
    {'region': 'Seoul', 'category': 'Electronics', 'sales': 200},
    {'region': 'Busan', 'category': 'Electronics', 'sales': 150},
    {'region': 'Jeju', 'category': 'Food', 'sales': 40}
]

agg_result = {}

for log in logs:
    region = log['region']
    category = log['category']
    sales = log['sales']
    
    # 지역이 처음 등장하면 딕셔너리 생성
    if region not in agg_result:
        agg_result[region] = {}
        
    # 해당 지역 내 카테고리가 처음 등장하면 0으로 초기화
    if category not in agg_result[region]:
        agg_result[region][category] = 0
        
    agg_result[region][category] += sales

print(agg_result)
