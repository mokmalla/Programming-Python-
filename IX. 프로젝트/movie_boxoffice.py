from urllib.request import urlopen
from bs4 import BeautifulSoup
if __name__ == '__main__':
    with urlopen("https://movie.daum.net/boxoffice/weekly") as response:
        soup = BeautifulSoup(response, "lxml")

    # print(soup)다
    movie_titles = soup.find_all("a", attrs={"class":"link_g"})
    print("다음 영화 박스오피스 주간")
    n = 1
    for movie_title in movie_titles[2:]:
        print(n, movie_title.text)
        n+=1

    with urlopen("https://search.naver.com/search.naver?where=nexearch&query=%EB%B0%95%EC%8A%A4%EC%98%A4%ED%94%BC%EC%8A%A4%20%ED%9D%A5%ED%96%89%EC%88%9C%EC%9C%84") as response:
        soup = BeautifulSoup(response, "lxml")
        #print(soup)

    print("\n네이버 영화 박스오피스")
    n = 1
    movie_titles_naver = soup.find_all("strong", attrs={"class":"_text"})
    for movie_title in movie_titles_naver[:10]:
        print(movie_title.text)
        n+=1