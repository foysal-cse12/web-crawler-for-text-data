# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 11:18:59 2020

@author: foysal
"""
import requests
from bs4 import BeautifulSoup
import re
import os
import random
import pandas as pd
import numpy as np




all_column = []
all_data = []
country = []
total_case = []
new_cases = []
total_death = []
new_death = []
total_recovered = []
active_cases = []
serious_case = []
total_case_1M_pop = []
death_1M_pop = []
total_test = []
test_1M_pop = []
continant = []
#cells = []
page = requests.get('https://www.worldometers.info/coronavirus/')

# =============================================================================
# craete a beautiful soup object out of that page.It will give a easy structure                    
# ============================================================================

soup = BeautifulSoup(page.content,'html.parser')

table = soup.find(id = 'main_table_countries_today')
#print(table)
thead = table.findAll('thead')
for thead in thead:
   column_name = thead.find_all('th')
   for th in column_name:
       #print(th.text)
       all_column.append(th.text)
print('all Column name: ',all_column)       


tbody = table.findAll('tbody')[0]   
#print('tbody: ',tbody) 
tr = tbody.find_all('tr',{ "class" : "" })
#print('tr: \n',tr)
for row in tr:
    cells =   row.find_all('td')
    #print(cells)
    for cell in cells:
        #print(cell.text)
        #all_data.append(cell.text.replace('+',''))
        #replacing unwanted character
        info = cell.text.replace('+','')
        info_ = info.replace(',','')
        all_data.append(info_)
            


#print('all data: \n',all_data)
#craete sublist from the list to separate each country information        
sub_list = [all_data[i:i+13] for i in range(0,len(all_data),13)]
#print('list: \n',sub_list)
# store individual information in a list from each country
country= [item[0] for item in sub_list]
total_case= [item[1] for item in sub_list]
#total_case = list(map(float, total_case))
#print(total_case)
new_cases= [item[2] for item in sub_list]
total_death= [item[3] for item in sub_list]
new_death= [item[4] for item in sub_list]
total_recovered= [item[5] for item in sub_list]
active_cases= [item[6] for item in sub_list]
serious_case= [item[7] for item in sub_list]
total_case_1M_pop= [item[8] for item in sub_list]
death_1M_pop= [item[9] for item in sub_list]
total_test= [item[10] for item in sub_list]
test_1M_pop= [item[11] for item in sub_list]
continant= [item[12] for item in sub_list]


all_info = pd.DataFrame(
        
            
            {
                    'Country': country,
                    'Total Cases':total_case,
                    'New Cases':new_cases,
                    'Total deaths':total_death,
                    'New deaths': new_death,
                    'Total Recovered':total_recovered,
                    'Active Cases':active_cases,   
                    'Srious/Critical Cases':serious_case, 
                    'Tot Cases/1M pop':total_case_1M_pop, 
                    'Deaths/ 1M pop':death_1M_pop,
                    'Total Tests':total_test, 
                    'Tests/ 1M pop':test_1M_pop, 
                    'Continant':continant,
                    
                    })

    
print(all_info)    

all_info.to_csv('corona_info.csv',index=False)
    
