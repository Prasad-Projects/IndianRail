'''
Created on May 6, 2015

@author: Asif
'''
import pickle

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

routes_list = pickle.load( open( "C:\Users\Asif\Desktop\Kurant\StationsRoutes.p", "rb" ) )
mylist = [
          (1884, 3314),
          (958, 1686),
          (1365, 2361),
          (757, 1887)
          ]
for edges in mylist:
    print(checkShortcut(edges[0], edges[1]))