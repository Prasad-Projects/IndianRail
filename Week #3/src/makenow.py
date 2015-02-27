'''
Created on Feb 27, 2015

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
edges = G.edges()
f = open('FinalOne.txt','r')
for lines in f.readlines():
    lines= lines.strip('\n')
    lines = lines.split(',')
    myedge = (lines[0],lines[1])
    if(not myedge in edges):
        G.add_edge(lines[0],lines[1],weight= float(lines[2]))


