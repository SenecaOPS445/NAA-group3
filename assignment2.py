#!/usr/bin/env python3
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

