__author__ = 'Asif'
from robobrowser import RoboBrowser
from bs4 import BeautifulSoup

browser = RoboBrowser()
browser.open('http://rbs.indianrail.gov.in/ShortPath/ShortPath.jsp')
signup_form = browser.get_form(action='/ShortPath/ShortPathServlet')

def getSP(stn1,stn2):
    signup_form['srcCode'].value = str(stn1)
    signup_form['destCode'].value = str(stn2)
    browser.submit_form(signup_form)
    table = browser.select("#routetbl")
    #print(table)

    table = ''.join(str(i) for i in table)
    soup = BeautifulSoup(table)
    shortest_path = []
    for row in soup.findAll('table')[0].tbody.findAll('tr'):
        #first_column = row.findAll('th')[0].contents
        third_column = row.findAll('td')[1].contents
        shortest_path.append(str(third_column[0].replace("\r\n\t\t\t\t\t\t\t\t\t\t\t","")))
    print "\nThe Shortest Path from ",stn1," to ",stn2," is below :"
    print(shortest_path)

#Getting Shortest path from Vasco to Guntakal
getSP("VSG","GTL")

#Getting Shortest PAth from New DElhi to Cuddapah
getSP("NDLS","HX")

#Getting Shortest PAth from Cuddapah to Tirupati
getSP("HX","TPTY")
