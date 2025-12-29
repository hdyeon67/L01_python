# 학생들의 이름과 시험 점수가 2차원 리스트로 주어집니다.
# 점수가 두 번째로 높은 학생(들)의 이름을 리스트 형태로 출력하시오.
# (점수가 가장 높은 학생이 여러 명일 수 있으며, 두 번째로 높은 점수도 여러 명일 수 있습니다.)
scores = [['Kim', 88], ['Lee', 95], ['Park', 92], ['Choi', 85], ['Jung', 95], ['Kang', 92]]

# 로직 작성
all_scores = []
for score in scores:
    all_scores.append(score[1])
    
unique_scores = sorted(list(set(all_scores)), reverse=True)

if len(unique_scores) >= 2:
    runner_up_students = []
    second_score = unique_scores[1]
    for score in scores:
        if score[1] == second_score:
            runner_up_students.append(score[0])
else :
    print('두번째로 높은 점수가 없습니다')

print(runner_up_students) # ['Park', 'Kang']
