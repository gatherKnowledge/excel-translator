
# wb = Workbook()
# ws = wb.active
from openpyxl import Workbook, load_workbook
from bs4 import BeautifulSoup
import urllib3

wb = load_workbook('C:\\words.xlsx')
ws = wb.active
row1 = ws[1]
arr = list()

for  cell in row1 :
    ad = str(cell)
    v = str(cell.value)
    print('Adr : ' + ad + '\tvalue : ' + v )
    if (v != 'None') :
        # print(cell.column)
        arr.append(cell.column)

# 해당 열에 값이 존재
print(arr)

# list 요소의 배열 생성
def getRowArray(rn):
    print()
    rowArray = ws[rn]
    print(rowArray)
    return rowArray

# soup동작
def getDic(word):
    response = urllib3.
    return 'result'

def putValue(arr):
    spell = getAlphabet(arr[0][0:1])
    for idx, word in arr :
        ws[spell+idx] = getDic(word)

def getAlphabet(spell) :
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N']
    for idx, a in enumerate(alphabet):
        if spell == a :
            if idx+1 <= len(alphabet) :
                return alphabet[idx+1]

for e in arr :
    eachArray = getRowArray(e)
    # 데이터가 있는 첫번째 열
    for aE in eachArray :
        # print(aE.value)
        # print(aE.column)
        v = str(aE.value)
        if v != 'None' :
            print('v' + v )
            translated = getDic(v)
            targetRow = getAlphabet(aE.column)
            target = targetRow + str(aE.row)
            print('result : ' + target)
            ws[target] = translated
        else :
            break

wb.save('C:\\word_trans.xlsx')
        # ws1 = wb.create_sheet("mysheet")

# print(ws['B2'].value)
# wb.save("translated.xlsx")
"""
print(wb.get_active_sheet)
print(wb.get_sheet_names)
wb1 = Workbook()
wb1['A2'] = 2

print('-'*20)
print(wb1['A2'])
print(type(wb1) == type(wb))
"""
# for i in wb.get_sheet_names :
#     print(i['B2'])
# print(wb.get_sheet_names[0]['B2'])
# worksheet 이름
# sheets = wb.get_sheet_names()
# wb['A4'] = 4
# wb.save("translated.xlsx")


# print(wb.get_active_sheet['A4'])


# wb.save('C:\\after.xlsx')
# ws1 = wb.create_sheet("mysheet")

# otherWB = Workbook.load_workbook('myfilename.xlsx')
#
# ws1.title = "test_sheet_name"
# ws1['A4'] = 4
# c = ws1['A4']

# wb.save("translated.xlsx")