#The data we need to retrieve
#1. The total number of votes case
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

#open the election results and read the file
with open(file_to_load) as election_data:
    
    file_reader = csv.reader(election_data) #store election data in memory to be used by calling variable
    #read and print the header row
    headers = next(file_reader) #next used to skip header row
    print(headers)

    #print each row in the CSV file #inital run 2-3mins
    #for row in file_reader:
     #   print(row)