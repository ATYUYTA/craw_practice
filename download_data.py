import requests
from bs4 import BeautifulSoup
import pandas



url='http://www.tse.com.tw/zh/page/trading/exchange/BWIBBU_d.html'
res=requests.get(url)
html=res.text.encode(res.encoding).decode()
soup=BeautifulSoup(html,'lxml')

a=soup.find('select',{'class':'board'})
