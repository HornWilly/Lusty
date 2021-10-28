from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()

driver.get("https://page.onstove.com/epicseven/global/list/e7en001?listType=2&page=1&direction=Latest")

content = driver.page_source
driver.close()
soup = BeautifulSoup(content, features="lxml")

for news in soup.find_all("div", attrs={'class': "group-col group-subject"}):
    print(news)

# print(soup.text)
