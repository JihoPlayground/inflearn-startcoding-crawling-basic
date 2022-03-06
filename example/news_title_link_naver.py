"""
네이버에서 검색된 뉴스 타이틀과 링크 크롤링
"""

import requests
from bs4 import BeautifulSoup

def main():
    """
    네이버에서 keyword에 해당하는 관련도순 뉴스 정보를 아마도 10개 가져온다.
    """

    keyword = "삼성전자"
    host = 'https://search.naver.com'
    uri = '/search.naver'
    query_string = f'?where=news&sm=tab_jum&query={keyword}'
    url = f'{host}{uri}{query_string}'
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
