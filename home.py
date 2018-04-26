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
from bs4 import BeautifulSoup
from time import sleep
import cx_Oracle
import re
import lxml
URLlst = []
#function to scrap and havde a list of url for th efirst page 
def scrapthis(url):
        con = cx_Oracle.connect('steven/admin@//localhost:1521/oracle')
        cursor = con.cursor()
        print("Starting the program" );
        req=requests.get(url)
        #print(req.status_code)
        #print(req.headers) # prints the header of page
        #print(req.content) # print all contetnt of the page
        #TIP1 To parse a document, pass it into the BeautifulSoup constructor. You can pass in a string or an open filehandle:
        soup = BeautifulSoup(req.content,'lxml')
        #Now soup hold all parsed page
        #print(soup )          
        result = soup.find('div', id='atfResults').find_all('li')
        #print('ytyt')
        for tag in result:
            a=tag.find_all('a')
            print('**********')
            for link  in a:
                #print(length(link))
                prdlnk = link.get('href')
                URLlst.append(prdlnk)               
        print("Program Ends here" )
        #Debug the length of the list
        print(len(URLlst))
        #convert the list to set to have unique values
        urlset = set(URLlst)
        #now the set has unique values
        print(len(urlset ))
        for allset in urlset:
            querystring = "Insert into AMAZON_OUTPUT_TUPLES(URL) values("+"'"+allset+"'"+")"
            #querystring = "Insert into test_scrap values("+"'"+product_name+"',"+"'"+product_url+"')"
            print(allset)
            print('Inserting below record')
            #print(querystring)
            cursor.execute(querystring)
            cursor.execute('commit')
#call function with url        
scrapthis("https://www.amazon.in/s/s/ref=sr_nr_p_89_3?fst=as%3Aoff&rh=n%3A976392031%2Cn%3A%211499764031%2Cn%3A%211499766031%2Cn%3A14174299031%2Cp_89%3ADell%7CLenovo&bbn=14174299031&ie=UTF8&qid=1510988837&rnid=3837712031")    