from selenium import webdriver
import time
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

# req = Request('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
# req = urlopen(req)
# html = res.read().decode('cp949')


path = "D:\WebDr\chromedriver.exe"
driver = webdriver.Chrome(path)
# driver = webdriver.Firefox()
# driver = webdriver.Ie()

driver.set_page_load_timeout(10)
driver.get("https://www.op.gg/")
driver.find_element_by_name("userName").send_keys("필동호랭이")
driver.find_element_by_class_name("챔피언 분석").click()
time.sleep(4)
driver.quit()

def ex1():
    bs = BeautifulSoup(html, 'html.parser')
    print(bs, type(bs))

    tag = bs.a
    print(tag, type(tag))
def ex2():
    bs = BeautifulSoup(html, 'html.parser')

    tag = bs.td
    print(tag['class'])
    print(tag['id'])
    print(tag.attrs)

    tag = bs.div
    print(tag['id'])

def ex3():
    bs = BeautifulSoup(html, 'html.parser')

    tag = bs.find('div', attrs={'class': 'tit3'})
    print(tag)

    tag = bs.find('div')
    print(tag)

    tag = bs.find('td', attrs={'class': 'not_exist'})
    print(tag)

    tag = bs.find(attrs={'title': '범죄도시'})
    print(tag)





