'''
Created on Jul 4, 2020

@author: KALYANASHIS
'''

from selenium import webdriver


driver = webdriver.Chrome("")
driver.get("http:google.com")
driver.set_page_load_timeout(10)



