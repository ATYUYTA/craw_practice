import requests
from bs4 import BeautifulSoup

url='http://www.ngchina.com.cn/index.php?m=content&c=index&a=lists&catid=596'
r=requests.get(url).text
soup=BeautifulSoup(r,'lxml')
img_url=soup.findAll('div',{'class':'showImg-list'})
for i in img_url:
    img_url1=i.findAll('dl')
    for i in img_url1:
        img_url2=i.findAll('img',{'height':'288'})
        for i in img_url2:
            url=i['src']
            r=requests.get(url)
            img_name=url.split('/')[-1]
            with open ('./img/%s' % img_name , 'wb') as f:
                f.write(r.content)
            print('save %s'%img_name)

                

