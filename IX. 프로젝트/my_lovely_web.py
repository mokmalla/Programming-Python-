#
from urllib.request import urlopen
from bs4 import BeautifulSoup

if __name__ == '__main__':
    with urlopen("https://www.youtube.com/user/AngrySmiile/videos") as response:
        soup = BeautifulSoup(response, "lxml")
    video_titles = soup.find_all("a",attrs={"class":"yt-uix-sessionlink yt-uix-tile-link spf-link yt-ui-ellipsis yt-ui-ellipsis-2"})
    video_shows = soup.find_all("ul", attrs={"class":"yt-lockup-meta-info"})


    print("머독 최신영상")
    for video_title in video_titles:
        print(video_title.text)
        # print(video_shows.text)

    for video_show in video_shows:
        print(video_show.text)