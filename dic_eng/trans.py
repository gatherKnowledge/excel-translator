import urllib3
from bs4 import BeautifulSoup

# 태그 제거
def html2text(html):
    soup = BeautifulSoup(html, "lxml")
    text_parts = soup.findAll(text=True)
    return ''.join(text_parts)

# 단어 검색
def trans(word) :
    http = urllib3.PoolManager()
    r = http.request(
         'POST',
         'http://dic.naver.com/search.nhn?dicQuery='+word+'&query='+word+'&target=dic&ie=utf8&query_utf=&isOnlyViewEE=')
    soup = BeautifulSoup(r.data, 'html.parser')
    print(type(soup))
    # soup.find_all("a")
    f1 = soup.find_all("dl", attrs={"class": "dic_search_result"})
    rs = html2text(str(f1))
    print("#### 결과 확인 ####")
    print("*"*100)
    print(rs)
    print("*"*100)
    return rs


