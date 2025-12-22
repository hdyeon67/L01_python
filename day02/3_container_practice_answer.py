# 문자열 포맷과 시간 변환
# 문자열 : 순서가 존재하는 문자들의 모음
minutes = int(input('시간(분)을 입력해 주세요: ')) # 135

hour = minutes // 60
minute = minutes % 60 

answer = ""
print(len(answer)) # 빈 문자열도 문자열이다!
print(type(answer))

if hour > 0:
    answer = answer + f'{hour}시간' # + 연산 (연결)

if minute > 0:
    answer += f'{minute}분' # 복합 연산

print(answer) # 2시간15분