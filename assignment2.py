#!/usr/bin/env python3
# Project Name: Assignment 2
# Group 3
# Student Name: Shawmya Sivakumar

import sys, os

def transportation(filename):
    """Returns the transportation methods selected by students."""
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            print("Transportation methods selected by students:")
            for line in lines:
                data = line.strip().split(',')
                if len(data) > 5:  # Ensure there are enough columns
                    print(f"{data[0]} {data[1]} - Transportation: {data[5]}")
                else:
                    print(f"Warning: Incomplete data in line: {line.strip()}")
    except FileNotFoundError:
        print("The file was not found.")

def dietary(filename):
    """Returns the dietary preferences selected by students."""
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            print("Dietary preferences of students:")
            for line in lines:
                data = line.strip().split(',')
                if len(data) > 4:  # Ensure there are enough columns
                    print(f"{data[0]} {data[1]} - Dietary Preference: {data[4]}")
                else:
                    print(f"Warning: Incomplete data in line: {line.strip()}")
    except FileNotFoundError:
        print("The file was not found.")


