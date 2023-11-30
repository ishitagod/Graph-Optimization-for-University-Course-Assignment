import csv

def combined_result(courses_cdc_dict,courses_elec_dict):
    combined_results = {}
# Combine CDC and ELEC dictionaries into one dictionary
    for prof, courses_cdc in courses_cdc_dict.items():
        courses_elec = courses_elec_dict.get(prof, [])  # Get ELEC courses for the professor if available
    combined_results[prof] = courses_cdc + courses_elec
    return combined_results
# Now, combined_results will have all professors assigned to both CDC and ELEC courses
# combined_results = {'P1': ['CDC_COURSE 1', 'CDC_COURSE 2', 'ELEC_COURSE 1', 'ELEC_COURSE 2'],
#                     'P2': ['CDC_COURSE 3', 'ELEC_COURSE 3']}

# Next, you can write this combined result to a CSV file
# with open('combined_results.csv', 'w', newline='') as csvfile:
#     csvwriter = csv.writer(csvfile)
    
#     # Write the header row
#     csvwriter.writerow(['Professor', 'Assigned Courses'])

#     # Write each professor and their assigned courses to the CSV file
#     for prof, courses in combined_results.items():
#         csvwriter.writerow([prof, ', '.join(courses)])

#     print("Combined results have been written to 'combined_results.csv'")