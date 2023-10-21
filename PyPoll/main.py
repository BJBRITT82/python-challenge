import csv
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "Resources\\election_data.csv")
output_file = os.path.join(dirname, "bb_election_analysis.txt")

# Open csv file 
with open(filename, "r") as csv_file:
    csvreader = csv.reader(csv_file, delimiter = ",")
    header = next(csvreader)
    
    ballot_ind = header.index("Ballot ID")
    county_ind = header.index("County")
    candidate_ind = header.index("Candidate")

    total_votes = 0
    candidates = {}
    max_votes = 0
    winner = ""

    for row in csvreader:
        candidate = row[candidate_ind]
        total_votes += 1
        # Get candidates
        if candidate not in candidates:
            candidates[candidate] = 0

        # Count votes for each candidate
        candidates[candidate] += 1

        if candidates[candidate] > max_votes:
            max_votes = candidates[candidate]
            winner = candidate

with open(output_file,'w') as output:
    # Print results 
    print("Election Results")
    print("-----------------------------")
    print(f"Total Votes: {total_votes}")
    print("-----------------------------")
    # Write results
    output.write("Election Results\n")
    output.write("-----------------------------\n")
    output.write(f"Total Votes: {total_votes}\n")
    output.write("-----------------------------\n")

    # Calculate percent votes
    for candidate in candidates:
        votes = candidates[candidate]
        percentage = round(votes/total_votes*100,3)
        
        print(f"{candidate}: {percentage}% votes")
        output.write(f"{candidate}: {percentage}% votes\n")

    print("-----------------------------")
    print(f"Winner: {winner}")
    print("-----------------------------")

    output.write("-----------------------------\n")
    output.write(f"Winner: {winner}\n")
    output.write("-----------------------------\n")

