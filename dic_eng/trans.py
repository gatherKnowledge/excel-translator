from bs4 import BeautifulSoup
import requests

def spider():
    url = "http://www.naver.com"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'lxml')

spider(1)