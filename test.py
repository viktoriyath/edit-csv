import csv
import re

filename = 'participants.csv'
try:
    with open(filename, 'rb') as fh:
        reader = csv.reader(fh, delimiter=',')
        for row in reader:
            if len(row) != 2:
                print("Row {} does not contain 2 fields".format(row))
                exit(1)
            if not re.search(r'^\w+$', row[0]):
                print("Row {} has an invalid username".format(row))
                exit(1)


except Exception as e:
    print("Could not read '{}'".format(filename))
    print(e)
    exit(1)

exit(0) 
