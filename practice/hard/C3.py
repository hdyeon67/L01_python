# [Challenge 3] 다중 그룹화 및 집계 (Group By)
# 다음과 같은 원시 로그 데이터가 주어질 때,
# '지역(Region)'별로 '카테고리(Category)'별 '판매량(Sales)'의 합계를 구하시오.
# 결과는 중첩 딕셔너리 구조여야 합니다.

logs = [
    {'region': 'Seoul', 'category': 'Electronics', 'sales': 100},
    {'region': 'Busan', 'category': 'Food', 'sales': 50},
    {'region': 'Seoul', 'category': 'Food', 'sales': 30},
    {'region': 'Seoul', 'category': 'Electronics', 'sales': 200},
    {'region': 'Busan', 'category': 'Electronics', 'sales': 150},
    {'region': 'Jeju', 'category': 'Food', 'sales': 40}
]

# 결과 예시: {'Seoul': {'Electronics': 300, 'Food': 30}, 'Busan': {...}, ...}

# 로직 작성



# print(agg_result)
