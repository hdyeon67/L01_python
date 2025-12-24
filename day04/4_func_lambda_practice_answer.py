# [수 정렬하기]
# 주어진 2차원 리스트를 기준에 따라서 정렬하세요.
# item을 [앞쪽, 뒤쪽] 이라고 할 때, 
# (1) 뒤 쪽이 '작은' 순서로 정렬하세요. -> item[1] 기준 / 오름차순
# (2) 만약 같다면 앞쪽이 '큰' 순서대로 정렬하세요. -> item[0] 기준 / 내림차순
nums = [[70, 30], [70, 10], [20, 30], 
        [50, 90], [40, 80], [80, 90], [10, 60]]

print(len(nums))
print(type(nums))

nums_new = sorted(nums)
print(nums_new) # 단순 오름차순

# item[1] 기준으로 오름차순 후, item[0] 기준으로 내림차순

nums_new = sorted(nums, key=lambda item:(item[1],-item[0]))
# lambda item:item[1],-item[0] # 이처럼 하나로 묶어주지 않는 경우
# -item[0]를 argument로 처리함 -> 에러 발생
# SyntaxError: positional argument follows keyword argument
print(nums_new)

def solution(x):
    return x, x**2

print(solution(3))
print(type(solution(3)))