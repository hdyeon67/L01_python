# 알고리즘 기초
# 다양한 설계 방식에 대해 알아봅시다!

gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]

# (1) 1등급 광물의 존재 여부를 알아보는 문제
# 방법 1: 멤버십 연산자(in)
print(1 in gems)

# 방법 2: for문 / 제어문 활용
grade_1 = False
for gem in gems:
    if gem == 1:
        grade_1 = True
        break

print(grade_1)

# (2) 등급별 광물의 갯수
# 방법 1: 리스트
grade_list = [0] * 3 # 등급 별 위치에 갯수 기록
print(grade_list)

for gem in gems:
    print(gem)
    grade_list[gem-1] += 1

print(grade_list)

# 방법 2: 딕셔너리
grade_dict = {1:0, 2:0, 3:0}
print(type(grade_dict))

for gem in gems:
    grade_dict[gem] += 1
print(grade_dict)

# 등급이 정해져 있지 않은 상황
grade_dict = {}
print(type(grade_dict))

for gem in gems:
    if gem not in grade_dict:
        grade_dict[gem] = 1
    else:
        grade_dict[gem] += 1

print(grade_dict)