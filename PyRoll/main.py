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

winner = max(voted_candidates, key=voted_candidates.get)
print(f"Total Votes: {total_votes}")
print("------------------")
for candidates, votes in voted_candidates.items():
    percentage = votes / total_votes * 100
    print(f"{candidates}: {percentage: 06.3f}% ({votes}) ")
    
print("------------------------------------")
print(f"Winner: {winner}")
print("--------------------------------------")

output_file = os.path.join('Analysis', 'PyPoll_Analysis.txt')
with open(output_file, "w") as file:
    file.write("Election Results\n")
    file.write("------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidates, votes in voted_candidates.items():
        percentage = votes / total_votes * 100
        file.write(f"{candidates}: {percentage: 06.3f}% ({votes})\n")
   
    file.write("----------------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")

print(f"Results have been saved to {output_file}")

#Create a script that analyzes the votes and calculates the following:
#The total number of votes cast: Complete
#A complete list of candidates who received votes: COmplete
#The percentage of votes each candidate won: Complete
# The total number of votes each candidate won: complete
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