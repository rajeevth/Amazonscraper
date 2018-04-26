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
import time
URLlst = []  #intermideate list to store page number urls  
#function to scrap and havde a list of url for th efirst page 
#To create log file 
#f= open("gsoup.txt","wb")
#proxies = {
 # 'http': 'http://153.149.171.53',
  #'https': 'http://153.149.168.31',
#}
# function to scrap product url from category page numbers
def scrapthis(url):
        con = cx_Oracle.connect('steven/admin@//localhost:1521/oracle')
        cursor = con.cursor()
        print("Starting the program" );
        label: entry
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        req = requests.get(url, headers=headers)
        time.sleep(1)
#DEBUG Only#        
        #print(req.content)        
        #req=requests.get(url)
        #print(req.status_code)
        #print(req.headers) # prints the header of page
        #print(req.content) # print all contetnt of the page
        #TIP1 To parse a document, pprintass it into the BeautifulSoup constructor. You can pass in a string or an open filehandle:
#DEBUG Only#
        soup = BeautifulSoup(req.content,'lxml')
#Now soup hold all parsed page
#to find if amazon treats us like robot
        '''if (soup.find('api-services-suppor') == -1):            
            print ("Fetching data Progressing  ")
        else:           
            print ("Robotic detected")
            time.sleep(5)
            scrapthis(url)
            '''       
# this will have all li elements from where we will dig up the product URL
        result = soup.find('div', id='atfResults').find_all('li')
        for tag in result:
            a=tag.find_all('a')
            for link  in a:
                #print(length(link))
#get href that is the link of product                 
                prdlnk = link.get('href')
#append the link in list                 
                URLlst.append(prdlnk)               
        print("Program Ends here" )
        #Debug the length of the list
        #print(len(URLlst))
#We could have duplicate urls/links so convert the list to set to have unique values
        urlset = set(URLlst)
#now the set has unique values
#loopthrough set of product urls and store them in DB
        for allset in urlset:
            querystring = "Insert into AMAZON_OUTPUT_TUPLES(URL) values("+"'"+allset+"'"+")"
            #querystring = "Insert into test_scrap values("+"'"+product_name+"',"+"'"+product_url+"')"
            #print(allset)
            #print('Inserting below record')
            #print(querystring)
            cursor.execute(querystring)
            cursor.execute('commit')
#call function with url          
#scrapthis("https://www.amazon.in/s/s/ref=sr_nr_p_n_feature_thirteen_0?fst=as%3Aoff&rh=n%3A14174299031%2Cp_89%3ADell%7CLenovo%2Cp_n_feature_thirteen_browse-bin%3A12598162031&bbn=14174299031&ie=UTF8&qid=1524494320&rnid=12598141031")    
