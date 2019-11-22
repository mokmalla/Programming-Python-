#터미널 > pip install bs4

from bs4 import BeautifulSoup
from urllib.request import urlopen

#네이버 웹툰 > 신의 탑 제목 가져오자

if __name__ == '__main__':
    data = urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=183559&weekday=mon")
    soup = BeautifulSoup(data,"lxml")
    print(data)
    cartoon_titles = soup.find_all("td", attrs={'class':'title'})
    for title in cartoon_titles:
       t = title.find('a').text
       print(t)
    #다음 웹툰 > 어쩌다 발견한 7월
    # data = urlopen("http://webtoon.daum.net/webtoon/view/findjuly")
    # soup = BeautifulSoup(data,"lxml")
    # print(data)
    # cartoon_titles = soup.find_all("string", attrs={'class':'tit_wt'})
    # for title in cartoon_titles:
    #     print(t)