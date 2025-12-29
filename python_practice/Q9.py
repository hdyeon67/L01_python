# [실습 9]
# 다음 리스트에서 이메일 주소의 도메인(gmail.com, naver.com 등)만 추출하여 
# 중복을 제거한 뒤, 알파벳 순서대로 정렬된 리스트를 구하시오.
emails = ['abc@naver.com', 'def@gmail.com', 'ghi@naver.com', 'jkl@daum.net', 'mno@gmail.com']

# 로직 작성
domain_list = []
for item in emails:
    domain = item.split('@')[1]
    domain_list.append(domain)
print(domain_list)
    
unique_domain_list = list(set(domain_list))
print(unique_domain_list)

unique_domain_list.sort()
print(unique_domain_list)
unique_domain_list.sort(reverse=True)
print(unique_domain_list)


# print(unique_domains) # ['daum.net', 'gmail.com', 'naver.com']
