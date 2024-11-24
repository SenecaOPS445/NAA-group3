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

# Dictionaries for the campuses
campuses = {
    'York': {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'},
    'Newnham': {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'},
    'Markham': {'Address': '8 The Seneca Way', 'City': 'Markham', 'Country': 'Canada', 'Postal Code': 'L3R5Y1', 'Province': 'ON'},
    'King': {'Address': '13990 Dufferin St', 'City': 'King City', 'Country': 'Canada', 'Postal Code': 'L7B1L7', 'Province': 'ON'}
}


# Output file name
file_name = 'campuses.txt'

