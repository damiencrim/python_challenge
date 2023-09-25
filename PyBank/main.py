import os
import csv

budget_csv = os.path.join("Resources","budget_data.csv")
months=[]
profits=[]
change_list=[]
counter=0
date=0


# Open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Read the header row first
    csv_header = next(csv_reader)
    
    # Read through each row of data after the header
    for row in csv_reader:
        
        months.append(row[0])
        profits.append(int(row[1]))
        if counter >0:
            current_value=(int(row[1]))
            change=current_value - previous_value
            change_list.append(change)
            
           
        counter += 1
        previous_value=(int(row[1]))


 # Find Total Number of Months
total_months = len(months)

# Find Total Profit
total_profit = sum(profits)

# Find Average Change
average_change=round(sum(change_list)/len(change_list),2)

# Find Greatest Increase and Decrease in Profits

greatest_increase=max(change_list)
greatest_decrease=min(change_list)


#print(greatest_increase)
#print(greatest_decrease)


# Produce Summmary of Output


output=(
    
    f"Financial Analysis\n"
f"----------------------------\n"
f"Total Months: {total_months}\n"
f"Total: ${total_profit}\n"
f"Average Change: ${average_change}\n"
f"Greatest Increase in Profits:$({max(change_list)})\n"
f"Greatest Decrease in Profits:$({min(change_list)})\n"

)

# Print Output of Findings to Text

print(output)
budget_txt = os.path.join("analysis","budget_analysis.txt")
with open(budget_txt,"w") as txt_file:
    txt_file.write(output)

