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