#soup 객체를 활용해서 엘리멘트와 속성, 속성값을 간단하게 반환하기

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()  #무슨 문제가 발생하면 프로그램 종료 엘리멘트

soup = BeautifulSoup(res.text, "lxml") 
# 가져온 html 텍스트를 lxml를 통해서 뷰티풀숲 객체로 만든거임 soup 은 모든걸 가지고 있음.
print(soup.title) 
#soup 객체를 통해서 웹툰 페이지의 타이틀을 빼올 수 있음.
print(soup.title.get_text())
#하위 텍스트도 가져올 수 있음.
print(soup.a)
#첫 번째 발견되는 a 엘리멘트를 가져와줘(반환).
print(soup.a.attrs)
#a 태그 안에 있는 어트리뷰트(온클릭, 메뉴 도큐멘트 등)를 가져와줘(반환)
print(soup.a["href"])
# a 엘리멘트의 href 속성 값을 반환.

print(soup.find("a", attrs={"class": "Nbtn_upload"}))
# a 태그에 해당하는 첫 번째 엘리멘트를 가져오는데 조건을 주는 attrs.
# class 라는 속성을 이용하여 ""에서 처음에 발견되는 속성 값을 반환.

# print(soup.find("li", attrs={"class":"rank01"}))
# 부모 자식 왔다갔다 하는 sibling 과 previous
rank1 = soup.find("li", attrs={"class":"rank01"})
rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text())
rank2 = rank3.previous_sibling.previous_sibling
print(rank2.a.get_text)

#print(rank1.parent)
rank2 = rank1.find_next_sibling("li") 
print(rank2.a.get_text())
#넥스트 시블링을 연속으로 칠 필요 없이 li 인 것만 반환
rank3 = rank2.find_next_sibling("li") 
print(rank3.a.get_text())
rank2 = rank3.find_previous_sibling("li")
print(rank2.a.get_text())

rank1.find_next_siblings("li") # 랭크1기준으로 li 의 형제들을 모두 가져온다
print(rank1.find_next_siblings("li"))


