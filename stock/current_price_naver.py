'''
네이버 금융에서 주식 정보 크롤링
'''

import requests
from bs4 import BeautifulSoup

class Stock:
    '''
    주식 정보 클래스
    '''
    def __init__(self, code: str, name: str) -> None:
        self.code = code
        self.name = name
        self.price = 0
    def set_price(self, price: str) -> None:
        '''
        입력받은 price 문자열에서 쉼표를 떼고 정수로 저장
        '''
        self.price = int(price.replace(',', ''))
    def __str__(self) -> str:
        return f'{self.code} {self.name} {self.price} 원'

def main():
    '''
    원하는 주식들의 코드로 현재가를 구함
    '''
    stock_list = [
        Stock('005930', '삼성전자'),
        Stock('000660', 'SK하이닉스'),
        Stock('035720', '카카오')
    ]

    for stock in stock_list:
        stock.set_price(get_current_price(stock.code))

    for stock in stock_list:
        print(stock)


def get_current_price(code: str):
    # type: (str) -> str
    '''
    실제 HTTP 요청을 통해 현재가 크롤링 하는 부분
    '''
    host = 'https://finance.naver.com'
    uri = '/item/sise.naver'
    url = f'{host}{uri}?code={code}'

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    return soup.select_one('#_nowVal').text


if __name__ == '__main__':
    main()
