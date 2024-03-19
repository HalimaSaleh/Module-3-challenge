#REQUESTS

#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#The changes in "Profit/Losses" over the entire period, and then the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period


#first we import the data set of "budget data"
import os
import csv

#my filepath from where to import the data

budget_data_csv = os.path.join('..', 'RESOURCES', 'budget_data.csv')

# declaire where to print
output = os.path.join('..', 'RESOURCES', 'My_Analysis.txt')



 # in order to read the file 
with open(budget_data_csv, 'r') as csvfile:
    budgetReader = csv.reader(csvfile, delimiter=',')
    
    budget_header = next(budgetReader) # i used Next function inOrder to skip the header

# inserted the variables
    
    total  = 0  #for the total months
    net = 0     #for net total
    preLoss = 0  #previous loss
    procng = []     #profit change
    greatestInc = ["", 0] # for greatest increase and used elements ["",0]  to store the date and amount of the greatest increase in profits
    greatestDec = ["", 9999999999999999999]  #used element empty sting and large number 

    for row in budgetReader: #inserted the for loop
       
            total += 1  #calculate the total month
            net += int(row[1]) #calculate the net total and converting the second row as integer
            
          

            # find change profit or loss
            if preLoss != 0:
                change = int(row[1]) -preLoss
                procng.append(change)
                

                #Calculate average change
                average_change = sum(procng) / len(procng)
                
                #calculate Greatest increase or decrease

                if change >greatestInc[1]:
                     
                 greatestInc= [row[0], change]
                if change < greatestDec[1]:
                 greatestDec = [row[0], change]
            
            preLoss= int(row[1])
           
    
    
        # Finally Print The Analysis
 
   
    Myanalysis = f"""Financial Analysis
    ------------------
    Total Months: {total}
    Total: ${net} 
    Average Change: ${average_change:.2f}
    Greatest Increase in Profits: {greatestInc[0]} (${greatestInc[1]})
    Greatest Decrease in Profits: {greatestDec[0]} (${greatestDec[1]})
    """
    print(Myanalysis)


with open(output, 'w') as f:
    f.write(Myanalysis)

print(f"THe Result of the Analysis is ALSO saved to '{output}'")