#PyPoll
import os
import csv

pyPoll = []

candidates = []
candidate_ctr = 0
total_ctr = 0
votesList = []
candidateDict = {}

#Summary Table Stats
totalVotes = 0
candidateList = []
percentVotes = 0
winner = ' '

#csvpath = os.path.join('c:\users\TriciaToffey\desktop\githubs\python_challenge\pybank\Resources','budget_data.csv')
os.chdir('Resources')
with open('election_data.csv', encoding="ISO 8859-1") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    csv_header = next(csv_file)
    for row in csv_reader:
        pyPoll.append(row)

totalVotes = len(pyPoll)

for row in pyPoll:
    candidates.append(row[2])

#CANDIDATE NAMES
def unique_function(list1):
    unique_list = []
    for name in candidates:
        if name not in unique_list:
            unique_list.append(name)
    return unique_list
candidateList = unique_function(candidates)
#print(candidateList)

for candidate in candidateList:
    candidate_ctr = 0
    for row in pyPoll:
        if row[2] in candidate:
            candidate_ctr += 1
    percentVotes = round(((candidate_ctr / totalVotes) * 100) , 3)
    percentVotes = "{:.3%}".format(percentVotes/100)
    votesList.append({'Name': candidate, 'Votes':candidate_ctr, 'Percent': percentVotes})
#print(votesList)

def myFunc(e):
    return e["Votes"]

votesList.sort(reverse=True, key=myFunc)
#print(votesList)

#ANALYSIS
line1 = 'Election Results\n'
lines = ['---------------------------- \n',
'Total Votes: ' + str(totalVotes) +'\n',
'---------------------------- \n',
votesList[0]['Name'] + ':  ' + votesList[0]['Percent'] + '%  (' + str(votesList[0]['Votes']) +')\n',
votesList[1]['Name'] + ':  ' + votesList[1]['Percent'] + '%  (' + str(votesList[1]['Votes']) +')\n',
votesList[2]['Name'] + ':  ' + votesList[2]['Percent'] + '%  (' + str(votesList[2]['Votes']) +')\n',
votesList[3]['Name'] + ':  ' + votesList[3]['Percent'] + '%  (' + str(votesList[3]['Votes']) +')\n',
'---------------------------- \n', 
'Winner:  ' + votesList[0]['Name'] + '\n',
'---------------------------- \n']
my_file = open('../Analysis/Analysis2.txt', 'w')
my_file.write(line1)
my_file.writelines(lines)
my_file.close()
#print("Writing Complete\n\n")

print(open('../Analysis/Analysis2.txt').read())

