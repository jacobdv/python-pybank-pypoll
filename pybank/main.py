import os
import csv

# path to budget_data.csv
bank_csv = os.path.join("resources", "budget_data.csv")

# opens budget_data.csv
with open(bank_csv) as csv_file:
    # tells csv to use commas to break lines
    csv_reader = csv.reader(csv_file, delimiter=",")

    # starts csv reader
    csv_header = next(csv_file)

    # prints header row from csv file
    # MAY BE REMOVED OR MODIFIED FOR BETTER FORMATTING LATER
    print(f"Header: {csv_header}")

    months = 0
    net_change = 0
    average_change = 0

    # loops through budget_data.csv rows
    for row in csv_reader:
        months = months + 1
        net_change = net_change + float(row[1])
        
    average_change = "${:,.2f}".format(net_change / months)

# The Total Number of Months
print(f"There are {months} months in this dataset.")

# The Net Total Amount of Profits/Losses
print(f"The net change for this time period was ${float(net_change)}.")

# The Average Change for Profits/Losses
print(f"The average change was {average_change} for this period of time.")

# The Greatest Increase in Profits


# The Greatest Decrease in Losses