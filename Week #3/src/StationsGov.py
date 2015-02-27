'''
Created on Feb 16, 2015

@author: Asif
'''
import mechanize
from bs4 import BeautifulSoup
import re
import pickle

def go(letter):
    filename = "C:\\Users\\Asif\\Desktop\\StnCodes\\"+letter+".html"
    f = open(filename,'r')
    content = f.read()
    f.close()
   
    mylist = re.findall(r'<TR>\n<TD>\w+.*</TD>\n<TD>(\w+.*)</TD>\n</TR>',str(content))
    mylist = [items.strip(" ") for items in mylist]
    
    return(mylist)
    
def giveStation(letter):
    url = "http://www.indianrail.gov.in/stn_Code.html"
    
    br = mechanize.Browser()
    br.set_handle_robots(False) # ignore robots
    br.open(url)
    br.select_form(name="stn_code")
    br["lccp_stnname"] = letter
    res = br.submit()
    br.close()
    content = res.read()
    filename = "C:\\Users\\Asif\\Desktop\\01\\"+letter+".html"
    f = open(filename,"w+")
    f.write(content)
    f.close()
    return
    soup = BeautifulSoup(content)
    #print(soup.find_all('table'))
    #print(soup.findAll("table", { "class" : "table_border_both" }))
    print soup.find_all("table", class_="table_border_both")
    for row in soup.find_all('table')[-1].tbody.find_all('tr'):
        cells = row.find_all('td')                
        try:
            for elements in (cells[1]):
                print( str(elements.get_text()))
        except:
            return(None)
    
def getStations():
    mystations = []
    alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','Z']
    for letter in alphabets:
        mystations += go(letter)
        print(letter,len(mystations))
    print(mystations[:20])
    pickle.dump(mystations, open( "StationsGovt.p", "wb" ))  
        
        
getStations()
        

