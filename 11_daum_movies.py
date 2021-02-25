import requests
from bs4 import BeautifulSoup

res = requests.get("https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=https%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F71454256ae63506a7fee5e03cf929b9b65a4f433")
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

images = soup.find_all("img", attrs={"class":"thumb_img"})

for image in enumerate(images):
    #print(image["src"])
    image_url = image["src"]
    if image_url.startswith("//"):
        image_url = "https:" + image_url

    print(image_url)
    image_res = requests.get(image_url)
    image_res.raise_for_status()

    with open("move{}.jpg".format(idx+1), "wb") as f:
        f.write(image_res.content)