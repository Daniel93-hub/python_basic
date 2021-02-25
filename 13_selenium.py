from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os.path

scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, 'chromedriver')
testFile=open(filename)

driver = webdriver.Chrome(filename)
driver.get('https://naver.com')


