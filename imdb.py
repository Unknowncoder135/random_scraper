import bs4
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup 
import requests
import pandas as pd
import os
import wget
main_list = []
my_url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"


r = requests.get(my_url)
soup = BeautifulSoup(r.text,'html.parser')


mains  = soup.find_all('td',class_='titleColumn')
imgas = soup.find_all('td',class_='posterColumn')
rat  = soup.find_all('td',class_='ratingColumn imdbRating')
for name,img,rd in zip(mains,imgas,rat):
    # print(c.text)
    nam = name.find('a').text.strip()
    # print(nam)
    imh  = img.find('a').find('img')
    imh = imh['src']

    rating  = rd.text.strip()

    main_dir = {
        'movie_name':nam,
        'img_link':imh,
        'rating':rating,
            }
    main_list.append(main_dir)




df = pd.DataFrame(main_list)
print(df.head)
    