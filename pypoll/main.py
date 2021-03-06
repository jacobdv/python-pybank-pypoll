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
    total_votes = 0
    election_winner = ""
    
    # candidates votes
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    o_tooley_votes = 0
    
    # more complex variables
    candidate_list = []

    # sums total votes for each candidate
    for row in csv_reader:
        total_votes = total_votes + 1
        if row[2] == "Khan":
            khan_votes += 1
        elif row[2] == "Correy":
            correy_votes += 1
        elif row[2] == "Li":
            li_votes += 1
        elif row[2] == "O'Tooley":
            o_tooley_votes += 1

    # calculates percentages for candidates and formats it as a percentage
    khan = "{:.0%}".format(khan_votes / total_votes)
    correy = "{:.0%}".format(correy_votes / total_votes)
    li = "{:.0%}".format(li_votes / total_votes)
    o_tooley = "{:.0%}".format(o_tooley_votes / total_votes)
    
    # compares vote totals to decide the winner and set the election_winner to the winner's name
    if khan_votes > correy_votes and li_votes and o_tooley_votes:
        election_winner = "Khan"
    elif correy_votes > khan_votes and li_votes and o_tooley_votes:
        election_winner = "Correy"
    elif li_votes > correy_votes and khan_votes and o_tooley_votes:
        election_winner = "Li"
    elif o_tooley_votes > correy_votes and li_votes and khan_votes:
        election_winner = "O'Tooley"

# prints election results for total votes, individual totals and percentages, and the winner
print(f"\nElection Results \n------------------- \nTotal Votes: {total_votes:,} \n------------------- \nKhan: {khan} ({khan_votes}) \nCorrey: {correy} ({correy_votes}) \nLi: {li} ({li_votes}) \nO'Tooley: {o_tooley} ({o_tooley_votes}) \n------------------- \nWinner: {election_winner} \n------------------- \n")

# sends analysis information to a text file in the analysis file
# overwrites if there's a duplicate file already there
budget_data_analysis = open("analysis/election_data_analysis.txt", "w")
budget_data_analysis.write(f"\nElection Results \n------------------- \nTotal Votes: {total_votes:,} \n------------------- \nKhan: {khan} ({khan_votes}) \nCorrey: {correy} ({correy_votes}) \nLi: {li} ({li_votes}) \nO'Tooley: {o_tooley} ({o_tooley_votes}) \n------------------- \nWinner: {election_winner} \n------------------- \n")
budget_data_analysis.close()
