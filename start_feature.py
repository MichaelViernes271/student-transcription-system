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
        
    # Validates if user ID, user level, and user degree is in database
    def validate_input(stdID, level, degree):   
        filename = "studentDetails.csv"
        data = np.loadtxt(filename, delimiter=",", skiprows=1, dtype=str)   # Loads data into string arrays
        std_in_data = False       

        while True:
            # Iterates on the database to check if user ID is in it
            for info in data: 
                # Validates if user ID is in data regardless of user level (B)
                if stdID in info and level == 'B':   
                    # Validates if user degree is in data
                    for item in info:     
                        if degree == 'B0':
                            std_in_data = True
                        elif degree in item and len(item) == 2:
                            std_in_data = True
                # Validates if user ID and user level (U or G) are in data
                if stdID in info and level in info:
                    # Validates if user degree is in data
                    for item in info:
                        if degree == 'B0':
                            std_in_data = True
                        elif degree in item and len(item) == 2:
                            std_in_data = True

            if std_in_data == True:
                return std_in_data
            else:
                print(f"The student with stdID: {stdID}, stdLevel: {level}, and stdDegree: {degree}, is cannot be found. Please try again. \n")
                std_in_data == False
                return std_in_data


    # Gets and validates user level input. Gets other user inputs after choosing a specific user level
    user_in_data = False
    while user_in_data == False:
        user_level = str(input("Select the student level: [U] Undergraduate, [G] Graduate, [B] Both : ")).upper()
        if user_level == 'U':
            user_degree = 'None'
            user_ID = stdID_input()
            user_in_data = validate_input(user_ID, user_level, user_degree)
        elif user_level == 'G':
            user_degree = degree_input()
            user_ID = stdID_input()
            user_in_data = validate_input(user_ID, user_level, user_degree)
        elif user_level == 'B':
            user_degree = degree_input()
            user_ID = stdID_input()
            user_in_data = validate_input(user_ID, user_level, user_degree)
        else:
            print("Invalid input. Please enter U, G, or B for student level. \n")

    return user_level, user_degree, user_ID, user_in_data

# Initialize user input values by calling startFeature()
student_level, student_degree, student_ID, student_in_data = startFeature()

# TEST 
# print(f"\nStudent level: {student_level} \nStudent degree: {student_degree} \nStudent ID: {student_ID}")