#! /bin/python3
import csv
import os
import signal 
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

print(tick, "Welcome to indexer")
print(tick, "Setting default book number to 1")
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
            for key, value in dic.items():
                print(key, ' : ', value)
            selection = input(tick + green + " Type the number of the file you would like\n" + reset)

            csvName = dic[int(selection)]
            print(tick, "You chose: ", csvName)

            return csvName 

    print("CSV Does not Exist")
    csvName = input(tick + yellow + "What do you want to name your CSV file?\n" + reset)
    if not csvName.endswith(".csv"):
        csvName += ".csv"
        print(csvName)
    with open(csvName, 'a') as f:
        write = csv.writer(f)
        print("Adding headers")
        write.writerow(headers)

    print(csvName)
    return csvName

def writeCsv():
    with open(csvName, 'a') as f:
        write = csv.writer(f)
        write.writerows(index)

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

    elif newEntry.count(',') != 2:
            print(newEntry.count(','))
            print(tickBad + " Try again, make sure you have 2 commas")
    else: 
        # Clear screen
        os.system("clear")
        # Split user input on commas and put into row variable
        row = newEntry.split(",")
        # append the book number to the end of the list 
        row.append(book)
        # Append row to list called index (This is a list of a lists)
        index.append(row)
        writeCsv()
