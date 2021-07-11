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
#empty string for winner, winning count and %
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data) #store election data in memory to be used by calling variable
    #read header row
    headers = next(file_reader) #next() used to skip header row and start from first line of data.

    #print each row in the CSV file #inital run 2-3mins
    for row in file_reader:
        #Add to the total vote count
        total_votes += 1 #same as: total_votes = total_votes + 1
        #Print Candidate name from each row
        candidate_name = row[2]
        #if candidate does not match any existing candidates
        if candidate_name not in candidate_options:
            #add it to list
            candidate_options.append(candidate_name)
            #track candidate votes
            candidate_votes[candidate_name] = 0
        
        #add candidate votes
        candidate_votes[candidate_name] +=1
        #save results to text file
    with open(file_to_save, "w") as txt_file:
    #print title to file
        election_results = (
            f"\nElection Results\n"
            f"------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"------------------------\n")
        print(election_results, end="")
        #save the final vote count to text file.
        txt_file.write(election_results)

#get votes for each candidate and calc percentage
for candidate_name in candidate_votes:
    #get votes for each candidate
    votes = candidate_votes[candidate_name]
    #calc % of votes
    vote_percentage = float(votes) / float(total_votes) * 100
    #print candidate name and % votes
    #print(f"{candidate_name} recieved {vote_percentage:.1f}% of the votes ({votes:,})\n")
    #determine winning vote count and candidate
    #is vote count/% greater than winning_vote
    if votes > winning_count and vote_percentage > winning_percentage:
        #if true - set values to winning counts/percentage
        winning_count = votes
        winning_percentage = vote_percentage
        #set winning candidate name equal to candidate name
        winning_candidate = candidate_name

#print winners details
winning_candidate_summary = (
    f"------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Vote Percentage: {winning_percentage:.1f}%\n"
    f"------------------------------\n"
)
#print(winning_candidate_summary)