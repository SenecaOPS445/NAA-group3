#!/usr/bin/env python3
# Project Name: Assignment 2
# Group 3
# Student Name: Juliana Giammarco

import sys, os

def campus(file_name, campuses):
    try:
        with open(file_name, 'w') as file:    # Open the file name and writing it
            for campus_name, campus_details in campuses.items():    # Name and details are further details about the campuses
                file.write(f"Campus: {campus_name}\n")    # File will write with the format and will do a new line each time
                for key, value in campus_details.items():
                    file.write(f" {key}: {value}\n")    # Key and values are a part of the dictionaries and will do new lines
                file.write("\n")
    except Error as e:    # Will print error message
        print(f"Campus is not found: {e}")

def search_campus(file_name, campus_name):
    if not os.path.exists(file_name):    # Making sure a file path exists
        print("The campus file does not exist.")
        return

    with open(file_name, 'r') as file:    # To see the output of the file with the campus details
        campus_info = []
        for line in file:
            line = line.strip()    # Will remove any whitespace before or after
            if line.startswith(f"Campus: {campus_name}"):    # Seeing if Campus name exists
                campus_info.append(line)
            elif campus_info and line:    # Has both info and line in the file
                campus_info.append(line)
            elif campus_info and not line:    # Doesn't have both info and line in the file
                break


        if campus_info:    # Seeing if the student goes to a proper campus name
            print("\n".join(campus_info))
            print("Student 1 goes to", campus_name)
        else:
            print(f"The campus '{campus_name}' was not found in the file.")


# Dictionaries for the campuses
campuses = {
    'York': {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'},
    'Newnham': {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'},
    'Markham': {'Address': '8 The Seneca Way', 'City': 'Markham', 'Country': 'Canada', 'Postal Code': 'L3R5Y1', 'Province': 'ON'},
    'King': {'Address': '13990 Dufferin St', 'City': 'King City', 'Country': 'Canada', 'Postal Code': 'L7B1L7', 'Province': 'ON'}
}


def main():
    if __name__ == "__main__":
    # Output file name
        file_name = 'campuses.txt'
        campus(file_name, campuses)

    # Asking user for a search and using the search variable to go through the file and search
        search_name = input("Enter the campus name you want to search for: ")
        search_campus(file_name, search_name)

