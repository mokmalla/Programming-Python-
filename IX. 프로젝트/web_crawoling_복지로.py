from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    url = "http://bokjiro.go.kr/welInfo/retrieveWelInfoBoxList.do"
    data = {"searchIntClId":"05", "pageUnit":"300"}
    with requests.post(url, data) as response:
        soup = BeautifulSoup(response.text, "lxml")

    # print(soup)
    titles = soup.select("dt.tit > a")
    i = 1
    for title in titles:
        print(i," ",title.text)
        i +=1