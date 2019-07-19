from bs4 import BeautifulSoup

html = '<td id="td1" class="title">' \
        '   <div class="tit3">' \
        '       <a href="/movie/bi/mi/basic.nhn?code=161242" title="범죄도시">범죄도시</a>' \
        '   </div>' \
        '</td>'

# 조회
def ex1():
    #위의 html 문자열에 대해서, html 파싱하겠다
    bs = BeautifulSoup(html, 'html.parser')
    print(bs, type(bs))

    # a 태그 출력
    tag = bs.a
    print(tag, type(tag))


# Attribute 값 받아오기
def ex2():
    bs = BeautifulSoup(html, 'html.parser')

    tag = bs.td
    print(tag['class'])
    print(tag['id'])
    print(tag.attrs)

    tag = bs.div
    print(tag['id'])

# Attribute 검색
def ex3():
    bs = BeautifulSoup(html, 'html.parser')

    #div 태그 중, class가 tit3인 태그를 찾는다
    tag = bs.find('div', attrs={'class': 'tit3'})
    print(tag)

    tag = bs.find('div')
    print(tag)

    # 없는 태그를 조회할 경우
    tag = bs.find('td', attrs={'class': 'not_exist'})
    print(tag)

    # 전체 태그에 대해 title이 범죄도시인 태그를 찾음
    tag = bs.find(attrs={'title': '범죄도시'})
    print(tag)

# select(), content() method
def ex4():
    bs = BeautifulSoup(html, 'html.parser')
    # css 처럼 셀렉터를 지정할 수 있다
    tag = bs.select("td div a")[0]
    print(tag)

    text = tag.contents[0]
    print(text)


# extract() method
def ex5():
    bs = BeautifulSoup(html, 'html.parser')
    tag = bs.select("td")[0]
    print(tag)

    # div 요소 제거
    div_elements = tag.find_all("div")
    for div in div_elements:
        div.extract()

    print(tag)


ex1()
ex2()
ex3()
ex4()
ex5()

