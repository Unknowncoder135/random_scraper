import csv
# import xlsx
import time
import os
import pandas as pd
from bs4 import BeautifulSoup
import json
import requests

from bs4 import BeautifulSoup
import requests
import time
import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
# LAZADA SCRIPT................................................................
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait



main_lisu = []
df = pd.DataFrame({ 'Sl. No':[''],'Product link':[''],'or_price':[''],
                    'final_p':[''],
                    'Handle': [''], 'Title': [''], 'Body (HTML)': [''], 'Vendor': [''], 'Standard Product Type':[''],'Published':[''],
                            'Option1 Name': [''], 'Option1 Value': [''],
                            'Option2 Name': [''], 'Option2 Value': [''],
                            
                            'Variant Grams':[''],
                            'Variant Inventory Tracker':[''],
                            'Variant Inventory Qty':[''],
                            'Variant Inventory Policy':[''],
                            'Variant Fulfillment Service':[''],
                            
                            'Variant Requires Shipping':[''],
                            'Variant Taxable':[''], 'Image Src': [''], 'Image Position': [''],'Image Alt Text':[''],
                            'Gift Card':[''],
                            'Status': [''],})
headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }
driver = webdriver.Chrome()
# //*[@id="content"]/div/div[1]/div/div[3]/div[2]/div[2]/div[6]/div/div/div/ul/li[1]/div/a

main_url = 'https://www.etsy.com/in-en/c/jewelry/necklaces?ref=pagination&explicit=1&page=2'

main_lisu.append('https://www.etsy.com/listing/107157219/name-necklace-personalized-name-plate?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=sr_gallery-1-1&frs=1')
main_lisu.append('https://www.etsy.com/listing/1053284660/christmas-gifts-for-mom-combined-birth?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=sc_gallery-1-2&plkey=c485c219f9f2df0af2d2a7763075165c4e84af88%3A1053284660&frs=1&bes=1&col=1')
main_lisu.append('https://www.etsy.com/listing/959627059/personalized-name-necklace-14k-gold-name?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=sc_gallery-1-3&plkey=0081b479d8fac7116790d12294ba66ac6ac36081%3A959627059&pro=1&frs=1')
main_lisu.append('https://www.etsy.com/listing/952063887/angel-wings-necklace-wings-name-necklace?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=sc_gallery-1-4&plkey=368ed6bbbce1dda4dbaea1728ef8200085c99099%3A952063887&pro=1&frs=1&col=1')
main_lisu.append('https://www.etsy.com/listing/463812221/rose-gold-dainty-double-multicolor?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=sr_gallery-1-2&etp=1&col=1')


counter = 0
for x in main_lisu:
    url = x
    counter = counter + 1
    driver.get(x)
    time.sleep(3)
    r = requests.get(x,headers=headers)
    soup = BeautifulSoup(r.text,'html.parser')
    try:
        name = driver.find_element_by_id('listing-title-small').text
    except:
        try:
            name = driver.find_element_by_xpath('//*[@id="listing-title-small"]').text
        except:
            try:
                name = soup.find('h1',class_='wt-text-body-01 wt-text-left-xs wt-line-height-tight wt-break-word wt-text-truncate--multi-line').text
            except:
                name ='nn'
    print(name)
    hend = name.strip()
    hend  = hend.replace(' ','-')
    hend = hend.lower()
    hendle = hend[0:12] 
    hands =  f'{hendle}-{counter}'
    print(hands)
    
    # name = soup.find('h1',{'id':'listing-title-small'}).text
    # try:
    #     original_price = soup.find('p',class_='wt-text-strikethrough wt-text-caption wt-text-gray wt-mr-xs-1').text
    # except:
    #     original_price = 'nn'
    # try:
    #     final_price = soup.find('p',class_='wt-text-title-03 wt-mr-xs-2').text
    # except:
    #     final_price = 'nn'

    try:
        venor = driver.find_element_by_xpath('//*[@id="listing-page-cart"]/div[1]/div/p/a/span').text
    except:
        venor = 'nn'

    try:
        cliker = driver.find_element_by_css_selector('.wt-btn wt-btn--transparent.wt-btn--small.wt-content-toggle--btn')
        cliker.click()
        time.sleep(1)
    except:
        pass
    try:
        description = driver.find_element_by_xpath('//*[@id="wt-content-toggle-product-details-read-more"]/p').text
    except:
        description = 'nn'
    # print(name,original_price,final_price,venor)

    img = []
    try:
        for xx in range(1,15):                  
            try:
                ig = driver.find_element_by_xpath(f'//*[@id="listing-right-column"]/div/div[1]/div[1]/div/div/div/div/div[2]/div[3]/ul/li[{xx}]/img')
                tem = ig.get_attribute('src')
                img.append(tem)
            except:
                pass
    except:
        print('done')
        pass
    print(len(img))
    size = []
    try:
        ma = driver.find_element_by_id("inventory-variation-select-0")
        drp = Select(ma)
        lens = drp.options
        
        for x in lens:
            ss = x.text
            size.append(ss)
        # size = size[1:]
        # print(size)
    except:
        size = "Not Found"
    # print(size)
    color = []
    try:
        ma = driver.find_element_by_id("inventory-variation-select-1")
        drp = Select(ma)
        lens = drp.options
        
        for x in lens:
            ss = x.text
            color.append(ss)
        # color = color[1:]
        # print(size)
    except:
        color = "Not Found"
    # print(color)
    try:
        lable_1 = driver.find_element_by_xpath('//*[@id="variations"]/div/div[1]/label').text
    except:
        lable_1 = "Not Found"
    try:
        lable_2  = driver.find_element_by_xpath('//*[@id="variations"]/div/div[2]/label').text
    except:
        lable_2 = 'Not Found'
    print(lable_2)
   
    mainss = driver.find_elements_by_css_selector('.wt-validation.wt-mb-xs-2')
    print(len(mainss))
    vv = -1
    img_co = 0
    if len(mainss) == 2:
       
        for v in range(1,len(size)):
            for r in range(1,len(color)):
                vv = vv + 1
                print(vv)
                if size != 'Not Found':
                    sizu = driver.find_element_by_id("inventory-variation-select-0")
                    drp  = Select(sizu)
                    drp.select_by_index(v)
                    time.sleep(2)
                if color != "Not Found":
                    calu = driver.find_element_by_id("inventory-variation-select-1")
                    kks  = Select(calu)
                    kks.select_by_index(r)
                    time.sleep(3)
                try:                                        
                    op_price = driver.find_element_by_xpath('//*[@id="listing-page-cart"]/div[3]/div[1]/div[1]/div/div[1]/p[2]').text
                    op_price = op_price.strip()
                    op_price = op_price.replace('Original Price:','')
                    ops = op_price.replace('US$','')
                    mms  = op_price.replace('\nUS$ ','')
                    print(op_price)
                except:
                    mms = ''
                
                # print(mms)
                # print(ops)
                prices = driver.find_element_by_xpath('//*[@id="listing-page-cart"]/div[3]/div[1]/div[1]/div/div[1]/p').text
                prices = prices.strip()
                prices = prices.replace('Price:','')
                pps = prices.replace('US$ ','')
                kss = pps.replace('\n','')
                print(kss)

                # try:
                #     op_price = driver.find_element_by_xpath('//*[@id="listing-page-cart"]/div[3]/div[1]/div[1]/div/div[1]/p[2]').text
                #     op_price = op_price.replace('Original Price:','')
                #     op_price = op_price.replace('US$','')
                #     print(op_price)
                # except:
                #     op_price = ''
                
                # prices = driver.find_element_by_xpath('//*[@id="listing-page-cart"]/div[3]/div[1]/div[1]/div/div[1]/p').text
                # prices = prices.replace('Price:','')
                # prices = prices.replace('US$ ','')
                # print(prices)
                # if lable_2 =='Add your personalisation':
                #     lable_2 = ''
                #     ccc = ''
                # else:
                ccc = color[r]
                try:
                    igs = img[vv]
                    img_co = img_co +1
                except:
                    igs = ''
                    img_co = ''
                if vv == 0:
                    df = df.append({'Sl. No': counter,
                                    'Product link':url,
                                    'or_price':mms,
                                    'final_p':kss,
                                    'Handle': hands,
                                    'Title': name,
                                    'Body (HTML)': description,
                                    'Vendor': venor, 
                                    'Standard Product Type':'Apparel & Accessories > Handbag & Wallet Accessories',
                                    'Published':'TRUE',
                                    'Option1 Name':lable_1,
                                    'Option1 Value':size[v],
                                    'Option2 Name':lable_2,
                                    'Option2 Value':ccc,
                                    'Variant Grams':'1000',
                                    'Variant Inventory Tracker':'shopify',
                                    'Variant Inventory Qty':'10',
                                    'Variant Inventory Policy':'continue',
                                    'Variant Fulfillment Service':'manual',
                                    'Variant Requires Shipping':'TRUE',
                                    'Variant Taxable':'TRUE',
                                    'Image Src':igs,
                                    'Image Position':img_co,
                                    'Image Alt Text':'',
                                    'Gift Card':'FALSE',
                                    'Status': 'active',
                                    },ignore_index=True)
                else:
                    df = df.append({'Sl. No': '',
                                    'Product link':'',
                                    'or_price':mms,
                                    'final_p':kss,
                                    'Handle': hands,
                                    'Title': name,
                                    'Body (HTML)': description,
                                    'Vendor': venor, 
                                    'Standard Product Type':'Apparel & Accessories > Handbag & Wallet Accessories',
                                    'Published':'TRUE',
                                    'Option1 Name':lable_1,
                                    'Option1 Value':size[v],
                                    'Option2 Name':lable_2,
                                    'Option2 Value':ccc,
                                    'Variant Grams':'1000',
                                    'Variant Inventory Tracker':'shopify',
                                    'Variant Inventory Qty':'10',
                                    'Variant Inventory Policy':'continue',
                                    'Variant Fulfillment Service':'manual',
                                    'Variant Requires Shipping':'TRUE',
                                    'Variant Taxable':'TRUE',
                                    'Image Src':igs,
                                    'Image Position':img_co,
                                    'Image Alt Text':'',
                                    'Gift Card':'FALSE',
                                    'Status': 'active',
                                    },ignore_index=True)
                print(df)
    elif len(mainss) == 1:
        print("don")
        lable_2 = ''
        ccc =''
        for cv in range(1,len(size)):
            vv =vv + 1
            sizu = driver.find_element_by_id("inventory-variation-select-0")
            drp  = Select(sizu)
            drp.select_by_index(cv)
            time.sleep(3)
            try:                                        
                op_price = driver.find_element_by_xpath('//*[@id="listing-page-cart"]/div[3]/div[1]/div[1]/div/div[1]/p[2]').text
                op_price = op_price.strip()
                op_price = op_price.replace('Original Price:','')
                ops = op_price.replace('US$','')
                mms  = op_price.replace('\nUS$ ','')
                print(op_price)

            except:
                mms = ''
            
            
            prices = driver.find_element_by_xpath('//*[@id="listing-page-cart"]/div[3]/div[1]/div[1]/div/div[1]/p').text
            prices = prices.strip()
            prices = prices.replace('Price:','')
            pps = prices.replace('US$ ','')
            kss = pps.replace('\n','')
            print(kss)

            print(pps)
            try:
                igs = img[vv]
                img_co = img_co +1
            except:
                igs = ''
                img_co = ''
            if cv ==1:
                 df = df.append({
                                'Sl. No':counter,
                                'Product link':url,
                                'or_price':mms,
                                'final_p':kss,
                                'Handle': hands,
                                'Title': name,
                                'Body (HTML)': description,
                                'Vendor': venor, 
                                'Standard Product Type':'Apparel & Accessories > Handbag & Wallet Accessories',
                                'Published':'TRUE',
                                'Option1 Name':lable_1,
                                'Option1 Value':size[cv],
                                'Option2 Name':lable_2,
                                'Option2 Value':ccc,
                                
                                
                                'Variant Grams':'1000',
                                'Variant Inventory Tracker':'shopify',
                                'Variant Inventory Qty':'10',
                                'Variant Inventory Policy':'continue',
                                'Variant Fulfillment Service':'manual',
                                
                                'Variant Requires Shipping':'TRUE',
                                'Variant Taxable':'TRUE',
                                'Image Src':igs,
                                'Image Position':img_co,
                                'Image Alt Text':'',
                                'Gift Card':'FALSE',
                                'Status': 'active',
                                },ignore_index=True)
            else:
                df = df.append({   
                                'Sl. No':'',
                                'Product link':'',
                                'or_price':mms,
                                'final_p':kss,
                                'Handle': hands,
                                'Title': name,
                                'Body (HTML)': description,
                                'Vendor': venor, 
                                'Standard Product Type':'Apparel & Accessories > Handbag & Wallet Accessories',
                                'Published':'TRUE',
                                'Option1 Name':lable_1,
                                'Option1 Value':size[cv],
                                'Option2 Name':lable_2,
                                'Option2 Value':ccc,
                                
                                
                                'Variant Grams':'1000',
                                'Variant Inventory Tracker':'shopify',
                                'Variant Inventory Qty':'10',
                                'Variant Inventory Policy':'continue',
                                'Variant Fulfillment Service':'manual',
                                
                                'Variant Requires Shipping':'TRUE',
                                'Variant Taxable':'TRUE',
                                'Image Src':igs,
                                'Image Position':img_co,
                                'Image Alt Text':'',
                                'Gift Card':'FALSE',
                                'Status': 'active',
                                },ignore_index=True)
            print(df)


            
                            
            



df.to_csv('bas_hoooo.csv', index=False)
print("script run successfully")

        







    