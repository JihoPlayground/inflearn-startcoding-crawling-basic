"""
requests Example

- 해당 도메인 주소의 HTML 파일을 읽어올 수 있다.
"""

import requests

def main():
    """
    Main Function
    """
    response = requests.get("https://www.naver.com")
    html = response.text
    print(html)

if __name__ == "__main__":
    main()
