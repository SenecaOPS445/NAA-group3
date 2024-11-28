#!/usr/bin/env python3


# Assignment2
# Group3
# Student Name: Nishan Gharti

import sys
import os

def alp_order(file_name):
  try:
    f = open(file_name, 'r') # Opens the file in read mode
    lines = f.readlines() # Read all the lines from the file
    students = [] # Creating a list to store student data
    for line in lines:
      name_split = line.strip().split(',') # Split the line by commas
      if len(name_split) > 1: 
        full_name = name_split[0].strip() # Extracting the full name
        first_name, last_name = full_name.split()[:2] # Splits it into first and last name
        name_format = f"{last_name} {first_name.strip()}" # To change the name format as lastname firstname
        students.append((last_name, name_format)) # Append it to the list student
    students.sort() # Sorts the name by lastname of the students in alphabetical order
    for student in students:
      print(student[1].strip()) # prints the name 
          
  except FileNotFoundError: # To chevck if the file exists or not and handle the error.
      print(f"Error: The file '{file_name}' does not exits")


def find_student(file_name):
  try:
      f = open(file_name, 'r') # Open the file in read mode
      lines = f.readlines() # read all the lines from the provided file.

      student_info = input('Enter the student name or ID: ').strip().lower() # Prompts the user for input to search for specific student.
      for line in lines:
       if student_info in line.lower(): # To check if the input info matches any part of the line or not.
        print( line.strip()) # Prints out the match info.
  except FileNotFoundError: # To check if the file exists or not and handle error.
       print(f"Error: The file '{file_name}' does not exits")



  


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

