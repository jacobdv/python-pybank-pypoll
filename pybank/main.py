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

    # variables for basic calculations: months, net change, average change
    months = 0
    average_change = 0
    net_change = 0 

    # dictionary and variables for greatest increase and decrease
    month_profit_dict = {}
    keys = []
    values = []
    greatest_increase = 0
    greateset_decrease = 0
    increase_month = ""
    decrease_month = ""

    # loops through budget_data.csv rows
    for row in csv_reader:
        months = months + 1
        net_change = net_change + float(row[1])

        # creates a list of keys (months) and a list of values (profit change)
        keys.append(row[0])
        values.append(row[1])

    # finds the greatest increase and decrease in the values list
    greatest_increase = max(values)
    greateset_decrease =  min(values)

    # pulls the list position for the greatest increase and decrease
    increase_position = int(values.index(greatest_increase))
    decrease_position = int(values.index(greateset_decrease))

    # pulls the months corresponding with the greatest increase and decrease
    increase_month = str(keys[increase_position])
    decrease_month = str(keys[decrease_position])

    # converts the greatest increase and decrease to floats for conversion to currency format
    greatest_increase = float(greatest_increase)
    greateset_decrease = float(greateset_decrease)

    # formats everything as currency      
    average_change = "${:,.2f}".format(net_change / months)
    net_change = "${:,.2f}".format(net_change)
    greatest_increase = "${:,.2f}".format(greatest_increase)
    greateset_decrease = "${:,.2f}".format(greateset_decrease)

# Prints two header rows, followed by five data values.
# Months, Total, Average Change, Greatest Increase Month, Greatest Decrease Month
print(f"Financial Analysis \n------------------- \nMonths: {months} \nNet Total: {net_change} \nAverage Change: {average_change} \nGreatest Profit Increase: {increase_month} ({greatest_increase}) \nGreatest Profit Decrease: {decrease_month} ({greateset_decrease})")

# Sends analysis information to a text file in the analysis file.
# Overwrites if there's a duplicate file already there.
budget_data_analysis = open("analysis/budget_data_analysis.txt", "w")
budget_data_analysis.write(f"Financial Analysis \n------------------- \nMonths: {months} \nNet Total: {net_change} \nAverage Change: {average_change} \nGreatest Profit Increase: {greatest_increase} \nGreatest Profit Decrease: {greateset_decrease}")
budget_data_analysis.close()