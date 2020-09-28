import csv
from sys import argv, exit
from cs50 import SQL

db = SQL("sqlite:///students.db")


def main():

    # Checking for correct number of command line arguments
    if len(argv) != 2:
        print("Usage: python roster.py housename")
        exit(1)

    # Set house to the required string
    house = argv[1]

    # Query database and order by last and then first name
    studentdb = db.execute("SELECT * FROM students WHERE house = (?) ORDER BY last, first", house)

    # Print people in the given house
    for student in studentdb:
        if student['middle'] == None:
            print(f"{student['first']} {student['last']}, born {student['birth']}")
        else:
            print(f"{student['first']} {student['middle']} {student['last']}, born {student['birth']}")


main()
