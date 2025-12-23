# 기초 자료 구조와 로직 설계

# 순서가 있는 자료 구조
# -> 순서(위치)로 값을 관리
user = ['alex',3,True]
print(user[0])  # 0번째 위치한 값이 "이름"임을 알고있어야 함
print(user[-1]) # -1번째 위치한 값이 "운전면허 여부"임을 알고 있어야 함
# => 자료를 표현하는데 적합하지 않을 수 있다.

# 딕셔너리
# "순서"가 없는 자료 구조
# key - value 한 쌍의 구조
user = {'name':'alex',
        'age':3,
        'license':True, 
        'money':3000 }
print(type(user))

print(user['age'])
print(user['money'])

# => 자료를 표현하는데 적합하다.