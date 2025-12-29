# 모듈 
# 함수의 정의와 호출을 분리하기 위한 목적

# 기본 사용법
# import 모듈 -> 모듈을 불러와서 사용할 수 있다.
import module_A

print(module_A.add(1,2)) # 호출 (call)
print(module_A.subtract(1,10000)) # 호출 

# 일부만 불러오고 싶을 때는?
from module_A import subtract
# from module_A import * # 함수를 다 불러올 수도 있음

print(subtract(1, 10000))

# 함수 이름이 너무 길 때?
from module_A import subtract as sb

print(sb(1, 10000))