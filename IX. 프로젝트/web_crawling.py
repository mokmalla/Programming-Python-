#터미널 > pip install bs4

from bs4 import BeautifulSoup
from urllib.request import urlopen

#네이버 웹툰 > 신의 탑 제목 가져오자

if __name__ == '__main__':
    # data = urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=183559&weekday=mon")
    # data = urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=651673&weekday=wed")
    # soup = BeautifulSoup(data,"lxml")
    with urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=183559&weekday=mon") as response:
        response_byte = response.read()
    cartoon_titles = soup.find_all("td", attrs={'class':'title'})   #<td class="title">
    html = "<html><body><meta charset='utf-8'></head><body>"
    print(html)
    for title in cartoon_titles:
        t = title.find('a').text     #제목 가져오자
        link = title.find("a").get("href")  #link 가져오자
        link="http://comic.naver.com/"+link
        # print(t)
        # print(link)
        # print("<a href='"+link+"'>"+t+"</a>")
        html+="<a href='"+link+"'>"+t+"</a><br>"
    html=="</body></html>"
    outputSoup = BeautifulSoup(html, "lxml")    #htmlstring -> BeaurifulSoup 객체
    prettyHtml = str(outputSoup.prettify())     #html 줄 예쁘게
    with open("유미의세포들.html","w",encoding="utf-8") as f:
        f.write(html)

    #다음 웹툰 > 어쩌다 발견한 7월
    # data = urlopen("http://webtoon.daum.net/webtoon/view/findjuly")
    # soup = BeautifulSoup(data,"lxml")
    # print(data)
    # cartoon_titles = soup.find_all("string", attrs={'class':'tit_wt'})
    # for title in cartoon_titles:
    #     print(t)