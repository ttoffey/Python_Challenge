#PyPoll
import os
import csv
firstRec = 0
start = 0
pyPoll = []

#Summary Table Stats
totalVotes = 0
candidateList = []
candidateVotes = 0
percentVotes = 0
winner = ' '

candidates = []
candidate_ctr = 0
khan_ctr = 0
correy_ctr = 0
li_ctr = 0
otooley_ctr = 0
khanPercent = 0
correyPercent = 0
liPercent = 0
otooleyPercent = 0
total_ctr = 0
votesList = []
winnerList = []
errorMessage = ' '
voteCountList = []

#csvpath = os.path.join('c:\users\TriciaToffey\desktop\githubs\python_challenge\pybank\Resources','budget_data.csv')
os.chdir('Resources')
with open('election_data.csv', encoding="ISO 8859-1") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    csv_header = next(csv_file)
    for row in csv_reader:
        pyPoll.append(row)

start = 0

totalVotes = len(pyPoll)

for row in pyPoll:
    candidates.append(row[2])


#Candidate Names
def unique_function(list1):
    unique_list = []
    for name in candidates:
        if name not in unique_list:
            unique_list.append(name)
    return unique_list

candidateList = unique_function(candidates)

#Candidate Votes
def vote_count(votes, candidate):
    candidate_ctr = 0
    for row in votes:
        if row[2] in candidate:
            candidate_ctr += 1
    return candidate_ctr

khan_ctr = vote_count(pyPoll, "Khan")
correy_ctr = vote_count(pyPoll, "Correy")
li_ctr = vote_count(pyPoll, "Li")
otooley_ctr = vote_count(pyPoll, "O'Tooley")

total_ctr = khan_ctr + correy_ctr + li_ctr + otooley_ctr

if total_ctr != totalVotes:
    errorMessage = ("Total of individual candidate votes + {total_ctr} + does not match Total Votes + {totalVotes}.")
    print(errorMessage)

def percent_count(votes, total_ctr):
    percentVotes = round(((votes / total_ctr) * 100) , 3)
    return percentVotes

khanPercent = percent_count(khan_ctr, total_ctr)
correyPercent = percent_count(correy_ctr, total_ctr)
liPercent = percent_count(li_ctr, total_ctr)
otooleyPercent = percent_count(otooley_ctr, total_ctr)
percentCtrsList = [khanPercent, correyPercent, liPercent, otooleyPercent]

def myFunc(e):
    return e["Votes"]
votesList = [{"Candidate": "Correy", "Votes": correy_ctr, "Percent": correyPercent}, {"Candidate": "Khan", "Votes": khan_ctr, "Percent": khanPercent}, {"Candidate": "Li", "Votes": li_ctr, "Percent": liPercent}, {"Candidate": "O'Tooley", "Votes": otooley_ctr, "Percent": otooleyPercent}]
votesList.sort(reverse=True, key=myFunc)
print(votesList)

khanPercent = "{:.3%}".format(khanPercent/100)
correyPercent = "{:.3%}".format(correyPercent/100)
liPercent = "{:.3%}".format(liPercent/100)
otooleyPercent = "{:.3%}".format(otooleyPercent/100)

khan_ctr = str(khan_ctr)
correy_ctr = str(correy_ctr)
li_ctr = str(li_ctr)
otooley_ctr = str(otooley_ctr)

votesList[0]['Votes'] = khan_ctr
votesList[0]['Percent'] = khanPercent
votesList[1]['Votes'] = correy_ctr
votesList[1]['Percent'] = correyPercent
votesList[2]['Votes'] = li_ctr
votesList[2]['Percent'] = liPercent
votesList[3]['Votes'] = otooley_ctr
votesList[3]['Percent'] = otooleyPercent

print(votesList)

#Analysis

line1 = 'Election Results\n'
lines = ['------------------------- \n', 
'Total Votes: ' + str(totalVotes) +'\n',
'---------------------------- \n', 
votesList[0]['Candidate'] + ':  ' + votesList[0]['Percent'] + '%  (' + votesList[0]['Votes'] +')\n',
votesList[1]['Candidate'] + ':  ' + votesList[1]['Percent'] + '%  (' + votesList[1]['Votes'] +')\n',
votesList[2]['Candidate'] + ':  ' + votesList[2]['Percent'] + '%  (' + votesList[2]['Votes'] +')\n',
votesList[3]['Candidate'] + ':  ' + votesList[3]['Percent'] + '%  (' + votesList[3]['Votes'] +')\n',
'---------------------------- \n', 
'Winner:  ' + votesList[0]['Candidate'] + '\n',
'---------------------------- \n']
my_file = open('../Analysis/Analysis.txt', 'w')
my_file.write(line1)
my_file.writelines(lines)
my_file.close()
print("Writing Complete\n\n")

print(open('../Analysis/Analysis.txt').read())

