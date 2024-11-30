#!/usr/bin/env python3
# Project Name: Assignment 2
# Group 3
# Student Name: Juliana Giammarco

import sys, os

def campus(file_name):

    campus_search = input('Enter the Campus: (York, Markham, Newnham, King): ').strip().lower()
    if campus_search not in ['york', 'markham', 'newnham', 'king']:
        print('Invalid Entry. Must be York, Markham, Newnham or King')
        sys.exit()
 
    try:
        with open('campus.txt', 'r') as file: #opens campus.txt                            campus_data = file.readlines() #reads the lines
            seneca_campuses = [campus_name.strip() for campus_name in campus_data] 
            for campus_name in seneca_campuses:
                if campus_search in campus_name.lower():
                    print(f"Details for {campus_search.capitalize()} campus: {campus_name}")
       
        with open(file_name, "r") as file: #opens user_test.txt
            data = file.readlines()  # Read all lines from the file
            # Initialize an empty dictionary to store campus counts
            campus_details = {}
            # Process each line in the file
            for line in data:
                campus_comp = [comp.strip(" '") for comp in line.strip().split(",")]
                if len(campus) < 8:  # Ensure there are enough fields
                    continue  # Skip invalid lines with insufficient data
            campus = campus_comp[2]
            # Count occurrences of each transportation mode
            campus_details[campus] = campus_details.get(campus, 0) + 1
       
        return campus_details  # Return the summary as a dictionary
    except FileNotFoundError:
        print("Error: The file 'user_test' was not found.")
        return {}




