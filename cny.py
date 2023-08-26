from bs4 import BeautifulSoup
import requests


url = "http://ru.investing.com/currencies/cny-rub"
page = requests.get(url)
filter = []
curs = []
soup = BeautifulSoup(page.text, 'html.parser')
filter = soup.findAll('span', class_='text-2xl')
for i in filter:
     curs.append(i.text)
for i in curs:
    print(i)


curs1 = (i.replace(',','.'))
cny = float(curs1)
print(cny)
CNY = cny + 1.5
print(CNY)
























# curs1 = (i.replace(',',''))
# l = list(curs1)
# int_lst = [int(x) for x in l]
# l1 = int_lst[:2]
# l2 = int_lst[2:]
# print(l2)
# firs_past = float(''.join(map(str, l1)))
# second_past = int(''.join(map(str, l2)))
# if '0' in l2[0]:
#     second_past2 = '0.' + second_past
# wtf = float(str(0) + '.' + str(second_past))
# CNY = firs_past + wtf + 1.5
# print(CNY)
# print(second_past)
# print(l2)
# print(wtf)
