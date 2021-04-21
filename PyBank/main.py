#PyBank
import os
import csv
firstRec = 0
pyBank = []
pyBankUpdated = [] 

firstPL = 0
lastPL = 0
monthlyChange_list = ['Avg Monthly P&L Change', 0]

totalMonthlyChange = 0
priorMonth = 0
changePL = 0

#Summary Table
totalMonths = 0
totalPL = 0
avgMonthlyChange = 0
dateIncrease = ' '
dateDecrease = ' '
greatestIncrease = 0
greatestDecrease = 0


#csvpath = os.path.join('c:\users\TriciaToffey\desktop\githubs\python_challenge\pybank\Resources','budget_data.csv')
os.chdir('PyBank\Resources')
with open('budget_data.csv', encoding="ISO 8859-1") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for row in csv_reader:
        pyBank.append(row)
        
#CALCULATE TOTAL PL
for row in pyBank:
    if firstRec == 1:
        totalPL += int(row[1])
    else:
        firstRec = 1   
firstRec = 0     


#CALCULATE TOTAL PL CHANGES
firstPL = int(pyBank[1][-1])
lastPL = int(pyBank[totalMonths - 1][-1])
totalPLChanges = lastPL - firstPL


#CALCULATE AVERAGE CHANGE P&L - MONTHLY
for row in pyBank:
    if firstRec == 0:      
        firstRec = 1
    elif firstRec == 1:    
        firstRec = 2
        priorMonth = int(row[-1])
    else:
        changePL = int(row[-1]) - priorMonth 
        totalMonthlyChange += changePL
        monthlyChange_list.append(changePL)
        priorMonth = int(row[-1])
        changePL = 0

firstRec = 0

#CACLUCATE AVERAGE MONTHLY CHANGE
totalMonths = (len(monthlyChange_list) - 1)
avgMonthlyChange = round(totalMonthlyChange / (totalMonths - 1), 2)
print(avgMonthlyChange) 

#New List with months, p&l and monthly change
pyBankUpdated = zip(pyBank, monthlyChange_list)

#GREATEST INCREASE & GREATEST DECREASE
for row in pyBankUpdated:
    if firstRec == 0:
        firstRec = 1
    else:
        if int(row[1]) > greatestIncrease:
            greatestIncrease = int(row[1])
            dateIncrease = row[0][0]
        elif int(row[1]) < greatestDecrease:
            greatestDecrease = int(row[1])
            dateDecrease = row[0][0]

firstRec = 0


line1 = 'Financial Analysis \n'
lines = ['-------------------- \n', 
'Total Months: ' + str(totalMonths) +'\n',
'Total: $' + str(totalPL) + '\n',
'Average Change: $' + str(avgMonthlyChange) + '\n',
'Greatest Increase in Profits: ' + dateIncrease + '  ($' + str(greatestIncrease) + ')\n',
'Greatest Decrease in Profits: ' + dateDecrease + '  ($' + str(greatestDecrease) + ')\n']
my_file = open('file_read_write.txt', 'w')
my_file.write(line1)
my_file.writelines(lines)
my_file.close()
print("Writing Complete\n\n")

print(open('file_read_write.txt').read())