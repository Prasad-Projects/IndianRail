'''
Created on Feb 27, 2015

@author: Asif
'''
#Get All the Work done previously
import networkx as nx
from makenow import G
from networkx.classes.function import number_of_nodes

myshortlist = nx.dijkstra_path(G,'SBI','HX')
print(myshortlist)
print(G.number_of_nodes())