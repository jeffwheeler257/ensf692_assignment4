# calgary_dogs.py
# AUTHOR NAME
#
# A terminal-based application for computing and printing statistics based on given input.
# Detailed specifications are provided via the Assignment 4 README file.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.

import numpy as np
import pandas as pd

def main():

    # Import data here
    dog_data = pd.read_excel(".\CalgaryDogBreeds.xlsx")

    print("ENSF 692 Dogs of Calgary")
    print(dog_data.head(10))

    # User input stage

    # Data anaylsis stage

if __name__ == '__main__':
    main()
