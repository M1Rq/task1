import csv
from collections import Counter

result = {}

with open('data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csvreader:
        if row[0] in result:
            result[row[0]]['people'].append(row[1])
            result[row[0]]['count'] += 1
        else:
            result[row[0]] = {'people': [row[1]], 'count': 1}

    print(result)
