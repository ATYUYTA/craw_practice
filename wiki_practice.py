from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random

wiki="https://zh.wikipedia.org"
data=["/wiki/Wikipedia:%E9%A6%96%E9%A1%B5"]

for i in range(10): 
    url=wiki+data[-1]
    html=urlopen(url).read().decode('utf-8')
    soup=BeautifulSoup(html,features='lxml')
    print(i,soup.find('h1').get_text(),data[-1])
    result = soup.find_all("a", {"href": re.compile("^/wiki/%.{2}")})
    
    if result!=0:
        data.append(random.sample(result,5)[1]['href'])
    else:
        data.pop()





