import requests
from bs4 import BeautifulSoup
 

url='http://www.ngchina.com.cn/animals/'
res=requests.get(url).text
soup=BeautifulSoup(res,'lxml')
img = soup.find_all('ul', {"class": "img_list"})

for i in img:
    imgs=i.find_all('img')
    for i in imgs:
        url=i['src']
        r=requests.get(url,stream=True)
        img_name=url.split('/')[-2]
        with open('./img/%s.jpg' % img_name, 'wb') as f:
            f.write(r.content)
        print('save %s'% img_name)
        

        
