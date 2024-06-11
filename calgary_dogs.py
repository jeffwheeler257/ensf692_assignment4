# calgary_dogs.py
# Jeff Wheeler
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

    # User input stage

    while(True):
        dog_breed = input("Please enter a dog breed: ").upper()
        try:
            if dog_breed in dog_data.values:
                break
            else:
                raise KeyError
        except KeyError:
            print("Dog breed not found in the data. Please try again.")
            continue

    # Data anaylsis stage

    # Find and print all years where the selected breed was listed in the top breeds.
    years = dog_data.loc[dog_data.Breed == dog_breed, ['Year']]['Year'].unique()
    # years_str =
    print(f"The {dog_breed} was found in the top breeds for years: {years}") # way to format years list as individual values

    # Calculate and print the total number of registrations of the selected breed found in the dataset.
    total = dog_data.loc[dog_data.Breed == dog_breed, ['Total']]['Total'].sum()
    print(f"There have been {total} {dog_breed} dogs registered total.")

    # Calculate and print the percentage of selected breed registrations out of the total percentage for each year (2021, 2022, 2023).
    # Calculate and print the percentage of selected breed registrations out of the total three-year percentage
    num_of_dogs_2021 = dog_data.groupby(['Year']).sum().loc[2021,'Total']
    num_of_dogs_2022 = dog_data.groupby(['Year']).sum().loc[2022,'Total']
    num_of_dogs_2023 = dog_data.groupby(['Year']).sum().loc[2023,'Total']
    num_of_dogs = num_of_dogs_2021 + num_of_dogs_2022 + num_of_dogs_2023
    breed_2021 = dog_data.loc[dog_data.Breed == dog_breed, ['Year', 'Total']].groupby(['Year']).sum().loc[2021,'Total']
    breed_2022 = dog_data.loc[dog_data.Breed == dog_breed, ['Year', 'Total']].groupby(['Year']).sum().loc[2022, 'Total']
    breed_2023 = dog_data.loc[dog_data.Breed == dog_breed, ['Year', 'Total']].groupby(['Year']).sum().loc[2023, 'Total']
    breed_tot = breed_2021 + breed_2022 + breed_2023

    print(f"The {dog_breed} was {round(breed_2021/num_of_dogs_2021 * 100, 6)}% of top breeds in 2021.")
    print(f"The {dog_breed} was {round(breed_2022/num_of_dogs_2022 * 100, 6)}% of top breeds in 2021.")
    print(f"The {dog_breed} was {round(breed_2023/num_of_dogs_2023 * 100, 6)}% of top breeds in 2021.")
    print(f"The {dog_breed} was {round(breed_tot/num_of_dogs * 100, 6)}% of top breeds across all years.")

    # Find and print the months that were most popular for the selected breed registrations. Print all months that tie
    # print(dog_data.groupby(['Month']).count())

if __name__ == '__main__':
    main()
