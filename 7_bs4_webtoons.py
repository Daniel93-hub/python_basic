# 그냥 find 는 해당하는 것에 첫 번째, find_all은 해당하는 모든 값을 반환.

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status() 

soup = BeautifulSoup(res.text, "lxml") 

#네이버 웹툰 전체 목록 가져오기
cartoons = soup.find_all("a", attrs={"class":"title"})
# class 속성이 title 인 모든 "a" 엘리멘트를 반환.
for cartoon in cartoons:
    print(cartoon.get_text())