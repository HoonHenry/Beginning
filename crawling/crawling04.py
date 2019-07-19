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
    wd = webdriver.Chrome("D:\\WebDr\\chromedriver.exe")
    wd.get(url)
    wd.set_page_load_timeout(10)
    wd.find_element_by_link_text("랭킹").click()
    result_directory = 'D:\\HoonsCode\\Beginning\\crawling'
    result = []

    html = wd.page_source
    bs = BeautifulSoup(html, 'html.parser')
    # print(bs)
    # wd.find_element_by_xpath(//*[@id="summoner-26670323"]/div[1])
    tag_body = bs.find('tbody')
    # tag_high = bs.find('ul')
    tags_tr1 = tag_body.findAll('tr')
    # tags_li = tag_high.findAll('li')

    # for tag_li in tags_li:
    #     strings = list(tag_li.strings)
    #     userID = strings[1]
    #     tier = strings[2]
    #     ladderPoint = strings[3]
    #     level = strings[4]
    #     winRate = strings[5]
    #
    #     result.append((userID, tier, ladderPoint,
    #                    level, winRate))

    for tag_tr in tags_tr1:
        strings = list(tag_tr.strings)
        user_id = strings[1]
        tier = strings[2]
        ladder_point = strings[3]
        level = strings[4]
        win_rate = strings[5]

        result.append((user_id, tier, ladder_point,
                       level, win_rate))

    table = pd.DataFrame(result, columns=['userID', 'tier', 'ladderPoint',
                                          'level', 'winRate'])
    table.to_csv('{0}/table_LOL.csv'.format(result_directory), encoding='utf-8', mode='w')




crawling(page)
print("end")