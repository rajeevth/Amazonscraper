# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 20:29:29 2018

@author: rajeev
"""

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from scrapthis import scrapthis
listURL = []
#driver = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe')
driver = webdriver.Firefox(executable_path="C:\\geckodriver\\geckodriver.exe")
#driver = webdriver.Firefox('C:\\Users\\rajeev\\Desktop\\Scrapping_Projects\\resource\\geckodriver\\geckodriver.exe')
#driver = webdriver.Firefox('D:\\geckodriver\geckodriver.exe')
driver.get('https://www.amazon.in/s/ref=lp_1375424031_pg_2/260-2334441-6024729?rh=n%3A976392031%2Cn%3A%21976393031%2Cn%3A1375424031&page=2&ie=UTF8&qid=1524666446')
#pagename =  driver.get_log('browser') to print browser loG
#Get the current url of page and then perform next

#save the first url in list 
#listURL.append(curURL)
#while driver.findElements(by.Id("pagnNextString")).Count !=0:
#while (driver.find_element_by_xpath("//span[@id='pagnNextString']").Count !=0):

while (driver.find_element_by_xpath("//span[@id='pagnNextString']")):
    #driver.find_element_by_partial_link_text('Next Page').click()
    #driver.find_element_by_xpath("//span[@id='pagnNextString']").click()
    driver.find_element_by_class_name('pagnNextArrow').click()
    curURL=driver.current_url
    listURL.append(curURL)
#print(curURL) 
    scrapthis(curURL)

#driver.find_element_by_name("print(tt)")
#driver.find_element_by_id('pagnNextString').count
#for urls in listURL:
#    print(urls)
'''
driver.find_element_by_xpath("//span[@id='pagnNextString']").click()
    #driver.findElements(by.Id("pagnNextString")
    #curURL=driver.current_url
    #listURL.append(curURL)

#WebElement elementOpen = driver.findElement(By.linkText("Next Page")); 

#Actions action= new Actions(driver);
'''