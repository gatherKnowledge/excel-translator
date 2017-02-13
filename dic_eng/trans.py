import urllib3
from bs4 import BeautifulSoup

def html2text(html):
    soup = BeautifulSoup(html, "lxml")
    text_parts = soup.findAll(text=True)
    return ''.join(text_parts)

def trans(word) :
    http = urllib3.PoolManager()
    r = http.request(
         'POST',
         'http://dic.naver.com/search.nhn?dicQuery='+word+'&query='+word+'&target=dic&ie=utf8&query_utf=&isOnlyViewEE=')
    soup = BeautifulSoup(r.data, 'html.parser')
    print(type(soup))
    # soup.find_all("a")
    f1 = soup.find_all("dl", attrs={"class": "dic_search_result"})
    print("*"*50)
    rs = html2text(str(f1))
    print(rs)
    print("*"*50)
    return rs



# soup2 = BeautifulSoup(str(f1), 'html.parser')
# print(type(soup2))
#
# f2 = soup.find_all("span", attrs={"class" : "blind"})
# print(f2)
# print(soup.prettify())

