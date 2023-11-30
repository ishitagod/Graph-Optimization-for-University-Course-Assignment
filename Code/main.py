import csv
import numpy as np
from combined_result import combined_result
from equal_priority import one_matrix_sol
from hungarian_algo import hungarian_algorithm, ans_calculation
from sorted_courses import sort_courses
import random
from random_generator import random_rows
from itertools import islice

from testcases import testcases


print("\nHello! Welcome to our DISCO Project.\nWe have two solutions using the Hungarian Algorithm.\nOur first solution divides courses into a CDC array and Elective array.\n")
def process_csv():
    
    with open('faculty_preference.csv', 'r') as file:
        
        csvreader = csv.reader(file)
        next(csvreader) # Skip the header row
        CDC_list = []
        ELEC_list = []
        prof_list = []
        professor = []
    

        #rows = random_rows(csvreader,30) #get 30 random rows for differetn test cases
        rows = random.sample(list(csvreader), 30)

        for row in rows:
            try: #If there are blank/unreadable rows in faculty_preference
                # Process the element as needed
                name = row[0]
                category = row[1]
                prefs = row[2:]
                professor.append({
                    'name':name,
                    'category':category,
                    'prefs':prefs
                })
                for i in prefs:
                    if 'CDC' in i:
                        CDC_list.append(i)
                    else:
                        ELEC_list.append(i)
                """ Here we append the professor names to the list of profs 
                depending on number of times we can divide it by 0.5, to help 1:1 mapping """
                if category == 'x1':
                    prof_list.append(name)
                elif category == 'x2':
                    prof_list.append(name)
                    prof_list.append(name)
                elif category == 'x3':
                    prof_list.append(name)
                    prof_list.append(name)
                    prof_list.append(name)

            except IndexError as e:
                print(f"Error: {e}. Skipping row.")
                continue
                
    return set(CDC_list), set(ELEC_list), professor, prof_list # Ensure unique courses for our initial data


CDC_set, ELEC_set, professor, prof_list = process_csv()

CDC_list = sort_courses(list(CDC_set) * 2)  # Duplicated so we can treat each course and professor mapping as 1:1
ELEC_list = sort_courses(list(ELEC_set) * 2)  # Duplicated so we can treat each course and professor mapping as 1:1
COURSE_list=[]
COURSE_list= CDC_list + ELEC_list

# Determine the size of the square matrix (maximum length of CDC_set or ELEC_set)

def cdc_hung_assignment(professor, prof_list, CDC_list):
    matrix_size = max(len(CDC_list), len(prof_list))

# Initialize square matrices with zeros
    CDC_arr = np.full((matrix_size, matrix_size),1000, dtype=int) #initilizing all elements with dummy data
# Iterate over each professor
    for idx, i in enumerate(prof_list):
    # Find the corresponding professor in the 'professor' list
        prof_info = next((p for p in professor if p['name'] == i), None)
    
        if prof_info:
        # Extract the preferences list for the professor
            prefs = prof_info['prefs']
            cdc_row = []

        # Populate CDC_arr
            for k in CDC_list:
                if k in prefs:
                    index=prefs.index(k) + 1 #To make sure preference goes from 1.. not 0
                    cdc_row.append(index)
                else:
                    cdc_row.append(1000)
        
        # Use slicing to ensure the correct length
            CDC_arr[idx, :len(cdc_row)] = cdc_row[:matrix_size]

#Calling Hungarian Algorithm

    ans_pos = hungarian_algorithm(CDC_arr.copy())
    ans, ans_mat = ans_calculation(CDC_arr, ans_pos)
    return CDC_arr,ans_mat

CDC_arr, ans_mat = cdc_hung_assignment(professor, prof_list, CDC_list)


def list_to_dict(assigned_prof_list):
    assigned_prof_dict = {}
    for assignment in assigned_prof_list:
        prof_name, course = assignment
        if prof_name not in assigned_prof_dict:
            assigned_prof_dict[prof_name] = [course]
        else:
            assigned_prof_dict[prof_name].append(course)
    return assigned_prof_dict


def assignments_check(Course_list,ans_mat,prof_list):
    assigned_prof=[]
    A_COURSE = []
    A_PROF=[]
    unassigned_course = Course_list.copy()
    unassigned_prof=[]
    for index,row in enumerate(ans_mat):
            #print("index",index)
            max_value_index = np.argmax(row)
            max_value=row[max_value_index]
            if(max_value!=1000.0 and max_value!=0.0):
                #print(max_value)
                A_COURSE.append(Course_list[max_value_index])
                A_PROF.append(prof_list[index])
                #print(A_PROF)
                assigned_prof.append([prof_list[index],Course_list[max_value_index]])
                unassigned_course.remove(Course_list[max_value_index])
            else:
                try:
                    unassigned_prof.append(prof_list[index])

                except IndexError:
                    continue
                #print(unassigned_prof)
                #print("max value invalid")
                continue                        

    # print("assigned PROFS:",assigned_prof)
    # print("assigned courses:",A_COURSE)
    # print("assigned Professors:",A_PROF)
    # print("unassigned course",unassigned_course)
    # print("unassigned profs", unassigned_prof)
    return unassigned_course,unassigned_prof, list_to_dict(assigned_prof)


unassigned_cdc,unassigned_prof, cdc_assigned_dict = assignments_check(CDC_list,ans_mat,prof_list) 

def elec_hung_assignment(unassigned_prof,ELEC_list,professor):
    elec_course_only_size = max(len(ELEC_list), len(unassigned_prof))
    elec_course_only = np.full((elec_course_only_size, elec_course_only_size), 1000, dtype=int)

    for idx, prof in enumerate(unassigned_prof):
        # Find the corresponding professor in the 'professor' list
        prof_info = next((p for p in professor if p['name'] == prof), None)
        
        if prof_info:
            # Extract the preferences list for the professor
            prefs = prof_info['prefs']
            elec_row = []

            # Populate elec_course_only
            for k in ELEC_list:
                if k in prefs:
                    index = prefs.index(k) + 1  # To make sure preference goes from 1.. not 0
                    elec_row.append(index)
                else:
                    elec_row.append(1000)
            
            # Use slicing to ensure the correct length
            elec_course_only[idx, :len(elec_row)] = elec_row[:elec_course_only_size]

        
        # Use slicing to ensure the correct length
    ans_pos = hungarian_algorithm(elec_course_only.copy())
    ans, ans_mat = ans_calculation(elec_course_only, ans_pos)
    unassigned_elec, unassigned_prof, elec_assigned_dict = assignments_check(ELEC_list,ans_mat,unassigned_prof)
    return unassigned_elec,unassigned_prof,elec_assigned_dict,ans_mat
    
unassigned_elec,unassigned_prof, elec_assigned_dict,ELEC_arr= elec_hung_assignment(unassigned_prof,ELEC_list,professor)


#CDC and Elec lists combined
def all_assignments():
    all_mat = one_matrix_sol(COURSE_list,prof_list,professor)
    unassigned_courses,unassigned_prof, all_course_assigned = assignments_check(COURSE_list,all_mat,prof_list)
    user_input = input("We have two solutions as we explained in the doc.\nOur second solution combines the CDC array and Elective array and runs the combined array through Hungarian Algorithm.\nDo you want to see the combined output of CDC and ELEC assignments? (Y/N): ").strip().lower()
    if user_input == 'y':

        for prof, courses_all in all_course_assigned.items():
            print(f"Professor {prof} assigned to {courses_all}")
        print("\n Unassigned Profs are:", unassigned_prof)
        print("\n Unassigned Courses are:", unassigned_courses)
    elif user_input == 'n':
        print("Okay thank you! Check out Output.csv for all our outputs.")

# Iterate over keys in one of the dictionaries (assuming both dictionaries have the same keys)
combined_dict = elec_assigned_dict.copy()  # Start with a copy of one dictionary

# Merge the second dictionary into the combined dictionary
for key, value in cdc_assigned_dict.items():
    combined_dict[key] = combined_dict.get(key, []) + value
sorted_combined_dict = dict(sorted(combined_dict.items()))

print("Program has run! Check out Output.csv for all our outputs.")
print(combined_dict)

with open("OUTPUT.csv", 'w', newline='') as csvfile:
        fieldnames = ['Professor', 'Category', 'Assigned Course']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header row
        writer.writeheader()

        # Write the data rows
        for prof, courses in sorted_combined_dict.items():
            
            prof_info = next((p for p in professor if p['name'] == prof), None)
        
            if prof_info:
            # Extract the preferences list for the professor
                category = prof_info['category']

            unique_courses = list(set(courses))
            writer.writerow({'Professor': prof, 'Category' : category, 'Assigned Course': courses})




all_assignments()



#For Testing
with open('tests/CDC_course_list.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(CDC_list)
    for line in CDC_arr:
        csvwriter.writerow(line)
with open('tests/OUTPUT_TEST.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(CDC_list)
    for line in ans_mat:
        csvwriter.writerow(line)

with open('tests/ELEC_course_list.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(ELEC_list)
    for line in ELEC_arr:
        csvwriter.writerow(line)
