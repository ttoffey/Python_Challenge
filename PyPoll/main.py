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
unique_list = []
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

errorMessage = ' '

#csvpath = os.path.join('c:\users\TriciaToffey\desktop\githubs\python_challenge\pybank\Resources','budget_data.csv')
os.chdir('PyPoll/Resources')
with open('election_data.csv', encoding="ISO 8859-1") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for row in csv_reader:
        pyPoll.append(row)

start = 0
for item in pyPoll:
    if start < 5:
        print(item)
        start += 1

totalVotes = len(pyPoll)
totalVotes -= 1
print(totalVotes)   #3521001


for row in pyPoll:
    if firstRec == 0:
        firstRec = 1
    else:
        candidates.append(row[2])
firstRec = 0
#print(candidates)

def unique_list(list1):
    unique_list = []
    for name in candidates:
        if name not in unique_list:
            unique_list.append(name)
    return unique_list

candidateList = unique_list(candidates)
#print(candidateList)

def vote_count(votes, candidate):
    candidate_ctr = 0
    ctr = 0
    for row in votes:
        if ctr == 0:
            ctr = 1
        else:
            if row[2] in candidate:
                candidate_ctr += 1
    return candidate_ctr

khan_ctr = vote_count(pyPoll, "Khan")
correy_ctr = vote_count(pyPoll, "Correy")
li_ctr = vote_count(pyPoll, "Li")
otooley_ctr = vote_count(pyPoll, "O'Tooley")
#print(khan_ctr)  # 2218231
#print(correy_ctr) #704200
#print(li_ctr)   #492940
#print(otooley_ctr)   #105630countersList = [khan_ctr, correy_ctr, li_ctr, otooley_ctr]
countersList = [khan_ctr, correy_ctr, li_ctr, otooley_ctr]
total_ctr = khan_ctr + correy_ctr + li_ctr + otooley_ctr
#print(total_ctr)  #3521001
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

#print(khanPercent)  #63.000
#print(correyPercent) #19.999
#print(liPercent) #13.9999
#print(otooleyPercent)  #2.9999
countersList = [khan_ctr, correy_ctr, li_ctr, otooley_ctr]
#votesDictionary = {"Khan": [khan_ctr, khanPercent] "Correy": [correy_ctr, correy_ctr], "LiVotes": [li_ctr, liPercent], "O'Tooley": [otooley_ctr, otooleyPercent]}
votesDictionary = {"Khan": khan_ctr, "Correy": correy_ctr, "LiVotes": li_ctr, "O'Tooley": otooley_ctr}
#print(votesDictionary["KhanVotes"])
winnersList = sorted(votesDictionary.values())
winnersList.sorted(reverse=True)
print(winnerList)

