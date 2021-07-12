# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. Calculate how many votes were cast in each county.
7. Determine which county had the highest turnout.

## Resources
- Data Source: election_results.csv
- SoftwareL Python 3.9.6, Visual Studio Code 1.58.0

## Election Audit Results
The analysis of the election show that:
- There were 369,711 Votes Cast in the election.
- The county results were:
    - Jefferson had a total of 38,855 votes (10.5%)
    - Denver had a total of 306,055 votes (82.8%)
    - Arapahoe had a total of 24,801 votes (6.7%)
- Denver had the largest number of votes.
- The candidates were: 
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23% of the vote and 85,213 number of votes.
    - Diana DeGette received 78.8% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
    - Diana DeGette, who received 78.8% of the vote and 272,892 number of votes.

## Election Audit Summary
This script can be used as a basis for further elections within Colorado as is but we could also expand it to provide some further information to the commission. 

# 1. Which candidate got most votes in which county:
-  To do this we would need to create another dictionary to track candidate votes per county. Then within the for loop to read data, we could use an if statement to check if the candidate and county exist in the candidate_county_votes dictionary, if not add it and begin to track votes and increase the vote count by 1. Once the for loop has completed,this would then be printed to the screen using the dictionary calculated results for each county and candidate.


# 2. Check there are no duplicate Ballot IDs:
- To do this we would need to create a list to hold all ballot Ids. All ballots would checked by reading in the data using </ballot_id = row[1]>. Then using an if - else statement, we could check if the ballot id already exists in the list. If it does not, add it. If it is already there - we could print "Duplicate Ballot Id found" and print the problem ID. This would help to ensure each Ballot Id is unique and there is no chance of false results. 
