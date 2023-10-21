import csv
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "Resources\\budget_data.csv")
output_file = os.path.join(dirname, "bb_finanacial_analysis.txt")

# Open csv file 
with open(filename, "r") as csv_file:
    csvreader = csv.reader(csv_file, delimiter = ",")
    header = next(csvreader)
    
    # Set index for date and profit/loss
    date_ind = header.index("Date")
    profit_loss_ind = header.index("Profit/Losses")
    
    max_profit = float('-inf')
    max_loss = float('inf')

    total_months = 0
    net_total = 0
    
    previous_value = 0
    changes = []
    
    greatest_increase_date = ''
    greatest_increase_value = 0

    greatest_decrease_date = ''
    greatest_decrease_value = 0
    
    for row in csvreader:
        # set current month and value for each row
        current_month = row[date_ind]
        current_value = int(row[profit_loss_ind])
        # Count number of months
        total_months += 1
        # total the profit/loss column
        net_total += current_value
        # Calculate the change in profit/loss
        # start on 2nd row of values to ignore first month value
        if total_months >1:
            change = current_value - previous_value
            changes.append(change)
            # Set greatest increase and decrease values and months
            if change > greatest_increase_value:
                greatest_increase_value = change
                greatest_increase_date = current_month
            if change < greatest_decrease_value:
                greatest_decrease_value = change
                greatest_decrease_date = current_month
        # set current value as new previous value
        previous_value = current_value

# Find average change
    average_change = round(sum(changes)/(total_months-1),2)


        
        


print("Financial Analysis")
print("-----------------------------------")

print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Profit/Loss Changes Each Month: {changes}")
print(f"Average Change: ${average_change}")

print(f"Greatest Increase in Profit: {greatest_increase_date} (${greatest_increase_value})")
print(f"Greatest Decrease in Profit: {greatest_decrease_date} (${greatest_decrease_value})")

# Save output file
with open(output_file, "w") as output:
    output.write("Financial Analysis\n")
    output.write("-----------------------------------\n")

    output.write(f"Total Months: {total_months}\n")
    output.write(f"Total: ${net_total}\n")
    output.write(f"Profit/Loss Changes Each Month: {changes}\n")
    output.write(f"Average Change: ${average_change}\n")

    output.write(f"Greatest Increase in Profit: {greatest_increase_date} (${greatest_increase_value})\n")
    output.write(f"Greatest Decrease in Profit: {greatest_decrease_date} (${greatest_decrease_value})\n")