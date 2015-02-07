'''
Created on Feb 8, 2015

@author: Asif
'''
from bs4 import BeautifulSoup
import os
import re
import pickle

def getStationList(soup):
    mylist = []
    for row in soup.find_all('table')[-1].tbody.find_all('tr'):
        cells = row.find_all('td')
        adding = []
        
        try:
            for elements in (cells[1],cells[4]):
                adding.append(re.sub('\s+', '', str(elements.get_text())))
        except:
            return(None)
        
        mylist.append(adding)
    return(mylist)

def processPage(filename):
    #open the file
    f = open(filename,'r')
    #Read the contents of the page
    mystring = f.read()
    
    #Make the Soup object
    soup = BeautifulSoup(mystring)
    list_of_stations = getStationList(soup)
    
    #close the file
    f.close()
    return(list_of_stations)

myfinaldict = {}
fileslist = []
for path, subdirs, files in os.walk('C:\\Users\\Asif\\Desktop\\FormalWork'):
    for filename in files:
        f = os.path.join(path, filename)
        fileslist.append(str(f))

def addToDict(mylist1,mylist2):
    #Put one in two
    global myfinaldict
    try:
        #Checking if node1 is in node2
        adding = myfinaldict[mylist1[0]]
        adding[mylist2[0]] = mylist2[1] 
    
    except:
        myfinaldict[mylist1[0]] = {mylist2[0]:mylist2[1]}
    
    
    try:
        #checking if node2 in node1
        adding = myfinaldict[mylist2[0]]
        adding[mylist1[0]] = mylist2[1]
    
    except:
        myfinaldict[mylist2[0]] = {mylist1[0]:mylist2[1]}
        
    
doned = 0
errorfiles = open("NoPaths.txt","w+")
errorstring = ""
for files in fileslist:
    
    getlist = processPage(files)
    if(getlist == None):
        errorstring += files+"\n"
    else:
        for i in range(len(getlist)-1):
            addToDict(getlist[i],getlist[i+1])
    doned +=1
    print(doned)
    
errorfiles.write(errorstring)
errorfiles.close()
pickle.dump(myfinaldict, open( "PickledDict.p", "wb" ))



    

        