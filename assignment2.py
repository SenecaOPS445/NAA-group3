#!/usr/bin/env python3
# Project Name: Assignment 2
# Group 3
# Student Name: Juliana Giammarco

import sys, os

def campus(file_name, campuses):
    try:
        with open("user_test", "r") as file:
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

    except:
            return campus_details  # Return the summary as a dictionary
