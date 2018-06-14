import os
import csv

file_name = os.path.join('/Users/michaelduffner/GWDC201805DATA3-Class-Repository-DATA/Homework/03-Python/Instructions/PyPoll/raw_data/election_data_1.csv')

voter_id = []
names = []

with open(file_name,'r') as f:
    csvreader = csv.reader(f, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        voter_id.append(row[0])
        names.append(row[2])

    num_votes = len(voter_id)

#use "set" to find unique values 

    my_set = set(names)

#transform "my_set" into a list

    candidate_list = list(my_set)

    candidate_list = (sorted(candidate_list))

    name_sort = (sorted(names))

    tally = []
    percent = []

    for row in candidate_list:
        row_counter = name_sort[row]
        tally[row] = row_counter
        percent[row] = (tally[row]/num_votes)

   # votes = 
   # winner =
        





