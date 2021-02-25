# 그냥 find 는 해당하는 것에 첫 번째, find_all은 해당하는 모든 값을 반환.

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") #lxml 이 도대체 뭐임?
cartoons = soup.find_all("td", attrs={"class":"title"})
title = cartoons[0].a.get_text()
link = cartoons[0].a["href"]
print(title)
print("https://comic.naver.com"+ link)

for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = "https://comic.naver.com" + cartoon.a["href"]
    print(title, link)






