"""
Assignment 4 - COMP301
Student: Haris Siddiqi
Sudent #: 301126020
Program: generator.py
Description: Generates and displays sentences using simple grammar and vocabulary. Words are chosen at random.
"""

import random
import csv

def getWords(filename):
    """Returns a tuple with a list of words from a specified file."""
    # Open file
    with open(filename) as file:
        # Read file
        fileText = csv.reader(file)
        # Add contents of file to list
        textList = []
        for row in fileText:
            textList.append(row[0])
    # Return as tuple
    return tuple(textList)

# Get words from files
articles = getWords('articles.txt')
nouns = getWords('nouns.txt')
verbs = getWords('verbs.txt')
prepositions = getWords('prepositions.txt')
adjectives = getWords('adjectives.txt')
conjunctions = getWords('conjunctions.txt')

def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""
    optional = random.choice(['yes', 'no'])
    if optional == 'yes':
        return random.choice(verbs) + " " + nounPhrase() 
    if optional == 'no':
        return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    """Allows the user to input the number of sentences
    to generate."""
    number = int(input("Enter the number of sentences you want: "))
    print()
    for count in range(number):
        print(sentence())
        
main()