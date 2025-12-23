# 떡잎마을 반장선거
# 후보가 없는 반장선거
# 표가 발생하면, 자동 입후보 되는 구조

votes = ['짱구', '짱구', '수지', '짱구', '훈이', '맹구', '수지', '수지', '수지', '짱구', '유리', '철수']
vote_count = {}
for vote in votes:
    if vote not in vote_count:
        vote_count[vote] = 1
    else :
        vote_count[vote] += 1
        
max_count = 0
winner = ''

for candidate, count in vote_count.items():
    if count > max_count:
        max_count = count
        winner = candidate

print(f'반장({max_count}표): {winner}')
        
        
         
         