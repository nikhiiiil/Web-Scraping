# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 15:47:57 2020

@author: lingam
"""

from selenium import webdriver
import pandas as pd
from selenium.webdriver.support.ui import Select
import time
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

problem_code ="DFNC"
problem = "https://www.codechef.com/problem/"
submissions_Url = "https://www.codechef.com/status/"

scraping_url =submissions_Url+problem_code


chrome_path = r"C:\Users\linga\Downloads\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get(scraping_url)

element = driver.find_element_by_id('status')
drop = Select(element)
drop.select_by_visible_text('AC')

driver.find_element_by_name('Submit').click()
time.sleep(2)

rows = len(driver.find_elements_by_xpath('//*[@id="primary-content"]/div/div[3]/table/tbody/tr'))
cols = len(driver.find_elements_by_xpath('//*[@id="primary-content"]/div/div[3]/table/thead/tr[1]/th'))

ids=[]
for row in range(1,rows):
    id = driver.find_element_by_xpath('//*[@id="primary-content"]/div/div[3]/table/tbody/tr['+str(row)+']/td[1]').text
    ids.append(id)
    
submisisons_urls=[]
for i in ids:
    submisisons_urls.append("https://www.codechef.com/viewplaintext/"+i)
    
    
import os
os.mkdir("codechef-"+problem_code)

for i in range(len(submisisons_urls)):
    req = Request(submisisons_urls[i],headers={'User-Agent': 'Chrome'})
    page = urlopen(req).read()
    page = BeautifulSoup(page,'html.parser')
    code = page.find('pre').text
    with open("codechef-"+problem_code+"/codechef-"+problem_code+"-"+ids[i]+".txt","w") as f:
        f.write(code)
        
print("files created in directory")



#change windows to below command
"""
driver.switch_to_window(driver.window_handles[0])
"""