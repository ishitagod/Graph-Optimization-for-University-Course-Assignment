import numpy as np
from hungarian_algo import hungarian_algorithm, ans_calculation
def one_matrix_sol(COURSE_list,prof_list,professor):
    matrix_size = max(len(COURSE_list), len(prof_list))
    COURSE_arr = np.full((matrix_size, matrix_size),1000,dtype=int)

    for idx, i in enumerate(prof_list):
    # Find the corresponding professor in the 'professor' list
        prof_info = next((p for p in professor if p['name'] == i), None)
    
        if prof_info:
        # Extract the preferences list for the professor
            prefs = prof_info['prefs']
            course_row = []
        

        # Populate CDC_arr
            for k in COURSE_list:
                if k in prefs:
                    index=prefs.index(k) + 1 #To make sure preference goes from 1.. not 0
                    course_row.append(index)
                else:
                    course_row.append(1000)
        
        # Use slicing to ensure the correct length
            COURSE_arr[idx, :len(course_row)] = course_row[:matrix_size]

#Calling Hungarian Algorithm 


    ans_pos = hungarian_algorithm(COURSE_arr.copy())
    ans, ans_mat = ans_calculation(COURSE_arr, ans_pos)
    return ans_mat
