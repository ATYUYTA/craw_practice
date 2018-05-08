import requests
import webbrowser
from bs4 import BeautifulSoup

def catch_url(url,head):
    data=requests.get(url,headers=head)
    if data.status_code != 200:
        print('invaliblie!')
    else:
        return data.text

head01={'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
test01='https://www.google.com/search?tbm=fin&q=NYSE:+ARE&stick=H4sIAAAAAAAAAONgecRoyi3w8sc9YSmdSWtOXmNU4-IKzsgvd80rySypFJLgYoOy-KR4uLj0c_UNLMsKi8xNeQC193ywOgAAAA&sa=X&ved=0ahUKEwiCv8i267HaAhUIJ5QKHYwECbUQlq4CCDAwAA&biw=1344&bih=722#scso=uid_GczNWsf5A8at0ASf9KyQDw_5:0'
html=catch_url(test01,head01)

soup=BeautifulSoup(html,features='lxml')


company=soup.find('div',{'class':'PyJv1b kno-fb-ctx'}).text
print(company)
price=soup.findAll('div',{'class':'aviV4d'})[0].find('span').text
print(price)


