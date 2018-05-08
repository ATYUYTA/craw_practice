import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen, urljoin
import multiprocessing as mp

base_url='https://morvanzhou.github.io/'
count=0

def crawl(url):
    res=requests.get(url).text
    return res 

def parase(html):
    soup=BeautifulSoup(html,'lxml')
    title=soup.find_all('h1')[-1].get_text().strip()
    urls=soup.findAll('a',{"href": re.compile('^/.+?/$')})
#    for url in urls:
#        url_data.add(base_url+url['href'])
    url_data = set([urljoin(base_url, url['href']) for url in urls])
    url1=soup.findAll('meta',{'property':'og:url'})
    for i in url1:
        url=i['content']
    return url,title,url_data
    
unseen=set([base_url,])
seen=set()

if base_url != 'https://morvanzhou.github.io/':
    restricted_crawl = True
else:
    restricted_crawl = False

pool=mp.Pool(4)

while len(unseen) != 0:
    if restricted_crawl and len(seen)>20:
        break
    
    print('crawling...')
#    htmls=[crawl(url) for url in unseen]
    crawl_job=[pool.apply_async(crawl,args=(url,)) for url in unseen]
    htmls=[i.get() for i in crawl_job]
    
    print('parasing...')
#    result=[parase(html) for html in htmls]
    parase_job=[pool.apply_async(parase,args=(html,)) for html in htmls]
    result=[i.get() for i in parase_job]
    
    
    print('analysing...')
    seen.update(unseen)
    unseen.clear()
    
    for title,url,url_data in result:
        count+=1
        print(count ,title , url)
        unseen.update(url_data-seen)
   

        
    
    
    
    
    
