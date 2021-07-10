#The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who recieved votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

import csv
import os

#assign variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")
#assign variable for the file to be created
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter
total_votes = 0
#create candidate list
candidate_options = []
# initialize candidate dictionary
candidate_votes = {}

#open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data) #store election data in memory to be used by calling variable
    #read header row
    headers = next(file_reader) #next() used to skip header row and start from first line of data.

    #print each row in the CSV file #inital run 2-3mins
    for row in file_reader:
        #2. Add to the total vote count
        total_votes += 1  #could use total_votes +=1
        #Print Candidate name form each row
        candidate_name = row[2]
        #if candidate does not match any existing candidates
        if candidate_name not in candidate_options:
            #add it to list
            candidate_options.append(candidate_name)
            #track candidate votes
            candidate_votes[candidate_name] = 0
        #add candidate votes
        candidate_votes[candidate_name] +=1

#3. Print the total votes
print(total_votes)
#print Candidate names
print(candidate_options)
#print candidate votes
print(candidate_votes)