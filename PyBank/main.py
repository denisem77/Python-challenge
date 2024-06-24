import os
import csv

print("Financial Analysis")
print("--------------------")   

csvpath = os.path.join('Resources', 'budget_data.csv')
unique_months = set()

net_amount = 0
previous_net = None
changes= [] 
total_months = 0

with open(csvpath) as csvfile:
    pybank = csv.reader(csvfile, delimiter = ",")
    next(pybank)

    rows = list(pybank) 

    for row in rows:
        date = row[0]
        Earnings = int(row[1])
        unique_months.add(date)
        net_amount += Earnings

        if previous_net is not None:
            change = Earnings - previous_net
            changes.append(change)
        
        previous_net = Earnings
        total_months += 1
      
    total_months = len(unique_months)
    avg_change = sum(changes) / len(changes) if changes else 0

    print(f"Total Months: {total_months}")
    print(f"Total: ${net_amount}")
    print(f"Average Change: ${avg_change: .2f}")

    

 

    
    #    Title: Financial Analysis
    # ------------------------------
    # The total number of months included in the dataset:complete
    # The net total amount of "Profit/Losses" over the entire period: complete
    # The changes in "Profit/Losses" over the entire period, and the the average of those changes
    # The greatest increase in profits (date and amount) over the entire period.
    # The greatest decrease in profits (date and amount) over the entire period.
    

    #  It should look like this:
    # Title
    # --------
    # Total Months: 86
    # Total: $22564198
    # Average Change: $-8311.11
    # Greatest Increase in Profits: Aug-16 (1862002)
    # Greatest Decrease in Profits: Feb-14 (-1825558)

    # In addition the final script should print the analysis to the terminal and export a text file with results.