'''
Created on Feb 12, 2015

@author: Asif
'''
"""
from robobrowser import RoboBrowser
from bs4 import BeautifulSoup

browser = RoboBrowser()
browser.open('http://www.indianrail.gov.in/stn_Code.html')
signup_form = browser.get_form()

def getStations():
    mystations = []
    alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for alphabet in alphabets:
        signup_form['lccp_stnname'].value = alphabet
        browser.submit_form(signup_form)
        
        table = browser.select(".table_border_both")
        print(table)
        break
getStations()"""
from selenium import webdriver
from bs4 import BeautifulSoup
driver = webdriver.PhantomJS("C:\\Users\\Asif\\Desktop\\phantomjs-2.0.0-windows\\bin\\phantomjs.exe")
def go():
    driver.get("http://www.indianrail.gov.in/stn_Code.html")
    element = driver.find_element_by_name("lccp_stnname")
    element.send_keys("A")
    driver.find_element_by_name("submit").click()
    mysource = driver.page_source()
    soup = BeautifulSoup(mysource)
    for row in soup.find_all('table')[-1].tbody.find_all('tr'):
        cells = row.find_all('td')
                
        try:
            for elements in (cells[1]):
                print( str(elements.get_text()))
        except:
            return(None)
    
    
go()