import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top"
#headers = {
    #"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36}",
    #"Accept-Language" : "ko-KR,ko"}
#한글 페이지를 반환해 달라고 유저에이전트 헤더 태그로 요청

res = requests.get(url)
res.raise_for_status
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
#div 태그에 class 이름이 ImZGtf mpg5gc 인 모든 엘리멘트를 가져와줘.
print(len(movies))

with open("movie.html", "w", encoding="utf8") as f:
    f.write(soup.prettify()) #html 문서를 예쁘게 출력

    
for movie in movies : 
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)

    # -*- coding: utf-8 -*- 
#pylint: disable-msg=E0611