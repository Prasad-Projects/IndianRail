'''
Created on Mar 27, 2015

@author: Asif
'''
import csv
import networkx as nx
from networkx.algorithms.components.connected import number_connected_components
from networkx.classes.function import number_of_nodes
f = open("EdgesTrains.csv","r")
reader = csv.reader(f)

edgesGraph = nx.Graph()

trainNum = ''
myRoutes = []
indRoutes = []

def checkShortcut(e1,e2):
    mypaths = []
    myindpaths = []
    for paths in myRoutes:
        myindpaths = []
        triggered = 0
        for items in paths:
            if(items == e1 or items == e2):
                triggered = 1
            if(myindpaths and myindpaths[0] == e1 and items == e2):
                triggered = 0
                if(len(myindpaths)>1):
                    mypaths.append(paths)
                break
            if(myindpaths and myindpaths[0] == e2 and items == e1):
                triggered = 0
                if(len(myindpaths)>1):
                    mypaths.append(paths)
                break
            if(triggered == 1):
                myindpaths.append(items)
    return(mypaths)
        

for lines in reader:
    edgesGraph.add_edge(lines[1], lines[2])
    if(lines[0] != trainNum):
        if(trainNum != ''):
            myRoutes.append(indRoutes)
        trainNum = lines[0]
        indRoutes = [lines[1],lines[2]]
    
    else:
        indRoutes.append(lines[2])

its = 0
g1 = (len(edgesGraph.edges()))
g3 = number_of_nodes(edgesGraph)
#f1 = open('NewShortCutEdges.txt','a+')
for every_edge in edgesGraph.edges()[:]:
    e1 = every_edge[0]
    e2 = every_edge[1]
    isShortcut = checkShortcut(e1,e2)
    if(len(isShortcut)> 0):
        #f1.write(str(every_edge)+","+str(len(isShortcut))+","+str(isShortcut)+"\n")
        edgesGraph.remove_edge(e1, e2)
    print(its)
    its += 1
    
f.close()
#f1.close()
g2 = (len(edgesGraph.edges()))
print(g1,g2,g3)
print(number_connected_components(edgesGraph))
print(number_of_nodes(edgesGraph))
