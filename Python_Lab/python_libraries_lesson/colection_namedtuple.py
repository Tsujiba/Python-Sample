"""
#############################################################################:
・colections.namedtuple
　　→座標とかタプルをクラスみたい(名前をつけて）に便利に使える
#############################################################################
"""

import csv
import collections

"""
tuple 
t = (2, 4)
print(t)
print(t[0])
t[0] = 3
"""

with open('named.csv', 'w', newline='') as csvfile:
    fieldnames = ['firstname', 'lastname', 'address']
    csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerow({'firstname':'Yu', 'lastname': 'Tsujibayashi', 'address':'Setagaya'})
    csv_writer.writerow({'firstname':'Masashi', 'lastname': 'Kamamoto', 'address':'Kawasaki'})
    csv_writer.writerow({'firstname':'Tomotoka', 'lastname': 'Araki', 'address':'Yokohama'})
    
with open('named.csv', 'r') as f:
    csv_reader = csv.reader(f)
    #print(next(csv_reader))
    Names = collections.namedtuple('Names', next(csv_reader))
    for row in csv_reader:
        names = Names._make(row)
        print(names.firstname, names.lastname, names.address)