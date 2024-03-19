#The total number of votes cast

#A complete list of candidates who received votes

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote


#first import the file
import os
import csv

#the file path 
election_data_csv = os.path.join('..', 'RESOURCES', 'election_data.csv')

#the file i want to print

output = os.path.join('..', 'RESOURCES', 'election_analysis.txt')

# we use WITH statement open and read file
with open(election_data_csv, 'r') as csvfile:
    electionReader = csv.reader(csvfile, delimiter=",")
    next(electionReader)  # inorder to skip the header


# create variables for total votes , the candidiate , winners's name and number of votes for winner
    
    totalVotes = 0
    candidates = {}
    winner = ""
    winner_votes = 0



    
    for row in electionReader:

      
        totalVotes += 1  # to count all votes
        
        # candidate name from EVERY next column to be stored in 'candidate' DICTIONARY
        candidate_name = row[2] 
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1
    
    # then we use for loop in order updates the winner variable with the name of the winning candidate and winner_votes
    for candidate, votes in candidates.items():
        if votes > winner_votes:
            winner = candidate
            winner_votes = votes


#Finally printing The Analysis

#print("Election Results") #The header
#print("-------------------------")
#print(f"Total Votes: {totalVotes}") #total number of voted held in the election
#print("-------------------------")
#for candidate, votes in candidates.items():
  #  percentage = (votes / totalVotes) * 100   #Finding the percentage
 #   print(f"{candidate}: {percentage:.3f}% ({votes})")  # print candidate name, percentage formatted to 3 decimal places , number of votes
#print("-------------------------")
#print(f"Winner : {winner}")  
#print("-------------------------")

analysis_text = f"""Election Results
-------------------------
Total Votes: {totalVotes}
-------------------------
"""
for candidate, votes in candidates.items():
    percentage = (votes / totalVotes) * 100   # Calculate the percentage
    analysis_text += f"{candidate}: {percentage:.3f}% ({votes})\n"
analysis_text += f"-------------------------\nWinner : {winner}\n-------------------------"

# Print the analysis to console
print(analysis_text)

# Write the analysis to a text file
with open(output, 'w') as f:
    f.write(analysis_text)

print(f"Analysis has been saved to '{output}'")