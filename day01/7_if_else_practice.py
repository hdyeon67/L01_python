#나이에 따라, 출력하는 단어를 다르게 해봅시다.

age = int(input('나이를 입력하세요 : '))

# 1. 20살 이상 어른
# 2. 10살 이상 청소년기
# 3. 5살 이상 어린이
# 4. 영유아기

if age >= 20 :
    print('어른')
elif age >= 10 :
    print('청소년기')
elif age >= 5 :
    print('어린이')
else :
    print('영유아기')
    