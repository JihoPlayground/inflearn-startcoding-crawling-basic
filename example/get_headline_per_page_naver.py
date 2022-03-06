"""
여러 검색 결과 페이지에서 헤드라인 가져오기
"""

import requests
from bs4 import BeautifulSoup

def main():
    """
    네이버에서 keyword에 해당하는 관련도순 뉴스 정보를 last_page까지 가져온다.
    페이지 당 10개 뉴스
    """

    keyword = "삼성전자"
    host = 'https://search.naver.com'
    uri = '/search.naver'

    last_page: int = 10
    limit: int = (last_page << 3) + (last_page << 1) # limit = last_page * 10

    for i in range(1, limit, 10):
        query_string = f'?where=news&sm=tab_jum&query={keyword}&start={i}'
        url = f'{host}{uri}{query_string}'
        get_headline(url)

def get_headline(url):
    # type: (str) -> None
    """
    뉴스 타이틀과 원본 링크 파싱 후 출력
    args : url 크롤링 할 URL
    """
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    news_list = soup.select('.news_tit')

    for news in news_list:
        title = news.text
        link = news.attrs['href']
        print([title, link])

if __name__ == "__main__":
    main()
