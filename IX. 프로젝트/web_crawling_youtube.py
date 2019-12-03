#
#from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    url = "https://www.youtube.com/feed/trending"
    response = requests.post(url) #post 방식으로 request
    soup = BeautifulSoup(response.text, "lxml")

    #print(soup)
    youtube_titles = soup.find_all("a", attrs={"class":"yt-uix-tile-link"}) #주로 a태그, 주로 class로 찾으면 쉬움
    for youtube_title in youtube_titles:
        print(youtube_title.text)
        print(youtube_title["href"])    #youtube_title.get("href") 속성값 가져오는 방법