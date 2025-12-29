# [실습 6] 
# 전체 출석부와 현재 출석한 인원이 리스트로 주어질 때, 출석하지 않은 인원을 출력하시오. (순서 굳이 상관 없음)
students = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']  # 전체 명단
attened = ['c', 'e', 'f', 'h']  # 출석 명단

for student in students:
    if student not in attened:
        print(student)
print('\n')

students_set = set(students)
attened_set = set(attened)
answer = students_set - attened_set
for student in answer:
    print(student)