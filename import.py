import csv
from sys import argv, exit
from cs50 import SQL

db = SQL("sqlite:///students.db")


def main():

    # Checking for correct number of command line arguments
    if len(argv) != 2:
        print("Usage: python import.py data.csv")
        exit(1)

    # Open csv file and input data into dict
    with open(argv[1], "r") as file:
        reader = list(csv.DictReader(file))

        # For each row in CSV file, parse name and insert student into database
        for row in range(len(list(reader))):

            # List of first (middle) and last name
            name = list(reader[row]['name'].split())

            # If name length = 2, set middle name to None
            if len(name) == 2:
                db.execute("INSERT INTO students(first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                           name[0], None, name[1], reader[row]['house'], reader[row]['birth'])

            else:
                db.execute("INSERT INTO students(first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                           name[0], name[1], name[2], reader[row]['house'], reader[row]['birth'])


main()
