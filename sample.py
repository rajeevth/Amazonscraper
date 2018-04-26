# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 21:31:56 2018

@author: rajeev
"""

# -*- coding: utf-8 -*-
"""
Spyder 
This is a category URl page that extracts all products url of that ctategory 
and stores in DB subsequent run of thiese URLS  will extract the each and every detail of the product 
This is a temporary script file.
"""

# import required libraries
# bs4 import BeautifulSoup for scrapping basuc functions
# import requests and HTTP library for handling request response
# import cx_Oracle for Oracle connection

import requests 
import sys
from bs4 import BeautifulSoup
from time import sleep
import cx_Oracle
import re
import lxml

#function to scrap and havde a list of url for th efirst page 
def scrapthis():
        con = cx_Oracle.connect('steven/admin@//localhost:1521/oracle') 
        cursor = con.cursor()
        print('Starting the program')
        r = requests.get('https://www.amazon.in/s/ref=mega_elec_s23_2_1_1_1?rh=i%3Acomputers%2Cn%3A1375424031&ie=UTF8&bbn=976392031')
        soup = BeautifulSoup(r.content, 'lxml')
        print(soup)
        li_list  = soup.find('div',id= "mainResults").find('ul')

        for tag in li_list:
            a=tag.find_all('a')
            #print('**********')
            for link  in a:
                #print(length(link))
                prdlnk = link.get('href')
                URLlst.append(prdlnk)              
        print("Program Ends here" )
        urlset = set(URLlst)
        for allset in urlset:
            querystring = "Insert into AMAZON_OUTPUT_TUPLES(URL) values("+"'"+allset+"'"+")"
            cursor.execute(querystring)
            cursor.execute('commit') 
scrapthis()
#call function with url          
#scrapthis('https://www.amazon.in/s/ref=mega_elec_s23_2_1_1_1?rh=i%3Acomputers%2Cn%3A1375424031&ie=UTF8&bbn=976392031') 
