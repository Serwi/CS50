import sys
import csv

from cs50 import get_string

# Checking for correct number of command-line arguments
if len(sys.argv) != 3:
    sys.exit("Incorrect number of command-line arguments")

# Loading data from CSV file into memory as List of Dictionaries
people = []
with open(sys.argv[1]) as file:
    reader = csv.DictReader(file)
    for row in reader:
        people.append(row)

# Loading sequence from TXT file into memory as String
with open(sys.argv[2]) as file:
    dna = file.read()

# Making Dictionary for dna_strs
dna_strs = {key: 0 for key in people[0].keys() if key != 'name'}

# Counting longest consecutive repeats for dna_strs
for dna_str in dna_strs:
    dna_strs[dna_str] = str(*[i for i in range(len(dna)) if dna_str * i in dna and dna_str * (i + 1) not in dna])
    
# Searching for matching person DNA
for person in people:
    if all(person.get(key, None) == val for key, val in dna_strs.items()): 
        print(person['name'])
        sys.exit()
        
print("No match")

