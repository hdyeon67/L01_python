# max() 의 직접 구현
nums = [7, 1, 2, 4, 6, 8, 3]

print(max(nums))
print(min(nums))

print('=== 최댓값 찾기 ===')
max_value = -9999 # 충분히 작은 초기값

for n in nums:
    print(max_value, n)
    if max_value < n: # n과 max_value를 비교
        # 만약 n이 max_value보다 크면,
        max_value = n # 재할당 : n으로 최댓값 갱신
    else:
        pass

print(max_value)

# min() 의 직접 구현
print('=== 최솟값 찾기 ===')
min_value = 9999 # 최소값을 갱신할 수 있도록 충분히 큰 초기값

for n in nums:
    print(min_value, n)
    if min_value > n:
        min_value = n
    else:
        pass

print(min_value)