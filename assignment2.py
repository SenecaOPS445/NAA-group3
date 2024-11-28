#!/usr/bin/env python3
<<<<<<< HEAD
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
=======
#Project Name: Assignment2
#Group 3

import sys, os

def program_name(file_name):

    #First we read the file and create a list of students and programs
    try:
        file = open(file_name, 'r')
        enrolled_programs = [] #stores valid entries as tuples

        for line in file: #iterate over each line in the file
            students_data = [item.strip().strip("'") for item in line.split(',')] #removes any whitespace from the line, any surrounding single quotes, splits line into components
            if len(students_data) >= 6: #data contains at least 6 fields
                first_name = students_data[0] #first field
                last_name = students_data[1] #second field
                program = students_data[4] #fifth field
                student_name = f"{first_name} {last_name}"#combines first and last name
                enrolled_programs.append((student_name, program))#Adds tuple of (student_name,program) to list of valid entries
            else:
                print(f"Invalid line: {line.strip()}") #if line doesn't meet criteria, print message tells us its being skipped

        #Ask the user which program their looking for
        searched_program = input("Enter the program name you are looking for: ").strip() #removes leading or trailing whitespace from input

        #Checks if an empty string was entered and displays an error message
        if not searched_program:
            print("No program entered. Please enter a valid program.")
            return None, []

        #Find all the students enrolled in that program, loops through each tuple in enrolled_programs, compares program with searched program, collects names of the students enrolled in the matching program
        enrolled_in_program = [student for student, program in enrolled_programs if program.lower() == searched_program.lower()]

        #print the results of the search
        if enrolled_in_program:
            print(f"Students enrolled in {searched_program}:")
            for student in enrolled_in_program: #loops through each student in list of matches, and prints each
                print(student)
        else:
            print(f"There are no students found in the program: {searched_program}") #error message if no students were found

        return searched_program, enrolled_in_program

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.") #file name does not exist
        return None, [] 

    except Exception as e:
        print(f"An error occurred: {e}") # any other errors
        return None, []

def elective(file_name):

    try:
        #Open and read the file with student and elective data
        file = open(file_name, 'r')
        enrolled_electives = []

        for line in file:
            student_electives = [item.strip().strip("'") for item in line.split(',')]
            if len(student_electives) >= 6:
                first_name = student_electives[0]
                last_name = student_electives[1]
                elective_name = student_electives[5]
                student_name = f"{first_name} {last_name}"
                enrolled_electives.append((student_name, elective_name))

            else:
                print(f"Invalid line: {line.strip()}")
        
        #Ask the user to search the elective they are looking for
        searched_elective = input("Enter the name of the elective you are looking for: ").strip()

        if not searched_elective:
            print("No elective entered. Please enter a valid elective.")
            return None, []

        #Find all students found in searched elective
        enrolled_in_elective = [student for student, elective in enrolled_electives if elective.lower() == searched_elective.lower()]

        #results of elective search
        if enrolled_in_elective:
            print(f"Students enrolled in {searched_elective}:")
            for student in enrolled_in_elective:
                print(student)
        else:
            print(f"There are no students found in the elective: {searched_elective}")


        #Return the elective and the students enrolled in it
        return searched_elective, enrolled_in_elective

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
        return None, []

    except Exception as e:
        print(f"An error occurred: {e}")
        return None, []







#Testing the function

def main():
    # Directly specifying the file name for testing
    file_name = 'test.txt'
    program_name(file_name)
    elective(file_name)

if __name__ == "__main__":
    main()

>>>>>>> 8e93a0ed22b0b8a191044e3f840d35b11d52c52f
