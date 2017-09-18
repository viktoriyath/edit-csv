import csv
import re

filename = 'dwarfs.csv'
try:
    with open(filename, 'r') as fh:
        reader = csv.reader(fh, delimiter=',')
        counter = 0
        for row in reader:
            counter += 1
            if len(row) != 2:
                print("Row {} does not contain 2 fields".format(row))
                exit(1)
            if counter == 9:
                if row[0] != 'Snow White':
                    print("The English name is 'Snow White'. Currenly we have '{}'".format(row[0]))
                    exit(1)
                if row[1] != 'Hófehérke':
                    print("The Hungarian name is 'Hófehérke'. Currently we have '{}'".format(row[1]))
                    exit(1)


except Exception as e:
    print("Could not read '{}'".format(filename))
    print(e)
    exit(1)

exit(0) 
