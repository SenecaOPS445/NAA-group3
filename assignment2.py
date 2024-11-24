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
        students.sort(key=lambda x:x[0]) # Sorts the name by lastname of the students in alphabetical order
        for student in students:
          print( student[1].strip()) # prints the name 
  except FileNotFoundError: # To chevck if the file exists or not and handle the error.
       read_text_file(file_name)


def find_student(file_name):
  try:
      f = open(file_name, 'r') # Open the file in read mode
      lines = f.readlines() # read all the lines from the provided file.

      student_info = input('Enter the student name or ID: ').strip().lower() # Prompts the user for input to search for specific student.
      for line in lines:
       if student_info in line.lower(): # To check if the input info matches any part of the line or not.
        print( line.strip()) # Prints out the match info.
  except FileNotFoundError: # To check if the file exists or not and handle error.
       read_text_file(file_name)
