import random
from random_generator import random_rows

def testcases(csv_reader):

    while True:
        try:
            num_professors = int(input("Enter the number of professors for the test case (3, 10, 20, 30, ...): "))

            # Use random_rows function based on the selected number of professors
            rows = random.sample(list(csv_reader), num_professors)
            
            # Add your preferences logic here, you can use the 'rows' variable
            more_test_cases = input("Do you want to enter more test cases? (Y/N): ").upper()
            if more_test_cases not in 'Y':
                break  # Exit the loop if the user enters anything other than 'Y'

        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

    return rows
