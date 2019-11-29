#다음 웹툰 > 어쩌다 발견한 7월
from urllib.request import urlopen
import json



if __name__ == '__main__':
    response = urlopen("http://webtoon.daum.net/data/pc/webtoon/view/findjuly")
    response_byte = response.read()
    response_json = json.loads(response_byte)
    #print(response_json['data']['webtoon'][ef'webtoonEpisodes'][11]['title'])
    cartoon_titles = response_json['data']['webtoon']['webtoonEpisodes']
    for item in cartoon_titles:
        title = item['title']
        thumbnail = item['thumbnailImage']['url']
        print(title)
        print(thumbnail)