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
    for text in file:
        dna = text

# Making Dictionary for dna_strs and setting their values to 0
dna_strs = {}
for person in people:
    for key in person:
        if key != 'name':
            dna_strs[key] = 0
    break

# Counting longest consecutive repeats for dna_strs
for dna_str in dna_strs:
    count = 1
    while True:
        if count * dna_str in text:
            count += 1
            dna_strs[dna_str] += 1
        else:
            break

# Searching for matching person DNA
for person in people:
    found = True
    for dna_str in dna_strs:
        if int(person[dna_str]) != dna_strs[dna_str]:
            found = False
    if found == True:
        print(person['name'])
        sys.exit()
print("No match")

