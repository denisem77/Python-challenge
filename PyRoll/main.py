import os
import csv

print("Election Results")
print("-------------------------")


csvpath = os.path.join('Resources', 'election_data.csv')

total_votes = 0
voted_candidates = {}


with open(csvpath) as csvfile:
    pypoll = csv.reader(csvfile, delimiter =",")
    next(pypoll)

    rows = list(pypoll)

    for row in rows:
        total_votes += 1
        candidates = row[2]

        if candidates in voted_candidates:
            voted_candidates[candidates] += 1
        else:
            voted_candidates[candidates] = 1


print(f"Total Votes:  {total_votes}")
print("------------------")
for candidates, votes in voted_candidates.items():
    print(f"{candidates}:  {votes} ")

#Create a script that analyzes the votes and calculates the following:
#The total number of votes cast: Complete
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