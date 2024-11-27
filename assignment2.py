#!/usr/bin/env python3
#Project Name: Assignment2
#Group 3

import sys, os

def program_name(file_name):

    #First we read the file and create a list of students and programs
    try:
        file = open(file_name, 'r')
        enrolled_programs = []

        for line in file: #iterate over each line in the file
            students_data = line.strip().split(',') #removes any whitespace from the line, and returns a list with student name and program name
            if len(students_data) == 2: #checks that line has 2 elements after splitting
                student_name, program = students_data #separates each element in the list to student_name and program
                enrolled_programs.append((student_name.strip(), program.strip())) #creates a tuple, and adds it to the list enrolled_programs. Now all valid entries from the file are stored.
            else:
                print(f"Skipping invalid line: {line.strip()}") #if line doesn't contain 2 items, print message tells us its being skipped

        #Close the file after reading it
        file.close()

        #Ask the user which program their looking for
        searched_program = input("Enter the program name you are looking for: ").strip()

        #Find all the students enrolled in that program
        enrolled_in_program = [student for student, program in enrolled_programs if program.lower() == searched_program.lower()]

        #print the results of the search
        if enrolled_in_program:
            print(f"Students enrolled in {searched_program}:")
            for student in enrolled_in_program:
                print(student)
        else:
            print(f"There are no students found in the program: {searched_program}")

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.") 

    except Exception as e:
        print(f"An error occurred: {e}")

def elective(file_name):

    try:
        #Open and read the file with student and elective data
        file = open(file_name, 'r')
        enrolled_electives = []

        for line in file:
            student_electives = line.strip().split(',')
            if len(student_electives) == 2:
                student_name, elective_name = student_electives
                enrolled_electives.append((student_name.strip(), elective_name.strip()))

            else:
                print(f"Invalid line: {line.strip()}")
        
        #Close file after reading it
        file.close()

        #Ask the user to search the elective they are looking for
        searched_elective = input("Enter the name of the elective you are looking for: ").strip()

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
    file_name = 'studentprograms.txt'
    program_name(file_name)

    file_name = 'electives.txt'
    elective(file_name)

if __name__ == "__main__":
    main()

