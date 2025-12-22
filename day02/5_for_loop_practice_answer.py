# for 문 간단실습
# 1~10 더한 값 55 출력하기

answer = 0 # 초기값

# 반복적으로 이루어지는 작업!
# answer = answer + 1
# answer = answer + 2
# answer = answer + 3
# ....
# answer = answer + 10

# 컨테이너
# list, string, tuple, .... -> 컨테이너 자료형
# 순서가 존재하는 정수 목록 
# range(start, end) -> start 부터 end-1 의 정수목록을 반환

for i in range(1, 11): 
    answer += i

print(answer) # 55

# 조건에 따라서 합산 가능
answer = 0

for i in range(1,11):
    if i % 2 == 0: # 짝수인 케이스에만 한해
        answer += i
        print(f'answer의 변화 : {answer}')

print(answer)