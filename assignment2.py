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
    if len(sys.argv) != 2:
        print('File name not given, Please enter a file name')
    else:
        file_name = sys.argv[1]
        file_content = read_text_file(file_name)
        print(file_content)
    '''change if management file is changed. Done by Saira'''

def read_text_file(file_name):
    '''opens the file given by the user'''
    try:
        management(file_name) #hmm?
    except FileNotFoundError:
        return 'File not found'

def management(file_name):
    '''This function organizes the file based on the user's input'''
    '''Options are: alphabetical, dietary, transportation, program name, elective, campus'''
    f = open(file_name, 'r')
    #TO DO: turn user_test into a dictonary/list
    #    if sys.argv[2] == 'alphabetical':
    #       alp_order(file_name)
    '''To do:TRY sys.arguments if that doesn't work, it'll be a user input. Done by Saira'''

def alp_order:
    ''' Take the file, turn it into a list/dictonary and then order last name by alphabectical order''' 
    ''' to do: Nishan'''

def program_name:
    '''Take the file, user inputs a program name, turn file into a list and dictonary and only pull the lines with the program name'''
    '''end of the report, count how many lines there were: There is 60 students in the _ program'''
    '''if name does not exist, enter an error message '''
    ''' to do: Andrew '''

def elective:
     '''similar to program name. Done by Andrew'''

def campus:
    ''' take the file, user input a program name, turn file into dictonary/list and only pull campus names'''
    ''' Done by Juliana'''

def transportation: 
   ''' take the file, user inputs transportation name, and pull whatever the name is'''
   '''Done by Shawmya'''

def dietary:
   '''take the file, user inputs dietary, pull the diets'''
   '''Done by Shawmya'''

def find_student:
   '''take a file, user would input a name and student id and then find the user"'''
   '''Done by Nishan'''


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

