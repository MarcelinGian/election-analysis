import csv
##from distutils import text_file
import os

#assign a variable to load a file from a path
file_to_load = '/Users/giannimarco/Desktop/Classwork/Challenges/Module3Challenge/election-analysis/resources/election_results.csv'

#Create a filename (assign a) vairable to a direct path to the file
file_to_save = '/Users/giannimarco/Desktop/Classwork/Challenges/Module3Challenge/election-analysis/analysis/election_analysis.txt'

#open election results and read the file
with open(file_to_load) as election_data:

    #topen election results, read & analyze the data here. create file_reader variable & use "reader" function via the "csv" module
    file_reader = csv.reader(election_data)
    
    #Read & print header row
    headers = next(file_reader)
    print(headers)
    #print each row in th csv file
    ##for row in file_reader:
        ## print(row)
    
    ##print(election_data)

#close the file
##election_data.close()


# Using the open() function with the "w" mode we will write data to the file.
##with open(file_to_save, "w") as txt_file:

    #write some data to the file
    ##txt_file.write("Counties in the Election\n")
    ##txt_file.write("--------------------------\n")
    ##txt_file.write("Arapahoe\nDenver\nJefferson\n")
    
##print(txt_file)

#close the file
##txt_file.close()


# the data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of Candidates who received votes
# 3. the percentage of votes each candidate won
# 4. the total number of votes each candidate won
# 5. the winner of the election based on popular vote
