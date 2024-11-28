#!/usr/bin/env python3
# Project Name: Assignment 2
# Group 3
# Student Name: Saira Munawar, Andrew, Juliana, Nishan Shawmya Sivakumar

import sys, os

def transportation():
    """
    Reads the file 'user_test' and returns a summary of transportation preferences.
    """
    try:
        with open("user_test", "r") as file:
            data = file.readlines()  # Read all lines from the file
        
        # Initialize an empty dictionary to store transportation counts
        transport_modes = {}
        
        # Process each line in the file
        for line in data:
            components = [comp.strip(" '") for comp in line.strip().split(",")]  # Clean up each component
            if len(components) < 8:  # Ensure there are enough fields
                continue  # Skip invalid lines with insufficient data
            
            transport = components[7]  # Transportation mode is the 8th field
            
            # Count occurrences of each transportation mode
            transport_modes[transport] = transport_modes.get(transport, 0) + 1
        
        return transport_modes  # Return the summary as a dictionary
    
    except FileNotFoundError:
        print("Error: The file 'user_test' was not found.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}


def dietary():
    """
    Reads the file 'user_test' and returns a summary of dietary preferences.
    """
    try:
        with open("user_test", "r") as file:
            data = file.readlines()  # Read all lines from the file
        
        # Initialize an empty dictionary to store dietary preference counts
        dietary_preferences = {}
        
        # Process each line in the file
        for line in data:
            components = [comp.strip(" '") for comp in line.strip().split(",")]  # Clean up each component
            if len(components) < 7:  # Ensure there are enough fields
                continue  # Skip invalid lines with insufficient data
            
            diet = components[6]  # Dietary preference is the 7th field
            
            # Count occurrences of each dietary preference
            dietary_preferences[diet] = dietary_preferences.get(diet, 0) + 1
        
        return dietary_preferences  # Return the summary as a dictionary
    
    except FileNotFoundError:
        print("Error: The file 'user_test' was not found.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}


# Testing the functions
if __name__ == "__main__":
    # Testing transportation function
    print("Transportation Preferences:")
    print(transportation())
    
    # Testing dietary function
    print("\nDietary Preferences:")
    print(dietary())

