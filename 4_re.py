import re
#re = 정규식 abcd,book, desk
# ca?e
#care, cafe, case, cave??
#caae, cabe, cace, cade ... 이런 식을 쉽게 찾는 컴파일

p = re.compile("ca.e")
# . (ca.e): 하나의 문자를 의미 - > care, cafe, case O/ caffe X
# ^ (^de): 문자열의 시작  - > desk, destination~~ O/ fade X
# $ (se$) : 문자열의 끝 - > case, base O/ face X

def print_match(m):
    if m:
        print(m.group())
    else:
        print("매칭X")
 
#m = p.match("careless") # match는 주어진 문자열의 처음부터 일치하는지 확인하는 것
#print_match(m)
#print(m.group()) # 매치되지 않으면 에러 발생

#m. 의 여러 인덱스
#print(m.string()) : 입력받은 문자열
#print(m.start()) : 일치하는 문자열의 시작 index
#print(m.end()) : 일치하는 문자열의 끝 index
#print(m.span()) : 일치하는 문자열의 시작 / 끝 index

m = p.search("careless") # search : 주어진 문자열 중에 일치하는게 있는지 확인
print_match(m)

#1. lst = p.findall("good care cafe") findall : 일치하는 모든 것을 리스트 형태로 반환
#2. m = p.match("비교할 문자열") : 주어진 문자열 중에 처음부터 일치하는게 있는지 확인
#3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지
#4. p = re.compile("원하는 형태") 원하는 형태 : 정규식
# . (ca.e): 하나의 문자를 의미 - > care, cafe, case O/ caffe X
# ^ (^de): 문자열의 시작  - > desk, destination~~ O/ fade X
# $ (se$) : 문자열의 끝 - > case, base O/ face X