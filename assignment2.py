#!/usr/bin/env python3
#Project Name: Assignment 2
#Group 3
#Student Names: Saira Munawar

import sys, os

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
        return 'File not found' #prints the error message if file doesn't exist

def management(file_name, option):
    '''This function organizes the file based on the user's input'''
    '''Options are: alphabetical, dietary, transportation, program name, elective, campus'''
    file_content = read_text_file(file_name) #checks if the file exist
    print(file_content) 

    if option.lower() == 'alphabetical' or option.lower() == 'a':
        alp_order()
    elif option.lower() == 'program' or option.lower() == 'p':
        program_name()
    elif option.lower() == 'elective' or option.lower():
        elective()
    elif option.lower() == 'campus' or option.lower() == 'c':
        elective()
    elif option == 'transportation' or option.lower() == 't':
        transporation()
    elif option.lower() == 'dietary' or  option.lower() == 'd':
        dietary()
    elif option.lower() == 'student' or option.lower() == 's':
        find_student()
    else:
        print('Please enter an option (Alphabetical (a), Program (p), Elective (e)')
        print('Campus (c), Transportation (t), Dietary (d), Student (s)')
    print('option name:', sys.argv[2])

def alp_order():
    '''Take the file, turn it into a list/dictonary and then order last name by alphabectical order '''
    print('To be done: Nishan')

def program_name():
    '''Take the file, turn it into a list/dictonary, print the program selected'''
    '''print the error message if program name doesn't exist'''
    print('To be done: Andrew')

def elective():
    '''returns the elective selected'''
    print('To be done: Andrew')

def campus():
    '''returns the campus selected'''
    print('To be done: Juliana')

def transportation():
    '''returns the transporation selected'''
    print('To be done Shawmya')

def dietary():
    '''returns the diet selected'''
    print('To be done by Shawmya')

def find_student():
    '''user will input name and student_id and find the the user'''
    print('To be done by Nishan')

def generate_report(filename)
   '''Takes the management report and generates it into a file and moves it to the school folder'''
   '''Done by Saira'''

def validiation(filename, argument):
   '''Validates users options, if the user picks incorrect options then print assignment2.py'''
   '''go through the file, check if the name exist, if it does not exist, it will print out an error message'''

if __name__ == '__main__':
    folder_path = 'school_folder' #the path of the folder - should be in the same directory as assignment 2
    print(school_folder(folder_path))
    usage()
    
