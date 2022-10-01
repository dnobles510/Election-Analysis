# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes of each candidate won
# 4. The total nuber of votes each candidate won.
# 5 . The winner of the election based on popular vote

# Import the datetime class from the datetime module
import datetime
# Use the now() attribute on the datetine class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is", now)

# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # to do : perform analysis
    print(election_data)

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
        
        # To do: read and analyze the data here
        file_reader = csv.reader(election_data)
        # Read and print the header row.
        headers = next(file_reader)
        print(headers)
        #for row in file_reader:
            #print(row)

# Create a filename variablr to a direct or indirect path to  the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the with statement to open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write three counties to the file.
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson")

    # Write three counties to the file.
     txt_file.write("Counties in the Election")
     txt_file.write("\nArapahoe\nDenver\nJefferson")

