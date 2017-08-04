import csv
import re

file2_list = []

with open('2.csv', 'r') as fh2:
    reader = csv.reader(fh2)
    for row in reader:
        if re.search(r'\d', row[0]):
            file2_list = row
            break

with open('1.csv', 'r') as fh1:
    reader = csv.reader(fh1)
    for row in reader:
        if not re.search(r'[^\d]', row[0]):

            result = [] 

            for i,v in enumerate(row):
                result.append(int(v) * int(file2_list[i]))

            print(sum(result))
            