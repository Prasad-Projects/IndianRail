'''
Created on Feb 16, 2015

@author: Asif
'''
import codecs
from selenium import webdriver
import selenium.webdriver.support.ui as ui

import pickle
from __builtin__ import True
import time

#driver = webdriver.PhantomJS("C:\\Users\\Asif\\Desktop\\phantomjs-2.0.0-windows\\bin\\phantomjs.exe")
i = 0
def go(stnCode):
    global i
    
    driver = webdriver.PhantomJS("C:\\Users\\Asif\\Desktop\\phantomjs-2.0.0-windows\\bin\\phantomjs.exe")
    wait = ui.WebDriverWait(driver,10)
    makeQuery = "http://etrain.info/in#!STATION="+stnCode
    driver.refresh()
    driver.get(makeQuery)
    TrainType = None
    if('class="exp"' in driver.page_source):
        TrainType = "exp"
    else:
        TrainType = "pass"
    try:
        wait.until(lambda driver: driver.find_element_by_class_name(TrainType))
    except:
        print("This Station is not there .........................",stnCode)
        return
    m = (driver.find_element_by_class_name(TrainType))
    
    m.click()
    waiting = True
    startTime = time.time()
    while(waiting):
        if( '"Source" means train starts and "Destination" means train ends here.' in driver.page_source):
            waiting = False
        else:
            end = time.time()
            if(end - startTime > 10):
                waiting = False
                print(stnCode," : Failed")
    
    filename = "C:\\Users\\Asif\\Desktop\\AllFinal\\"+stnCode+".html"
    f = codecs.open(filename,"w+","utf-8")
    
    f.write(driver.page_source)
    
    f.close()
    print(i,stnCode)
    i += 1
    driver.delete_all_cookies()
    driver.close()
    
mylist = myfinaldict = pickle.load(open( "NotExist.p", "rb" ))

#print(mylist[470:475])

for stations in mylist[472:]:
    go(stations)
    
