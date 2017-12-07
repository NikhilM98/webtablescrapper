from BeautifulSoup import BeautifulSoup
import sys
import csv
import requests

baseurl="https://www.timesmed.com/OnlinePharmacy/India-Online-Medicine/Page-"

for file in range(2000,2001):
    url=baseurl+str(file)
    fin  = htmltext = requests.get(url).text
    print "Opening file & Parsing file "+str(file)
    soup = BeautifulSoup(fin,convertEntities=BeautifulSoup.HTML_ENTITIES)
#print "Preemptively removing unnecessary tags"
    [s.extract() for s in soup('script')]
# print "CSVing file"
    tablecount = -1
    for table in soup.findAll(id="prescription_tbl"):
        tablecount += 1
# print "Processing Table #%d" % (tablecount)
        with open('file'+str(tablecount)+str(file)+'.csv', 'wb') as csvfile:
            fout = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in table.findAll('tr'):
                cols = row.findAll(['td','th'])
                if cols:
                    cols = [x.text for x in cols]
                    fout.writerow(cols)
#cat file*.csv > combined.csv