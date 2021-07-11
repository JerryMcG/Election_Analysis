#adding dependancies
import csv
import os

#assign variable for the file to load(with path) and file_to_save(with path)
file_to_load = os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0
#create candidate list
candidate_options = []
# initialize candidate dictionary
candidate_votes = {}
#empty string for winner, winning count and %
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#candidate_results list
candidate_results =[]


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

#get votes for each candidate and calc percentage
for candidate_name in candidate_votes:
    #get votes for each candidate
    votes = candidate_votes[candidate_name]
    #calc % of votes
    vote_percentage = float(votes) / float(total_votes) * 100
    #add votes to candidate_results list
    candidate_results.append(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    #determine winning vote count and candidate
    #is vote count/% greater than winning_vote
    if votes > winning_count and vote_percentage > winning_percentage:
        #if true - set values to winning counts/percentage
        winning_count = votes
        winning_percentage = vote_percentage
        #set winning candidate name equal to candidate name
        winning_candidate = candidate_name

#output results to text file and terminal
with open(file_to_save, "w") as txt_file:
    #print title to file
    election_results = (
        f"\nElection Results\n"
        f"------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------\n"
        f"{candidate_results.pop(0)}"
        f"{candidate_results.pop(0)}"
        f"{candidate_results.pop(0)}"
    )
    print(election_results, end="")
    #save the final vote count to text file.
    txt_file.write(election_results)

    #print winners details
    winning_candidate_summary = (
        f"------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Vote Percentage: {winning_percentage:.1f}%\n"
        f"------------------------------\n"
    )
    print(winning_candidate_summary)
    #save winning candidate to text file.
    txt_file.write(winning_candidate_summary)