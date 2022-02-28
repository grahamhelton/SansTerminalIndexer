#! /bin/python3
import csv
import os
import signal 
import pandas as pd
from colorama import Fore, Style

headers = ['Title', 'Description','Page','book']
index = []
row = []
book = "1"
dic = {}
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

print(tick, "Welcome to Sans Terminal Indexer")
print(tick, "Setting default book number to 1")
print(tick, "Enter \"new book\" to change to the next book")

# Handle control+c
def handler(signum, frame):
    print(red, "Exiting")
    exit(0)
signal.signal(signal.SIGINT, handler)

# Kick off program, check if any .csv files are in directory, if not, prompt user to create one
def init():
    count = 0
    csvCheck = os.listdir('.')
    for i in csvCheck:
        if(i.endswith(".csv")):
            print(tickInfo,"CSV Exists in current directory, which would you like to use? ")

            for i in os.listdir():
                count+=1
                dic[count]=i
            print(sep)
            # For each value, assign a key from 1-n. This will allow the user to select a number that corresponds to the csv file
            for key, value in dic.items():
                print(green, key, red,'-->', cyan , value, reset)
            print(sep)
            print(green, "0", red,  "-->" + cyan +  "  New index")
            selection = input(tick + green + " Type the number of the file you would like\n" + reset)
            # If selecing existing csv, exit function
            if selection != "0":
                csvName = dic[int(selection)]
                print(tick, "You chose: ", csvName)
                return csvName 
            # If selection is to create a new CSV, carry on with creating it
            else:
                csvName = input(tick + yellow + "What do you want to name your CSV file?\n" + reset)
                if not csvName.endswith(".csv"):
                    csvName += ".csv"
                with open(csvName, 'a') as f:
                    write = csv.writer(f)
                    write.writerow(headers)

                print(csvName)
                return csvName

def writeCsv():
    with open(csvName, 'a') as f:
        write = csv.writer(f)
        write.writerows(index)
def readIndex(csvName):
    print(tick, "Displaying abbreviated entries")
    df = pd.read_csv(csvName)
    #bottom = df.tail()
    print(df)

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





















