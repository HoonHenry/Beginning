import time
from selenium import webdriver
from itertools import count
from bs4 import BeautifulSoup
import pandas as pd
import requests


def crawlin_goobne():


    # \U 는 유니코드로 인식되기 때문에 \\와 같이 escape 처리
    wd = webdriver.Chrome("D:\WebDr\chromedriver.exe")
    wd.get(url)

    RESULT_DIRECTORY = 'D:\HoonsCode\jccc\\notes\d'
    result = []
    for page in count(1):
        script = 'store.getList(%d)' % page
        # 굽네치킨에서 사용하는 페이지를 이동시키는 js code
        wd.execute_script(script) # js 실행
        time.sleep(5)

        html = wd.page_source
        bs = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
        tag_body = bs.find('tbody', attrs={'id': 'store_list'})
        tags_tr = tag_body.findAll('tr')
        # print(tags_tr)

        if tags_tr[0].get('class') is None:
            break
        # 맨 마지막 페이지인 102에서는 class='on lows'가 없다. => 종료 조건

        for tag_tr in tags_tr:
            strings = list(tag_tr.strings)
            name = strings[1]
            address = strings[6]
            result.append((name, address))

        table = pd.DataFrame(result, columns=['name', 'address'])
        table.to_csv('{0}/table_goobne.csv'.format(RESULT_DIRECTORY), encoding='utf-8', mode='w')


url = 'http://www.goobne.co.kr/store/search_store.jsp'
req = requests.get(url)
print(req.encoding)
crawlin_goobne()
print("end")
