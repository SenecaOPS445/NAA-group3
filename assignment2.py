#!/usr/bin/env python3
#Project Name: Assignment 2
#Group 3
#Student Names: Saira Munawar

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

def program_name(file_name):

def elective(file_name):

def campus(file_name):
   
def transportation(file_name):

def dietary(file_name):

def find_student(file_name):
    '''user will input name and student_id and find the the user'''
    
def generate_report(option, information):
   '''Takes the management report and generates it into a file and moves it to the school folder'''
   current_date = datetime.datetime.now()
   formatted_date = current_date.strftime('%d-%m-%Y-%H-%M-%d')
   filename = "Report_" + option + "_" + formatted_date + ".txt"
   print('file generated will be named: ' + filename)
   f = open(filename, "a")
   f.write(option + " Report\n")
   f.write("=" * 80 + "\n")
   if information:
       for info in information:
           f.write(info + "\n")
   else:
       f.write("No " + option + " found matching your query.\n")
   f.close()
   print('Report was generated: ' + filename)
   
   #moving the file to school folder:
   source = filename
   destination = 'school_folder'
   dest = shutil.move(source, destination) 
   print('File moved to school_folder!')
   
if __name__ == '__main__':
    folder_path = 'school_folder' #the path of the folder - should be in the same directory as assignment 2
    print(school_folder(folder_path))
    usage()
    
