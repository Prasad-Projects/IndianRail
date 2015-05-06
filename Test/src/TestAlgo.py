'''
Created on May 6, 2015

@author: Asif
'''
"""
#######  First Phase of Testing
mapping.dat has the info all the routes.
Adding the info provided.... 

1) First Get all the routes of the trains
2) Construct Graph following all the routes
3) Weight of an edge is the number of trains passed through that edge in either direction
"""

from collections import Iterable
import json
import networkx as nx
import pickle

routes_list = []
f = open("mapping.dat","r")
for lines in f.readlines():
    
    #Remove the last spaces and new lines
    lines = lines.rstrip()
    
    #First dump the line as it is easy to load back
    lines = json.dumps(lines)
    
    #Replace the curly brackets to square to represent as a list
    lines = lines.replace('{', '[')
    lines = lines.replace('}',']')
    
    #Load two times as in the first it creates a string and then to a list
    mylist = json.loads(lines)
    mydict = json.loads(mylist)
    
    #Append to a list
    routes_list.append(mydict)
    
f.close()

#Create a Space of stops Graph
stopsGraph = nx.Graph()

#Create a variable to modify the routes_list to actual routes list without any info of weight
route_variable = 0

#Iterate through all the routes
for info in routes_list:
    
    #Get the Weight first
    _weight = info[0]
    
    #Then Iterate through each edge present in the route
    for i in range(1,len(info[1])):
        node1 = info[1][i-1]
        node2 = info[1][i]
        if(stopsGraph.has_edge(node1, node2)):
            stopsGraph[node1][node2]['weight'] += _weight
        else:
            stopsGraph.add_edge(node1,node2,weight = _weight)
    
    #Remove the weight information from the routes list
    routes_list[route_variable] = routes_list[route_variable][1]
    route_variable += 1

print("Processed Space of Stops!!! Graph Constructed ...")

##Now a Function to check if an edge is an shortcut or not
def checkShortcut(e1,e2):
    global routes_list
    
    #Complete list of paths proving the edge being a shortcut
    complete_list = set()
    
    #Store the detailed path here
    myindpaths = []
    
    #For every route in the route list
    for paths in routes_list[:]:
        
        #Detailed path is stored here 
        myindpaths = []
        
        #triggered is set if one node is present
        triggered = 0
        
        #Iterate through every path
        for items in paths:
            
            #If any node is found in the list
            if(items == e1 or items == e2):
                triggered = 1
            
            #If the second node is found
            if(myindpaths and myindpaths[0] == e1 and items == e2):
                triggered = 0
                if(len(myindpaths)>1):
                    myindpaths.append(items)
                    complete_list.add(tuple(myindpaths))
                break
            
            #If the other node is found
            if(myindpaths and myindpaths[0] == e2 and items == e1):
                triggered = 0
                if(len(myindpaths)>1):
                    myindpaths.append(items)
                    complete_list.add(tuple(myindpaths))
                break
            
            #Just append
            if(triggered == 1):
                myindpaths.append(items)
                
    #Just return the empty list
    return(list(complete_list))

#This is a function to flatten a list
#That is if there is a list present in another list it will make into a single list
def flatten(lis):
    #Check for each item if it is iterable or not
    for item in lis:
        #Check if it is iterable and not a string
        if isinstance(item, Iterable) and not isinstance(item, basestring):
            #Then yeild each item in the list iterable
            for x in flatten(item):
                yield x
        else:
            yield item

#Change the routes_list
def changeRoutes(shortpath):
    global routes_list
    ind = 0
    #Iterate through each item in the route list
    for items in routes_list[:]:
        
        #ITerate through every node in the route
        for j in range(1,len(items)):
            
            #Checking if it is an edge and it is replace that edge
            if(items[j-1] == shortpath[0] and items[j] == shortpath[-1]):
                
                for indnodes in shortpath[1:-1]:
                    if(indnodes in items):
                        return(False)
                    
                #First insert the detail path and then flatten the list
                routes_list[ind].insert(j,shortpath[1:-1])
                routes_list[ind] = list(flatten(routes_list[ind]))
                
                break
            
            #What if it is reverse?
            elif(items[j-1] == shortpath[-1] and items[j] == shortpath[0]):
                
                for indnodes in shortpath[1:-1]:
                    if(indnodes in items):
                        return(False)
                    
                myRevPath = shortpath[1:-1]
                myRevPath.reverse()
                routes_list[ind].insert(j,myRevPath)
                routes_list[ind] = list(flatten(routes_list[ind]))
                
                break
            
            else:
                pass
        
        ind += 1
    return(True)

def check_loops():
    global routes_list
    for indRoutes in routes_list:
        if(len(set(indRoutes)) != len(indRoutes)):
            print(indRoutes)
            return(True)
    return(False)

nx.write_gpickle(stopsGraph,"C:\\Users\Asif\Desktop\Kurant2\StopsGraph.gpickle")
pickle.dump( routes_list, open( "C:\\Users\Asif\Desktop\Kurant2\StopsRoutes.p", "wb" ) )

mylist = [
          set([1884, 3314]),
          set([958, 1686]),
          set([1365, 2361]),
          set([757, 1887])
          ]

processing = 1


for edges in stopsGraph.edges():
    
    node1 = edges[0]
    node2 = edges[1]    
    if(set([node1,node2]) in mylist):
        continue
    
    detail_path = checkShortcut(node1, node2)
    
            
    if(len(detail_path)>0):
        test = 0
        for det_paths in detail_path:
            if(changeRoutes(list(det_paths))):
                detail_path = list(det_paths)
                test = 1
                break
        if(test == 0):
            continue
        
        thisWeight = stopsGraph[node1][node2]['weight']
        stopsGraph.remove_edge(node1, node2)
        for iNode in range(1,len(detail_path)):
            try:
                stopsGraph[detail_path[iNode-1]][detail_path[iNode]]['weight'] += thisWeight
                
            except:
                print(detail_path[iNode-1],detail_path[iNode])
                quit()
    print(processing)
    processing += 1   
    

nx.write_gpickle(stopsGraph,"C:\\Users\Asif\Desktop\Kurant2\StationsGraph.gpickle")
pickle.dump( routes_list, open( "C:\\Users\Asif\Desktop\Kurant2\StationsRoutes.p", "wb" ) )
