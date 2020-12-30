import urllib
import json
import requests

URL = "https://www.medicaid.gov/sites/default/files/2020-11/drug-utilization-july.json"
URL = "drug-utilization-july.json"
csvfile = "filelist.csv"
downprefix = "https://data.medicaid.gov/resource/"

#f = urllib.urlopen(URL)
with open(URL, 'r') as f:
    datafile = json.load(f)

#print(json.dumps(list, sort_keys=True))
with open(csvfile, 'w') as csv:
    csv.write("State,Year,Link\n")
    for data in datafile['aaData']:
        if data['State']:
            csv.write(data['State'])
            csv.write(",")
            csv.write(str(data['Year']))
            csv.write(",")
            csv.write(downprefix + data['ID'] + ".csv" + "\n")

# this part will directly download

for data in datafile['aaData']:
        if data['State']:
            outfile = data['Category'] + "_" + data['State'] + "_" + str(data['Year'])  + ".csv"
            csvurl = downprefix + data['ID'] + ".csv"
            print(csvurl + " --> " + outfile)
            r = requests.get(csvurl)
            open(outfile, 'wb').write(r.content)

print("Finished downloading")
