from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
#headless chrome 의 출입을 막아야겠네?
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
# 이렇게 옵션을 추가하면 headless chrome 으로 안뜨고 그냥 크롬으로 뜬다.

browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) 
# AppleWebKit/537.36 (KHTML, like Gecko) 
# Chrome/87.0.4280.88 Safari/537.36
detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
browser.quit()