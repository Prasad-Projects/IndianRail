'''
Created on Feb 27, 2015

@author: Asif
'''
from os import listdir
from os.path import isfile, join
import lxml
from bs4 import BeautifulSoup
import re
newdict = {}
ERROR = ""
mypath = "C:\\Users\\Asif\\Desktop\\AllFinal"
onlyfiles = [ "C:\\Users\\Asif\\Desktop\\AllFinal\\"+f for f in listdir(mypath) if isfile(join(mypath,f)) ]
making = 0
golist = []
fnew = open("StoreThis.txt","w+")
myfinstr = ""
def finalattempt(list1,list2):
    global golist,ERROR,myfinstr
    if(len(list1) == len(list2)):
        start = 1
        while(start < len(list1)):
            if([list1[start-1],list1[start]] in golist):
                pass
            else:
                golist.append([list1[start-1],list1[start]])
                golist.append([list1[start],list1[start-1]])
                myfinstr += list1[start-1]+","+list1[start]+","+str(list2[start])
                myfinstr += list1[start]+","+list1[start-1]+","+str(list2[start])
            start += 1
            
    else:
        print("ERR ",ERROR)
def dict_process(mylist,mylist2):
    global newdict,ERROR
    
    diff = 0
    newlist = []
    for items in mylist2:
        newlist.append(items-diff)
        diff = items
    mylist2 = newlist
    finalattempt(mylist, mylist2)
    return()
    if(len(mylist) == len(mylist2)):
        start = 1
        while(start<len(mylist)):
            if(mylist[start-1] in newdict.keys()):
                if(mylist[start] in newdict.keys()):
                    pass
                else:
                    newdict[mylist[start-1]][mylist[start]] = mylist2[start]
                    newdict[mylist[start]] = {mylist[start-1]:mylist2[start]}           
            else:
                newdict[mylist[start-1]] = {mylist[start]:mylist2[start]}
                if(mylist[start] in newdict.keys()):
                    newdict[mylist[start]][mylist[start-1]] = mylist2[start]
                else:
                    newdict[mylist[start]] =  {mylist[start-1]:mylist2[start]}
            start +=1
    else:
        print("False!!!",ERROR)
        
def testing(content):
    soup = BeautifulSoup(content)
    table = soup.find_all(id = 'schtbl')[0]
    initial = 0
    mylist1 = []
    mylist2 = []
    for row in table.tbody.find_all('tr'):
        cols = row.find_all('td')
        if(len(cols) == 6):
            if(initial == 0):
                initial = 1
            else:
                mylist1.append(str(cols[1].a.get_text()))
                mylist2.append(int(cols[5].get_text()))
    dict_process(mylist1, mylist2)
    
   
    
    

for myfiles in onlyfiles:
    
    ERROR = myfiles
    opening = open(myfiles,"r")
      
    content = opening.read()
    try:
        testing(content)
    except:
        print(ERROR)
    print(making,len(golist))
    making += 1
    opening.close()

fnew.write(myfinstr)
    

