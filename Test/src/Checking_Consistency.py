'''
Created on May 6, 2015

@author: Asif
'''
import networkx as nx

f = open("C:\Users\Asif\Desktop\Kurant\original_Stations.txt","r")
original_set = set()
for lines in f.readlines():
    lines = [int(nums) for nums in lines.split()]
    original_set.add(tuple(lines))
f.close()

myAlgo_set = set()
stationsGraph = nx.read_gpickle("C:\\Users\\Asif\\Desktop\\Kurant2\\StationsGraph.gpickle")
for edges in stationsGraph.edges():
    myAlgo_set.add(edges)

print(len(original_set),len(myAlgo_set))

print("#########Diferrence1##########")
for items in original_set:
    if(items not in myAlgo_set):
        print(items)
