import os 
import csv

def create_separator(char, count):
    sepline = str(char) * count
    return sepline

def display_results(candidates):
    total_votes = sum(candidates.values())

    print(f'Total Votes: {total_votes}')

    for candidate, votes in candidates.items():
        vote_percent = round((votes / total_votes) * 100)
        print(candidate + ": " + str(vote_percent) + '% (' + str(votes) + ')')

    #print(create_separator,"-",25)commented out because made code look weird 

    winner = max(candidates, key=lambda key: candidates[key])

    print(f"Winner: {winner}")  
    print('\n') 

def writeoutput(cadidates):

   outfile = 'output.txt'          

   # Opens the output file 

   with open(outfile, 'a') as file_object:
       

       file_object.write(create_separator('-', 25) + '\n')

       # Calcualtes total votes by summing values in dictionary

       totalvotes = sum(candidates.values())

       # Writes total votes to output file

       file_object.write("Total Votes: " + str(totalvotes) + '\n')

       file_object.write(create_separator('-', 25) + '\n')

       # Iterates through key-value pairs in dictionary

       for candidate, votes in candidates.items():
           # Calculates percentage of votes for each candidate

           cand_percent = round(((votes / totalvotes) * 100), 1)

           # summary line for output file 

           file_object.write(candidate + ": " + str(cand_percent) + '% (' + str(votes) + ')' + '\n')

       file_object.write(create_separator('-', 25) + '\n')

       #find the max value in the dictionary 
       #lambda is a way to use a sort function in a dictionary 

       winner = max(candidates, key=lambda key: candidates[key])

       # Writes winner to output file
       #Use '\n' to write a new line 

       file_object.write("Winner: " + winner + '\n')

       file_object.write(create_separator('-', 25) + '\n')

       file_object.write('\n')         

#import files 

files = ['election_data_2.csv','election_data_1.csv']

for filename in files:                  
   candidates = {}  

   # Specifies import path and file

   csv_in = os.path.join(".", "raw_data", filename)

   # Read csv and opens file 

   with open(csv_in, newline="") as csvfile:
       csvreader = csv.reader(csvfile, delimiter=",")
       
       #skip header row in csv

       next(csvreader)                 

       # Iterates through each row in csv

       for row in csvreader:



           if row[2] not in candidates:

               candidates[row[2]] = 0

           candidates[row[2]] += 1     

   display_results(candidates)           

   writeoutput(candidates)             

