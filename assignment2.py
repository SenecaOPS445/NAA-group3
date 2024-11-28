#!/usr/bin/env python3
#Project Name: Assignment 2
#Group 3
#Student Names: Saira Munawar, Nishan, Juliana

import sys, os, datetime, shutil

def school_folder(folder_path):
    '''Creates the school folder if it does not exit.'''
    if os.path.isdir(folder_path): #using os.dir to find school_folder in the a2assignment
        return folder_path + ' exists'
    else:
        os.mkdir(folder_path) #creates the folder otherwise
        return folder_path + ' has been created.'

def usage():
    '''prints messages to users'''
    if len(sys.argv) != 3:
        print('USAGE: ' + sys.argv[0] + ' File_Name' + ' Options') #if the user does not use 3 arguments: filename + options + program name
        sys.exit() 
    else:
        file_name = sys.argv[1]
        option = sys.argv[2]
        management(file_name, option) #call the management function

def read_text_file(file_name):
    '''opens the file given by the user'''
    if os.path.isfile(file_name): #checks if the file is found
        return 'File found!'
    else:
        print('File not found')
        sys.exit()
#        return 'File not found' #prints the error message if file doesn't exist

def management(file_name, option):
    '''This function organizes the file based on the user's input'''
    '''Options are: alphabetical, dietary, transportation, program name, elective, campus'''
    file_content = read_text_file(file_name) #checks if the file exist
    print(file_content) 
    print('option: ', sys.argv[2])
    if option.lower() == 'a' or option.lower() == 'alphabetical':
        alp_order(file_name)
    elif option.lower() == 'p' or option.lower() == 'program':
        program_name(file_name)
    elif option.lower() == 'e' or option.lower() == 'elective':
        elective(file_name)
    elif option.lower() == 'c' or option.lower() == 'campus':
        campus(file_name)
    elif option.lower() == 't' or option.lower() == 'transportation':
        transportation(file_name)
    elif option.lower() == 'd' or option.lower() == 'dietary':
        dietary(file_name)
    elif option.lower() == 's' or option.lower() == 'student':
        find_student(file_name)
    else:
        print('Please enter an option (Alphabetical (a), Program (p), Elective (e)')
        print('Campus (c), Transportation (t), Dietary (d), Student (s)')
        
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

def campus(file_name):
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
      
def program_name(file_name):

def elective(file_name):

def campus(file_name):
  try:
        with open("user_test", "r") as file:
            data = file.readlines()  # Read all lines from the file