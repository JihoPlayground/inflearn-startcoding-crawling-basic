"""
BeautifulSoup4 Example

- HTML Parser 정도의 역할을 수행
- JS의 querySelector처럼 접근해서 특정 HTML 엘리먼트 접근 가능
"""

import requests
from bs4 import BeautifulSoup

def main():
    """
    Main Function
    """
    response = requests.get("https://www.naver.com")
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    word = soup.select_one('#NM_set_home_btn')
    print(word)

if __name__ == "__main__":
    main()
