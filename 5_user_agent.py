#암튼 브라우저마다 유저에이전트 값이 다르다 라는 걸 얘기하는 듯
import requests
res = requests.get("http:nadocoding.tistiory.com")
res.raise_for_status()
with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)

#그냥 자기 알아서 끝내버리네 어이없음 ㅋㅋ