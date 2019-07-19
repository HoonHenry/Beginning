import time
from selenium import webdriver
from itertools import count
from bs4 import BeautifulSoup
import pandas as pd
import requests

page = "https://www.op.gg/"
req = requests.get(page)
print(req.encoding)

def crawling(url):
    # \U 는 유니코드로 인식되기 때문에 \\와 같이 escape 처리
    wd = webdriver.Chrome("D:\WebDr\chromedriver.exe")
    wd.get(url)
    wd.set_page_load_timeout(10)
    wd.find_element_by_link_text("랭킹").click()


    RESULT_DIRECTORY = 'D:\HoonsCode\jccc\\notes\d'
    result = []

    html = wd.page_source
    bs = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
    tag_body = bs.find('tbody', attrs={'id': 'store_list'})
    tags_tr = tag_body.findAll('tr')



crawling(page)
print("end")