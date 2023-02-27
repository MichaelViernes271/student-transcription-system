import numpy as np

def startFeature():
    
    # Gets and validates user degree input
    def degree_input():     
        while True:
            degree = str(input("Select the student degree: [M] Master, [D] Doctorate, [B0] Both : ")).upper()
            if degree == 'M':
                return degree
            elif degree == 'D':
                return degree
            elif degree == 'B0':
                return degree
            else:
                print("Invalid input. Please enter M, D, or B0 for student degree. \n")

    # Gets and validates user ID input
    def stdID_input():
        filename = "studentDetails.csv"
        data = np.loadtxt(filename, delimiter=",", skiprows=1, dtype=str)   # Loads data into string arrays
        stdID_in_data = False 

        while stdID_in_data == False:
            stdID = str(input("Enter student ID: "))
            for info in data:
                if stdID in info:
                    stdID_in_data = True
                    return stdID
            
            print("Student ID not found in database. Please try again. \n")

    def store_details(name, college, department, level, terms, values):
        name.append(values[2])
        college.append(values[3])
        department.append(values[4])
        level.append(values[5])
        terms.append(values[9])
        
        
    # Validates if user ID, user level, and user degree is in database. Return verified student's details
    def validate_input(stdID, level, degree):  
        # Intializes empty lists to store specified student details
        std_name = []
        std_college = []
        std_department = []
        std_level = []
        std_terms = []

        filename = "studentDetails.csv"
        data = np.loadtxt(filename, delimiter=",", skiprows=1, dtype=str)   # Loads data into string arrays
        std_in_data = False       

        # Iterates on the database to check if user ID is in it
        for info in data:
            # Validates if user ID and user level (U or G) are in data
            if stdID in info and level in info:
                if degree == "Bachelor's":
                    store_details(std_name, std_college, std_department, std_level, std_terms, info)
                    std_in_data = True
                elif degree == 'M' or degree == 'D':
                    for item in info:
                        if degree in item and len(item) == 2:
                            store_details(std_name, std_college, std_department, std_level, std_terms, info)
                            std_in_data = True
                elif degree == 'B0':
                    store_details(std_name, std_college, std_department, std_level, std_terms, info)
                    std_in_data = True

            # Validates if user ID is in data regardless of user level (B)
            if stdID in info and level == 'B':
                if degree == 'M' or degree == 'D':
                    for item in info:
                        if item == 'U':
                            store_details(std_name, std_college, std_department, std_level, std_terms, info)
                            std_in_data = True
                        if degree in item and len(item) == 2:
                            store_details(std_name, std_college, std_department, std_level, std_terms, info)
                            std_in_data = True
                elif degree == 'B0':
                    store_details(std_name, std_college, std_department, std_level, std_terms, info)
                    std_in_data = True

        if std_in_data == True:
            return std_in_data, std_name, std_college, std_department, std_level, std_terms
        else:
            print(f"The student with stdID: [{stdID}], stdLevel: [{level}], and stdDegree: [{degree}], is cannot be found. Please try again. \n")
            return False, [], [], [], [], []    # Re-initializes default values to student details lists


    # Gets and validates user level input. Gets other user inputs after choosing a specific user level
    user_in_data = False
    while user_in_data == False:
        user_status = str(input("Select the student level: [U] Undergraduate, [G] Graduate, [B] Both : ")).upper()
        if user_status == 'U':
            user_degree = "Bachelor's"
            user_ID = stdID_input()
            user_in_data, user_name, user_college, user_department, user_level, user_terms = validate_input(user_ID, user_status, user_degree)
        elif user_status == 'G':
            user_degree = degree_input()
            user_ID = stdID_input()
            user_in_data, user_name, user_college, user_department, user_level, user_terms = validate_input(user_ID, user_status, user_degree)
        elif user_status == 'B':
            user_degree = degree_input()
            user_ID = stdID_input()
            user_in_data, user_name, user_college, user_department, user_level, user_terms = validate_input(user_ID, user_status, user_degree)
        else:
            print("Invalid input. Please enter U, G, or B for student level. \n")

    return user_in_data, user_ID, user_name, user_college, user_department, user_level, user_terms


# PROGRAM STARTS HERE:
# Initialize user input values by calling startFeature()
student_in_data, student_ID, student_name, student_college, student_department, student_level, student_terms = startFeature()
if student_in_data == True:
    print("Student found in database! \n")

# TEST VALUES
#print(f"\nStudent level: {student_level} \nStudent degree: {student_degree} \nStudent ID: {student_ID}")