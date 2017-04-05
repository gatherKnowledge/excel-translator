엑셀파일 단어 서치 프로그램(파이썬) 사용법 정리 

Name: urllib3
Version: 1.20
Summary: HTTP library with thread-safe connection pooling, file post, and more.
Home-page: https://urllib3.readthedocs.io/
Author: Andrey Petrov
Author-email: andrey.petrov@shazow.net
License: MIT
Location: C:\..\appdata\local\programs\python\python36\lib\site-packages
Requires:


Name: openpyxl
Version: 2.4.2
Summary: A Python library to read/write Excel 2010 xlsx/xlsm files
Home-page: http://openpyxl.readthedocs.org
Author: See AUTHORS
Author-email: eric.gazoni@gmail.com
License: MIT/Expat
Location: C:\..\appdata\local\programs\python\python36\lib\site-packages
Requires: jdcal, et-xmlfile

Name: beautifulsoup4
Version: 4.5.0
Summary: Screen-scraping library
Home-page: http://www.crummy.com/software/BeautifulSoup/bs4/
Author: Leonard Richardson
Author-email: leonardr@segfault.org
License: MIT
Location: C:\..\appdata\local\programs\python\python36\lib\site-packages\beautifulsoup4-4.5.0-py3.6.egg
Requires:

python version : 3.6
==> pip install [package명]로 전부 설치 가능
위에 설치 된 라이브러리 정보 보는 방법 
==> pip show [...]



1. openpyxl
  - 엑셀파일에 대해 파이썬 환경에서 동작시킬 수 있고 윈도우, 엑셀이 설치돼있지 않아도 동작시킬 수 있는 신뢰성 높은 파이썬 라이브러리
  (1) 선행작업
    a. 최소한의 워크시트가 존재해야한다.
     - workbook에 대한 생성/로드 후 workbook.active
    b. 워크시트 생성 작업
>>> ws1 = wb.create_sheet("Mysheet") # insert at the end (default)
or
>>> ws2 = wb.create_sheet("Mysheet", 0) # insert at first position
--> 시트 명명과 함께 active하지 않고 바로 사용 할 수 있을 듯, 확인

  (2) 셀에 대한 조작
    a. 열/행에 대한 조작
>>> cell_range = ws['A1' : 'C2']
>>> colC = ws['C']
>>> col_range = ws['C:D']
>>> row10 = ws[10]
>>> row_range = ws[5:10]

ws[1] --> 1행에 있는 모든 것을 튜플로 정의
ws['A'] --> A열의 모든 데이터 튜플로 정의

>>> print(wb2.get_sheet_names())
['Sheet2', 'New Title', 'Sheet1']
# 해당 워크 북의 시트명 튜플로 호출


    b. 각 셀에 대한 조작
ws['X1'] --> 셀 지정.
ex)
for cell in row :
    print(cell)
    print(cell.row)
    print(cell.column)
    print(cell.value)

  (3) 파일에 대한 접근 및 로드, 저장
    a. save메서드 이용
openpyxl.workbook.Workbook.save() method of the openpyxl.workbook.Workbook object

    b. loading from file 
>>> from openpyxl import load_workbook
>>> wb = load_workbook(filename = 'empty_book.xlsx')

  (4) 기타
    - worksheet가 메모리에 생성됐다고 하더라도 셀이 존재하는 것이 아니므로 해당 셀에 대한 첫 접근은 생성하는 작업이 우선적으로 필요하다.
2. urllib3
 - 강력한 파이썬 http클라이언트 라이브러리로 이미 많은 파이썬 생태계에서 사용되고 있다.
 
Thread safety.
Connection pooling.
Client-side SSL/TLS verification.
File uploads with multipart encoding.
Helpers for retrying requests and dealing with HTTP redirects.
Support for gzip and deflate encoding.
Proxy support for HTTP and SOCKS.
100% test coverage.
source : https://urllib3.readthedocs.io/en/latest/
 - urllib3.PoolManager, urllib의 기본 obj
r = urllib3.PoolManager.request(
    ['GET'|'POST'],
    url).data --> url html 전체 소스를 얻을 수 있고 다른 추가 옵션 설정 가능 , 자세한 내용은 공식 페이지 참고

3. BeautifulSoup4
 - html과 xml형태의 데이터를 입맛에 맞게 조작할 수 있게 해주는 파싱라이브러리, Jquery셀렉트 태그 사용법과 연관이 있다. 참고로 현재 BeautifulSoup3의 개발은 중단됐고 4만 개발중이다 
 - BeautifulSoup3와 BeautifulSoup4의 차이를 알고 싶다면 https://www.crummy.com/software/BeautifulSoup/bs4/doc/#porting-code-to-bs4로 들어가면 되겠다.
 (1) 공식문서 링크 
  - https://www.crummy.com/software/BeautifulSoup/bs4/doc/
 (2) urllib3와의 활용
# urllib3의 request와 함께 사용
r = urllib3.PoolManager.request()

soup = BeautifulSoup(r.data, 'html.parser') 
# soup = BeautifulSoup(url, 'html.parser') 
soup.prettify() --> 불러들인 html요소 정렬

# 요소 찾기
soup.find("dl", attrs={"class": "dic_search_result"})
# --> dl 태그의 class명이 dic..찾기


