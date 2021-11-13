
import csv
import json
import os
import time
from sys import version

import pandas as pd
import requests
from bs4 import BeautifulSoup, SoupStrainer
from requests_html import HTMLSession

df = pd.read_csv('okk.csv')

month = df['hiren'].tolist()

# print(month[0])

print(len(month))
counter = 1
df = pd.DataFrame({'Handle': [''], 'Title': [''], 'Body (HTML)': [''], 'Vendor': [
                  ''], 'Standard Product Type': [''], 'Published': [''],
    'Variant Grams': [''],
    'Variant Inventory Tracker': [''],
    'Variant Inventory Qty': [''],
    'Variant Inventory Policy': [''],
    'Variant Fulfillment Service': [''],
    'Variant Price': [''],
    'Variant Requires Shipping': [''],
    'Variant Taxable': [''], 'Image Src': [''], 'Image Position': [''], 'Image Alt Text': [''],
    'Gift Card': [''],
    'Status': [''], })


for x in range(0, len(month)):
    url = month[x]
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    try:
        name = soup.find(
            'p', class_='Text-uqn6ov-0 Text__H0-uqn6ov-1 ItemInfo__Heading-ijvfho-2 enHgUe').text
    except:
        continue
    hendel = name.lower()
    hendel = hendel.replace(' ', '-')
    hendel1 = f'{hendel}-{counter}'
    counter = counter + 1
    print(hendel)
    print(name)
    description = soup.find(
        'p', class_='Text-uqn6ov-0 Text__T2-uqn6ov-10 Spec__Description-sc-1oxis5o-2 eNOzrJ')
    print(description)
    price = soup.find(
        'p', class_='Text-uqn6ov-0 Text__H0-uqn6ov-1 bfDrkK').text

    no_su_thay = soup.find(
        'div', class_='Flex-ych44r-0 Space-cutht5-0 Container-sc-9aa7mx-0 PhotoIndicatorsRevamp__FilmStripWrapper-sc-97b0h4-7 PhotoIndicatorsRevamp__FilmStripWrapperAdapt-sc-97b0h4-12 jZnHGO')
    images = no_su_thay.find_all(
        'img', class_='Image-sc-172fqpb-1 Image__ImageWithWidth-sc-172fqpb-4 bSkUgQ')
    img = []
    for x in images:
        imgs = x['src']
        print(imgs)
        img.append(imgs)
    vendor = soup.find(
        'a', class_='Text__LinkText-sc-1e98qiv-0-a Link__StyledAnchor-dkjuk2-0 fiIUU Link__StyledPlainLink-dkjuk2-3 ciLNld ItemInfo__H4PlainLink-ijvfho-1 dgTblj').text
    print(vendor)
    name0 = f'{name}(small)'
    name1 = f'{name}(medium)'
    name2 = f'{name}(large)'
    hend = hendel1
    img_co = 1
    for vv in range(0, len(img)):

        # if vv==0:
        #     names = name0
        #     kk = 'small'
        # elif vv==1:
        #     names = name1
        #     kk = 'medium'
        # elif vv==2:
        #     names = name2
        #     kk = 'large'
        # else:
        #     kk =''


        if vv == 0:
            df = df.append({'Handle': hend,
                            'Title': name,
                            'Body (HTML)': description,
                            'Vendor': vendor,
                            'Standard Product Type': '',
                            'Published': 'TRUE',
                            'Variant Grams': '1000',
                            'Variant Inventory Tracker': 'shopify',
                            'Variant Inventory Qty': '10',
                            'Variant Inventory Policy': 'continue',
                            'Variant Fulfillment Service': 'manual',
                            'Variant Price': price,
                            'Variant Requires Shipping': 'TRUE',
                            'Variant Taxable': 'TRUE',
                            'Image Src': img[vv],
                            'Image Position': img_co,
                            'Image Alt Text': '',
                            'Gift Card': 'FALSE',
                            'Status': 'active',
                            }, ignore_index=True)


        else:
            df = df.append({'Handle': hend,
                            'Title': name,
                            'Body (HTML)': '',
                            'Vendor': '',
                            'Standard Product Type': '',
                            'Published': '',
                            'Variant Grams': '',
                            'Variant Inventory Tracker': '',
                            'Variant Inventory Qty': '',
                            'Variant Inventory Policy': '',
                            'Variant Fulfillment Service': '',
                            'Variant Price': '',
                            'Variant Requires Shipping': '',
                            'Variant Taxable': '',
                            'Image Src': img[vv],
                            'Image Position': img_co,
                            'Image Alt Text': '',
                            'Gift Card': '',
                            'Status': '',
                            }, ignore_index=True)

        img_co = img_co+1
        # print(df)

    print('product', counter)
    # if counter == 10:
    #     break


df.to_csv('jay_ho.csv', index=False)
print("script run successfully")
