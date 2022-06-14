import csv
##from distutils import text_file
import os

#assign a variable to load a file from a path
file_to_load = '/Users/giannimarco/Desktop/Classwork/Challenges/Module3Challenge/election-analysis/resources/election_results.csv'

#Create a filename (assign a) vairable to a direct path to the file
file_to_save = '/Users/giannimarco/Desktop/Classwork/Challenges/Module3Challenge/election-analysis/analysis/election_analysis.txt'

# Initialize a total vote counter, set equal to zero
total_votes = 0

# Declare a new empty LIST as candidate_options
candidate_options =[]

# Declare new empty DICTIONARY as candidate_votes
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open election results and read the file
with open(file_to_load) as election_data:

    # read & analyze the data here. create file_reader variable & use "reader" function via the "csv" module
    file_reader = csv.reader(election_data)
    
    #Read the header row
    headers = next(file_reader)
    
    #print each row in th csv file
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Print thte candidate name from each row
        candidate_name = row[2]
        # IF the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        #Aalign with IF statement (so: outside of IF statement) so candidate's vote count is incremented as we iterate through each row
        candidate_votes[candidate_name] += 1

        #TEST
        county_name = row[1]
        print(county_name)
    
# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:

# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    
    # Save the final vote count to the text file.
    txt_file.write(election_results)
        
    # Determine the percentage  of votes for each candidate by looping through the counts..:
    # a. Iterate through he candidate list.
    for candidate_name in candidate_votes:
        # b. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # c. Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        
        # Print out each candidate's name, vote count, and percentage pf votes to the termina
        ##print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # ^ above code is now modified to add to a text file. take code out of 'print()' function and place in a variable
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        #print each candidate, their vote count, and percentage to the terminal.
        print(candidate_results)
        #save the candidate results to the text file.
        txt_file.write(candidate_results)

        # TO Determin the winning vote count and candidate..:
        # a. Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # b. If true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # c. And, set the winning_candidate equal to candidate's name>
            winning_candidate = candidate_name

    # Print out the winning candidate, vote count, and percentage to terminal.
    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winnig Vote Count: {winning_count:,}\n"
        f"Winning Percntage: {winning_percentage:.1f}%\n"
        f"---------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)










# Print the candidate name and percentage votes
##print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote.")

# Print the candidate vote dictionary
##print(candidate_votes)      

#Add a print statement that is flush with the left margin to print out the candidate_options list.
##print(candidate_options)

#Print the total votes.
##print(total_votes)
    
    ##print(election_data)

#close the file
##election_data.close()




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
