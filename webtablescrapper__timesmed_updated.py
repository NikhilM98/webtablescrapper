from bs4 import BeautifulSoup
import sys
import csv
import requests

baseurl="https://www.timesmed.com/OnlinePharmacy/India-Online-Medicine/Page-"

for file in range(1,2101):
    url=baseurl + str(file)
    fin  = htmltext = requests.get(url).text
    print(file)
    soup = BeautifulSoup(fin, "html.parser")
    [s.extract() for s in soup('script')]
    tablecount = -1
    for table in soup.findAll(id="prescription_tbl"):
        tablecount += 1
        with open('file'+str(tablecount)+str(file)+'.csv', 'wb') as csvfile:
            fout = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in table.findAll('tr'):
                cols = row.findAll(['td','th'])
                if cols:
                    cols = [x.text for x in cols]
                    fout.writerow(cols)

# for linux
#cat file*.csv > combined.csv

#for ubuntu
#copy file*.csv combined.csv
