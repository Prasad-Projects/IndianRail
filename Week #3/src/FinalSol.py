'''
Created on Feb 8, 2015

@author: Asif
'''
#Get All the Work done previously
import networkx as nx
from getShortestPath import G
import pickle
from networkx.classes.function import number_of_nodes

myshortlist = nx.dijkstra_path(G,'TPTY','HX')
leng = 0.0
for i in range(len(myshortlist)-1):
    leng += float(G[myshortlist[i]][myshortlist[i+1]]['weight'])
    #print(leng)

non_existent = []
mystationlist = pickle.load( open( "StationsGovt.p", "rb" ) )
for elements in mystationlist:
    if(not elements in G):
        non_existent.append(elements)

print(non_existent,len(non_existent))
pickle.dump(non_existent, open( "NotExist.p", "wb" ))      
print(number_of_nodes(G)) 
print(myshortlist)