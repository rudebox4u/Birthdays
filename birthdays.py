import getopt
import os
import sys
import json
import datetime
import calendar

filePath = './birthdays.json'


class Birthday:
    def __init__(self, n, m, d):
        self.name = n
        self.month = m
        self.day = d


# DEFAULT FUNCTIONALITY FOR WHEN THE PROGRAM IS GIVEN NO ARGUMENTS
# Checks to see if a birthday is within 33 days and outputs it to the terminal if so.
def no_arguments(birthdays):
    # Get today's date
    todays_date = datetime.date.today()
    leap_year = False
    if calendar.isleap(todays_date.year):
        leap_year = True
    for b in birthdays:
        d = int(b.day)
        if not leap_year:
            if int(b.month) == 2 and d == 29:
                d = d-1
        birthday_date = datetime.date(todays_date.year, int(b.month), d)
        # if today > birthday, set birthday to next year.
        if todays_date > birthday_date:
            next_year = todays_date.year + 1
            birthday_date = datetime.date(next_year, b.month, d)
        # Compare today's date to birthday and return days until
        delta = birthday_date - todays_date
        difference = delta.days
        # If delta < 33 days = output message to terminal
        if delta.days < 33:
            print(b.name + "'s birthday is in", difference, "days.")


def day_is_valid(d, m):
    # Allow leap year as year is never asked for
    if d == 29 and m == 2:
        print("returning true")
        return True
    else:
        today = datetime.date.today()
        try:
            x = datetime.date(today.year, m, d)
            return True
        except:
            print("returning false")
            return False


# Function for adding a new birthday
def add(birthdays):
    # TAKE INPUT FROM CONSOLE AND CHECK IF THE DATA ENTERED IS BOTH NUMERIC AND A VALID DATE
    name = input("Enter the person's name: ")
    # CHECK IF MONTH IS VALID
    month_is_valid = False
    while not month_is_valid:
        month = input("Enter the month of {}'s birthday: ".format(name))
        if month.isnumeric() and 0 < int(month) < 13:
            month_is_valid = True
        else:
            print("Please enter a valid number between 1 and 12 to represent the month.")
    # CHECK IF DAY IS VALID
    valid = False
    while not valid:
        day = input("Enter the date (day) of their birthday: ")
        if day.isnumeric() and day_is_valid(int(day), int(month)):
            valid = True
        else:
            print("Please enter a valid number that represents a valid day in {}.".format(month))
    # CONFIRM WHETHER DETAILS ARE CORRECT
    loop = True
    should_commit = False
    while loop:
        case = input("Please confirm (Y/N) you would like to add a reminder for {}'s birthday on {}/{} every year: "
                     .format(name, day, month))
        commit = case.lower()
        if commit == 'y' or commit == 'yes':
            print('Committing Birthday')
            should_commit = True
            loop = False
        elif commit == 'n' or commit == 'no':
            print('Birthday has not been committed')
            should_commit = False
            loop = False
        else:
            print("Please type yes or no. ")
    if should_commit:
        new_birthday = Birthday(name, month, day)
        birthdays.append(new_birthday)
    return birthdays


def with_arguments(leftovers, birthdays):
    # Returns birthdays array
    short_arguments = "aph"
    long_arguments = ["add", "print", "help"]
    try:
        arguments, values = getopt.getopt(leftovers, short_arguments, long_arguments)
    except getopt.error as errorCode:
        print("Please run the program again with a valid argument. -a to add, -p to print, -h for help.")
        sys.exit(2)
    for a, v in arguments:
        if a in ("-a", "--add"):
            print("You have chosen add")
            updated = add(birthdays)
            return updated
        elif a in ("-p", "--print"):
            print("You have chosen to print all birthdays.")
            for b in birthdays:
                print(b.__dict__)
            return birthdays
        elif a in ("-h", "--help"):
            print("You have chosen help.")
            # echo readme
            return birthdays


# OPEN TEXT FILE FOR READ AND WRITE OR CREATE FILE IF IT DOES NOT EXIST
if os.path.isfile(filePath):
    text_file = open(filePath, 'r+')
    birthdayDict = json.load(text_file)  # [{},{}]
    # Convert dict objects into birthday objects and put into an array
    birthdaysArray = []
    for birthday in birthdayDict:
        birthdaysArray.append(Birthday(birthday.get('name'), birthday.get('month'), birthday.get('day')))
else:
    # Create file
    print('File does not exist')
    text_file = open(filePath, 'w+')
    # create empty array in text_file
    birthdaysArray = []
    text_file.seek(0)
    json.dump([ob.__dict__ for ob in birthdaysArray], text_file)
# CHECK FOR COMMAND LINE ARGUMENTS AND RUN APPROPRIATE FUNCTIONS
fullArguments = sys.argv
if len(fullArguments) == 1:
    no_arguments(birthdaysArray)
else:
    leftoverArguments = fullArguments[1:]
    updated_array = with_arguments(leftoverArguments, birthdaysArray)
    text_file.seek(0)
    json.dump([ob.__dict__ for ob in updated_array], text_file)
