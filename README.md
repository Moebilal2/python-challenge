# python-challenge
PyBank
import os
import csv


file = os.path.join("Resources","budget_data.csv")
outfile = os.path.join("analysis","PayBank Analysis.txt")
totalmonths=0 # to hold the counter
totalamount=0
changes=[] #to hold the monthly changes in total value
newchange=0
month=[]

inicialamount=0 #This is the amount of total value of the header
with open(file,'r') as text:
    reader=csv.reader(text,delimiter=",")
    header=next(reader)
    firstrow=next(reader)
    totalmonths+=1
    totalamount=float(firstrow[1])
    lastvalueamount=float(firstrow[1])
    #Iterate throw the row to count
    for row in reader:
        totalmonths+=1
        totalamount+=float(row[1])
    
        newchange=float(row[1])-lastvalueamount #The changes of the first month is the amount of the first month
        changes.append(newchange)
        #add the month
        month.append(row[0])
        lastvalueamount=float(row[1])
    
#Calculate the average changes in total values
averagechange=sum(changes)/len(changes)

#Calculate the increase and decrease
greatestincrease=["",0]
greatestdecrease=["",0]
for m in range(len(changes)):
    if changes[m]>greatestincrease[1]:
        greatestincrease[1]=changes[m] #will get the amount of the greatest increase
        greatestincrease[0]=month[m] #this will get the month
    if changes[m]<greatestdecrease[1]:
        greatestdecrease[1]=changes[m] #will get the amount of the greatest increase
        greatestdecrease[0]=month[m] #this will get the month

    
    

final=(f"Financial Analysis \n"
      f"------------------ \n"
      f"Total Months: {totalmonths}\n"
      f"Total Amount of Profit/Losses: ${totalamount}\n"
      f"Average Change: ${averagechange:,.2f}\n"
      f"Greatest Increase in profits: {greatestincrease[0]} ${greatestincrease[1]}\n"
      f"Greatest Decrease in profits: {greatestdecrease[0]} ${greatestdecrease[1]}")
with open(outfile,'w') as outf:
    outf.write(final)

-------------------------------------------------------------------------------------------------------------------------------

PyPol
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