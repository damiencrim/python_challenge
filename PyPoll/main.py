import os
import csv

# Set Path for Directory
election_csv = os.path.join("Resources","election_data.csv")



# Open and read csv
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Read the header row first
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    # Declare Variables to hold
    total_votes = []
    candidates = []
    stockham = []
    degette = []
    doane = []
    stockham_votes = 0
    degette_votes = 0
    doane_votes = 0
    total_votes = 0

# Read through each row of data after the header
    for row in csv_reader:
        # total_votes.append(int(row[0]))
        # candidates.append(row[2])
        total_votes += 1
   
    # total_votes = (len(total_votes))

   # Find Candidates in Poll
        
        

        # Tally number of Votes per Candidate
    for row in csv_reader:

        if candidates == "Charles_Casper_Stockham":
            stockham.append(candidates)
            stockham_votes = len(stockham)

        elif candidates == "Diana_DeGette":
            degette.append(candidates)
            degette_votes = len(degette)

        else:
            candidates == "Raymon_Anthony_Doane"
            doane.append(candidates)
            doane_votes = len(doane)

    print(stockham_votes)
    print(degette_votes)
    print(doane_votes)

    

# Find Percentages of the Vote
stockham_percent = (stockham_votes)/(total_votes) * 100, 3
degette_percentage = (degette_votes)/(total_votes) * 100, 3
doane_percent = (doane_votes)/(total_votes) * 100, 3


# Find Winner of the Election
if stockham_percent > degette_percentage and doane_percent:
        winner = "Charles_Casper_Stockham"

elif degette_percentage > stockham_percent and doane_percent:
        winner = "Diana_DeGette"
else:
        winner = "Raymon_Anthony_Doane"





       


output=(

    f"Election Results\n"

f"-------------------------------\n"
f"Total Votes: (len(votes))\n"
f"-------------------------------\n"
f"Charles Casper Stockham: {stockham_percent}{stockham_votes}\n"
f"Diana DeGette: {degette_percentage}{degette_votes}\n"
f"Raymon Anthony Doane: {doane_percent}{doane_votes\n"
f"---------------------------------\n"
f"Winner: {winner}"
f"---------------------------------\n"

)

# Print Results of Vote to Text

print(output)
election_txt = os.path.join("Resources","election_data.csv")
with open(election_txt, "w") as txt_file:
    txt_file.write(output)


        





     