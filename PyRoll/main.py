import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)




#Create a script that analyzes the votes and calculates the following:
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote

# These are the results:
# Election Results
# -----------------
# Total Votes: 369711
# --------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -----------------------------------------
# Winner: Diana DeGette
# ------------------------------------