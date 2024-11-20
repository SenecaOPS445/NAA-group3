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

#def management(filename):
#   '''This function organizes the file based on the user's input'''
#   '''Options are: alphabetical, dietary, transportation, program name, elective'''

#def generate_report(filename):
#   '''Takes the management report and generates it into a file and moves it to the school folder'''

#def validiation:
#   '''Validates users options, if the user picks incorrect options then print assignment2.py'''


if __name__ == '__main__':
    folder_path = 'school_folder' #the path of the folder - should be in the same directory as assignment 2
    print(school_folder(folder_path))

