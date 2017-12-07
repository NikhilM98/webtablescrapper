from BeautifulSoup import BeautifulSoup
import sys
import csv
import requests

baseurl="https://www.timesmed.com/OnlinePharmacy/India-Online-Medicine/Page-"

first=input("Enter index page: ")

for file in range(first,2151):
    url=baseurl+str(file)
    fin  = htmltext = requests.get(url).text
    print "Opening file & Parsing file "+str(file)
    soup = BeautifulSoup(fin,convertEntities=BeautifulSoup.HTML_ENTITIES)
    
    [s.extract() for s in soup('script')]

    tablecount = -1
    
    for table in soup.findAll(id="prescription_tbl"):
        tablecount += 1

        with open(str(tablecount)+'file'+str(file)+'.csv', 'wb') as csvfile:
            fout = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            for row in table.findAll('tr'):
                cols = row.findAll(['td','th'])

                if cols:
                    cols = [x.text for x in cols]
                    fout.writerow(cols)
