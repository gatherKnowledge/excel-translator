import urllib3
from bs4 import BeautifulSoup

# 태그 제거
def html2text(html):
    soup = BeautifulSoup(html, "lxml")
    text_parts = soup.findAll(text=True)
    return ''.join(text_parts)

# 단어 검색 / TODO: req의 두번째 param은 네이버의 검색 url에 종속적이므로 따로 빼내는 편이 좋을 듯
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


