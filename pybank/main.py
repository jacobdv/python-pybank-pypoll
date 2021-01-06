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

    # variables for basic calculations: months, average change, net change
    months = average_change = net_change = 0 

    # dictionary and variables for greatest increase and decrease and their corresponding month/year pairings
    dates = []
    profit_change = []
    greatest_increase = greateset_decrease = 0
    increase_month = decrease_month = ""

    # loops through budget_data.csv rows
    for row in csv_reader:
        months = months + 1
        net_change = net_change + float(row[1])

        # creates a list of months and a list of profit changes
        dates.append(row[0])
        profit_change.append(float(row[1]))

    # finds the greatest increase and decrease and pulls their corresponding month/year as a string
    increase_month = str(dates[int(profit_change.index(max(profit_change)))])
    decrease_month = str(dates[int(profit_change.index(min(profit_change)))])

    # formats all money values as currency      
    average_change = "${:,.2f}".format(net_change / months)
    net_change = "${:,.2f}".format(net_change)
    greatest_increase = "${:,.2f}".format(max(profit_change))
    greateset_decrease = "${:,.2f}".format(min(profit_change))

# prints two header rows, followed by five data values:
# {Months, Total, Average Change, Greatest Increase Month, Greatest Decrease Month}
print(f"\nFinancial Analysis \n------------------- \nMonths: {months} \nNet Total: {net_change} \nAverage Change: {average_change} \nGreatest Profit Increase: {increase_month} ({greatest_increase}) \nGreatest Profit Decrease: {decrease_month} ({greateset_decrease})\n")

# sends analysis information to a text file in the analysis file
# overwrites if there's a duplicate file already there
budget_data_analysis = open("analysis/budget_data_analysis.txt", "w")
budget_data_analysis.write(f"Financial Analysis \n------------------- \nMonths: {months} \nNet Total: {net_change} \nAverage Change: {average_change} \nGreatest Profit Increase: {greatest_increase} \nGreatest Profit Decrease: {greateset_decrease}")
budget_data_analysis.close()
