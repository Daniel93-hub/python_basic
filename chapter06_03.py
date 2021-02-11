# Chapter06-3
# 파이썬 패키지
# 패키지 작성 및 사용법
# 파이썬은 패키지로 분할 된 개별적인 모듈로 구성
# __init__.py : Python3.3 부터는 없어도 패키지로 인식 -> 단, 하위 호환을 위해 작성 추천
# 상대 경로 : ..(부모 디렉토리), .(현재 디렉토리) -> 모듈 내부에서만 사용

# 예제1
import sub.sub1.module1
import sub.sub2.module2

# 사용
sub.sub1.module1.mod1_test1()
sub.sub1.module1.mod1_test2()

# 사용
sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test2()

print()
print()
print()

# 예제2
from sub.sub1 import module1
from sub.sub2 import module2 as m2 # Alias

# 사용
module1.mod1_test1()
module1.mod1_test2()

# 사용
m2.mod2_test1()
m2.mod2_test2()

print()
print()
print()

# 예제3
from sub.sub1 import *
from sub.sub2 import *

# 사용
module1.mod1_test1()
module1.mod1_test2()

# 사용
module2.mod2_test1()
module2.mod2_test2()

print()
print()
print()
