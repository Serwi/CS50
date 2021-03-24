import sys
import csv
import argparse

parser = argparse.ArgumentParser(description = 'Identifies a person based on their DNA', usage = 'python dna.py data.csv sequence.txt' )
parser.add_argument('database', help = 'CSV file containing STR counts for a list of individuals')
parser.add_argument('dna_sequence', help = 'text file containing dna to analyze')
args = parser.parse_args()

# Loading data from CSV file into memory as List of Dictionaries
people = []
with open(args.database) as file:
    reader = csv.DictReader(file)
    for row in reader:
        people.append(row)

# Loading sequence from TXT file into memory as String
with open(args.dna_sequence) as file:
    dna = file.read()

# Making Dictionary for dna_strs
dna_strs = {key: 0 for key in people[0].keys() if key != 'name'}

# Counting longest consecutive repeats for dna_strs
for dna_str in dna_strs:
    count = 0
    while count * dna_str in dna:
        count += 1
    dna_strs[dna_str] = str(count - 1)
    
# Searching for matching person DNA
for person in people:
    if all(person.get(key, None) == val for key, val in dna_strs.items()): 
        print(person['name'])
        sys.exit()
        
print("No match")

