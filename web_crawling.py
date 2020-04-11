# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 12:40:53 2020

@author: foysal
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

def page_control(max_pages):
    
# =============================================================================
#     column_names = ["Book Name", "Price"]
#     df = pd.DataFrame(columns = column_names)
# =============================================================================
    
    price_list= []
    book_list=[]
    book_name=[]
    price=[]
    current_page= 1
    while(current_page<=max_pages):
        base_url = 'http://books.toscrape.com/'
        url = 'http://books.toscrape.com/catalogue/page-'+str(current_page)+'.html'
        #print(url)
        #single_page_info(base_url,url,current_page)
        book_name,price= single_page_info(base_url,url,current_page)
        #print(p)
        #ap.append(price)# it makes sublist because price is already a list
        price_list.extend(price)
        #print(price_list)
        book_list.extend(book_name)
        #print(book_list)

        current_page = current_page+1 
        
    df= pd.DataFrame({'Book Name ':book_list,'Price ': price_list})
    print(df)
    df.to_csv('book.csv',index=False)
def single_page_info(base_url,url,current_page):
    books_name= []
    book_name= []
    prices = []
    stocks = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    
    #for finding one book url
    all_book_info = soup.find('ol', class_ = 'row')
    #there are multiple li container where class = col-xs-6 col-sm-4 col-md-3 col-lg-3. we need to find all
    single_book = all_book_info.findAll('li',class_ = 'col-xs-6 col-sm-4 col-md-3 col-lg-3')
    
    #print(single_book)
# =============================================================================
#      each li container where class = 'col-xs-6 col-sm-4 col-md-3 col-lg-3' carries individual book information
#      all book information is under article conatiner where class = 'product_pod'. Under the article container we 
#      can find different tag where specific book informartion is available
# =============================================================================
     
    for infos in single_book:
        #find all book name.......................
        #book_name = [info.find[].get_text() for info in infos]
        book_name = infos.find("article", class_ = "product_pod").div.a.img.get('alt')
        #book_name = [x.div.a.img.get('alt') for x in infos.findAll("article", class_ = "product_pod")]
        books_name.append(book_name)
        #print(str(len(book_name)) + " book_name")
        #print("One example:")
        #print(book_name)
        
        #find all price.................................
        find_prices_stocks = infos.find("article", class_ = "product_pod")
        price = find_prices_stocks.find("p", class_ = "price_color").get_text().replace('£','')
        prices.append(price)
        #stock = find_prices_stocks.find("p", class_ = "instock availability").get_text().replace('\n','')
        #stocks.append(stock)
    return books_name,prices
    #print(books_name)
    #print(prices)
    #print(stocks)
  


page_control(4)        
    