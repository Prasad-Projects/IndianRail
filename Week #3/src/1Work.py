'''
Created on Feb 5, 2015

@author: Asif
'''

from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from bs4 import BeautifulSoup
#import re
#All the required Libraries are imported

#Using PhantomJS which does not open a browser which reduces potentially
# a great amount of time
driver = webdriver.PhantomJS("C:\\Users\\Asif\\Desktop\\phantomjs-2.0.0-windows\\bin\\phantomjs.exe")

def go(stn1,stn2):
    #Prepare the Selenium to handle alerts
        
    #Removing the redundant Characters in the output
    #regex = re.compile(r'[\r\n\t\\n\\t]')

    #Get the Driver Class
    driver.get("http://rbs.indianrail.gov.in/ShortPath/ShortPath.jsp")

    #Fill the Source and Destination entries
    element = driver.find_element_by_name("srcCode")
    element.send_keys(stn1)
    element = driver.find_element_by_name("destCode")
    element.send_keys(stn2)

    #Submit the form
    driver.find_element_by_name("findPath0").click()

    #Get the total number of links
    #total_links = len(re.findall('<a id=\"link\d+',driver.page_source))
    
    #Clicking all the links
    #Implemented a hack to click all the links
    start=0
    link="link"
    try:
        while(True):
            clickthis = link+str(start)
            start += 1
              
            driver.find_element_by_id(clickthis).click()
            #print 'The Start is now [%d%%]\r'%start,
           
    except:
        pass

    #Using Beautiful Soup Library to get the required elements
    mysource = driver.page_source
    
    filename = "C:\\Users\\Asif\\Desktop\\FormalWork2\\"+stn1+";"+stn2+".html"
    f = open(filename,"w+")
    f.write(mysource)
    f.close()
   

def main():
    myfile = open("qw2.txt","r")
    processed = 1
    for lines in myfile.readlines():
        
        lines = lines.strip("\n")
        lines = lines.split(",")
        go(lines[0],lines[1])
        print(processed,lines[0],lines[1])
        processed += 1
    myfile.close()

          
main()



