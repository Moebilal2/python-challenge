import os
import csv
file2 = os.path.join("Resources","election_data.csv")
outputfile = os.path.join("analysis","PayPol Analysis.txt")
candidate=[]
candidatevotes={}
winnercount= 0 #will hold the winning count
winningcandidate=""
with open(file2,'r') as text:
    reader=csv.reader(text)
    header=next(reader)
    totalvoters=0
    for row in reader:
        totalvoters+=1
        if row[2] not in candidate:
            candidate.append(row[2])
            #add value to the dictionary
            #{"key":value}
            #start the count at 1 for the votes
            candidatevotes[row[2]]=1
        else:
            #the candidate is in the list
            #add a vote to the candidate count
            candidatevotes[row[2]]+=1
votersoutput=""
for x in candidatevotes:
    #get the vote count and the percentage of the votes
    votes=candidatevotes.get(x)
    votepercent=(float(votes)/float(totalvoters))*100.00
    votersoutput+=(f"\n{x}: {votepercent:.2f}% ({votes})\n")
    #compare the votes to the winner count
    if votes>winnercount:
        #update the votes to be the new winnercount
        winnercount=votes
        #update the winning flavor
        winningcandidate=x
   
output=(f"Election Results\n"
      f"------------------\n"
      f"Total Votes: {totalvoters}\n"
      f"------------------\n"
      f"{votersoutput}\n"
      f"------------------\n"
      f"Winner: {winningcandidate}\n"
      f"------------------")
with open(outputfile,'w') as textout:
    textout.write(output)