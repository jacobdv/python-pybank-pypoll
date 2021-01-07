import os
import csv

# path to election_data.csv
election_csv = os.path.join("resources", "election_data.csv")

# opens election_data.csv
with open(election_csv) as csv_file:
    # tells csv to use commas to break lines
    csv_reader = csv.reader(csv_file, delimiter=",")

    # starts csv reader
    csv_header = next(csv_file)

    # basic variable assignments
    total_votes = candidate_votes = 0
    candidate = election_winner = ""
    vote_percentage = 0.0

    # more complex variables
    candidate_list = []

    for row in csv_reader:
        total_votes = total_votes + int(row[0])
        candidate_list.append(str(row[2]))

    candidate_list = set(candidate_list)
    number_of_candidates = len(candidate_list)

    for row in csv_reader:
        candidate_list[candidate]

# console output
print(f"\nElection Results \n------------------- \nTotal Votes: {total_votes:,} \n------------------- \n")

# sends analysis information to a text file in the analysis file
# overwrites if there's a duplicate file already there
budget_data_analysis = open("analysis/election_data_analysis.txt", "w")
budget_data_analysis.write(f"\nElection Results \n------------------- \nTotal Votes: {total_votes:,} \n------------------- \n")
budget_data_analysis.close()