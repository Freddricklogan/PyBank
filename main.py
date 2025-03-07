# PyBank Financial Analysis
import os
import csv

# Path to collect data from the Resources folder
budget_data_csv = os.path.join("Resources", "budget_data.csv")

# Variables for financial analysis
total_months = 0
net_total = 0
previous_profit_loss = None
profit_changes = []
dates = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Read the CSV file
with open(budget_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row
    header = next(csvreader)
    
    # Loop through rows
    for row in csvreader:
        # Date and Profit/Loss values
        date = row[0]
        profit_loss = int(row[1])
        
        # Count months
        total_months += 1
        
        # Net total
        net_total += profit_loss
        
        # Calculate change in profit/loss
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            profit_changes.append(change)
            dates.append(date)
            
            # Check for greatest increase
            if change > greatest_increase[1]:
                greatest_increase = [date, change]
                
            # Check for greatest decrease
            if change < greatest_decrease[1]:
                greatest_decrease = [date, change]
        
        # Update previous profit/loss
        previous_profit_loss = profit_loss

# Calculate average change
average_change = sum(profit_changes) / len(profit_changes)

# Generate analysis report
analysis = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

print(analysis)

# Export results to text file
output_path = os.path.join("analysis", "financial_analysis.txt")
with open(output_path, "w") as txt_file:
    txt_file.write(analysis)

print(f"Analysis exported to {output_path}")
