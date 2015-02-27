'''
Created on Feb 8, 2015

@author: Asif
'''
import pickle
import networkx as nx

myfinaldict = pickle.load( open( "PickledDict2.p", "rb" ) )
G = nx.Graph()
for items in myfinaldict.keys():
    src = items
    for target in myfinaldict[items].keys():
        G.add_edge(src,target,weight = float(myfinaldict[src][target]))
"""

myshortlist = nx.dijkstra_path(G,'VSG','NZM')
leng = 0.0
for i in range(len(myshortlist)-1):
    leng += float(G[myshortlist[i]][myshortlist[i+1]]['weight'])
    
print(myshortlist,leng)"""        
    