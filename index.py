#! /bin/python3
import csv
import os
from os.path import expanduser
import signal 
import pandas as pd
from colorama import Fore, Style

headers = ['Title', 'Description','Page','book']
index = []
row = []
dictionary = {}
# Define formatting
reset = Style.RESET_ALL
red = Fore.RED
cyan = Fore.CYAN
green = Fore.GREEN
yellow = Fore.YELLOW
purple = Fore.MAGENTA
sep = Fore.BLUE + "---------------------------" + reset
tick = Fore.BLUE + "[" + Fore.GREEN + "+" + Fore.BLUE + "]" + reset
tickBad = Fore.YELLOW + "[" + Fore.RED + "X" + Fore.YELLOW+ "]" + reset
awaitingInput = Fore.BLUE + "-----" + Fore.GREEN + "> " + reset
tickInfo = Fore.BLUE + "[" + yellow + "!" + Fore.BLUE + "]" + reset

os.system("clear")
print(tick, "Welcome to Sans Terminal Indexer")
print(tick, "Enter" , green, "\"new book\"" , reset, "to change to the next book")
book = input("Which book are you currently working on?\n")
def path():
    home = expanduser("~")
    path = '/.Indexes/'
    if not os.path.exists(home+path):
        print("~/.Indexes Does not exist! Creating .Index directory in your home folder!")
        os.mkdir(home+path)

    os.chdir(home+path)

# Handle control+c
def handler(signum, frame):
    os.system("clear")
    print(red, "Exiting")
    exit(0)
signal.signal(signal.SIGINT, handler)

# Kick off program, check if any .csv files are in directory, if not, prompt user to create one
def init():
    os.system("clear")
    path()
    count = 0
    csvCheck = os.listdir()
    print(csvCheck)

    # If a .csv file exists in the current directory (~.Indexes) then prompt user for which one they would like to use
    for i in csvCheck:
        print("printing elements", i)
        if (i.endswith(".csv")):
            print(tickInfo,"CSV Exists in current directory, which would you like to use? ")
            # For each file that ends in .csv, add to dictionary, then for each value, assign a key from 1-n.
            # This will allow the user to select a number that corresponds to the csv file.
            for x in os.listdir():
                if x.endswith((".csv")):
                    count+=1
                    dictionary[count]=x
            print(sep)
            # For each key and value, in the dictionary, print key, value for user to select from
            for key, value in dictionary.items():
                print(green, key, red,'-->', cyan , value, reset)
            print(sep)
            print(green, "0", red,  "-->" + cyan +  "  New index")
        
            # Ask the user which file they would like
            selection = input(tick + green + " Type the number of the file you would like\n" + reset)
    
                # If selecing existing csv, set csvName to choice and exit function
            if selection != "0":
                csvName = dictionary[int(selection)]
                print(tick, "You chose: ", csvName)
                return csvName 
            
    csvName = input(tick + green + " Creating a new index, what do you want to name your CSV file?\n" + reset)
        
    if not csvName.endswith(".csv"):
        csvName += ".csv"

    with open(csvName, 'a') as f:
        write = csv.writer(f)
        write.writerow(headers)

    print(tick, "Creating file named: ", csvName)
    os.system("clear")
    return csvName

def writeCsv():
    with open(csvName, 'a') as f:
        write = csv.writer(f)
        write.writerows(index)

def readIndex(csvName):
    os.system("clear")
    print(tick, "Displaying entries for",cyan, csvName,reset)
    df = pd.read_csv(csvName)
    #bottom = df.tail()
    print(df)

# Call init function and assign csvName to a string
csvName = str(init())

# Get user input
while True:
    # Set index and row to null 
    index = []
    row = []
    # Get user input
    newEntry = input(tick + green+" Enter your index entry. Format: Title, Description, Page\n" + reset)
    # Handle input
    if newEntry == "exit":
        writeCsv()
        os._exit(0)
    elif newEntry == "new book":
        book = str(input(yellow + "Enter the book number\n"))

    elif newEntry == "index":
        readIndex(csvName)

    elif newEntry.count(',') != 2:
            print(newEntry.count(','))
            print(tickBad + " Try again, make sure you have 2 commas")
    else: 
        # Clear screen
        os.system("clear")

        # Split user input on commas and put into row variable
        row = newEntry.split(",")

        # Strip whitespace
        strippedRow = [x.strip(' ') for x in row]

        # append the book number to the end of the list 
        strippedRow.append(book)

        # Append row to list called index (This is a list of a lists)
        index.append(strippedRow)
        writeCsv()





















