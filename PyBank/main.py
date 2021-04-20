#PyBank
import os
import csv
pyBank = []
monthlyPL = []
totalPL = 0
firstRec = 0
#csvpath = os.path.join('c:\users\TriciaToffey\desktop\githubs\python_challenge\pybank\Resources', 'budget_data.csv')
with open('budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for row in csv_reader:
        pyBank.append(row)

#for row in pyBank:
#   print(row)

totalMonths = len(pyBank) #87 rows

#for row in pyBank:
#    print(type(row[1]))


for row in pyBank:
    if firstRec == 1:
        totalPL += int(row[1])
    else:
        firstRec = 1   
   
print(totalPL)

#for row in pyBank:
#    totalPL += int(row[1])

#print(totalPL)
