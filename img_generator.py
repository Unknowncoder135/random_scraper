import bs4
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup 
import requests
import os
import wget
my_url = 'https://www.imdb.com/list/ls053501318/'
#opening up connection, downloading the page
# imdb = urlopen(my_url)

r = requests.get(my_url)
soup = BeautifulSoup(r.text,'html.parser')

containers =soup.findAll('div',{'class':'lister-item mode-detail'})
pic = soup.findAll('img')
# mains = soup.find_all('h3',class_='lister-item-header')
# for x in mains:
#     name  = x.find('a').text.strip()
#     print(name)
path = os.getcwd()
path = os.path.join(path,'okkss')


os.mkdir(path)
print(path)

for container,img in zip(containers,pic):
    name = container.h3.a.text.strip()
    image = img.get('src')
    fullname = str(name) + '.jpg'
    save = os.path.join(path,fullname)
    wget.download(image,save)
    # print(name,image)


