import os
import time

def detailsFeature(std_ID, std_name, std_college, std_department, std_level, std_terms):

    # Prints student details in terminal
    print(f"Name: {std_name[0]} \nstdID: {std_ID} \nLevel(s): {', '.join(std_level)} \nNumber of terms: {', '.join(std_terms)} \nCollege(s): {', '.join(std_college)} \nDepartment(s): {', '.join(std_department)}")

    # Writes student details to a txt file with the student ID as the file name
    txtfilename = f"std{std_ID}details.txt"
    with open(txtfilename, "w") as f:
        f.write(f"Name: {std_name[0]}\n")
        f.write(f"stdID: {std_ID}\n")
        f.write(f"Level(s): {', '.join(std_level)}\n")
        f.write(f"Number of terms: {', '.join(std_terms)}\n")
        f.write(f"College(s): {', '.join(std_college)}\n")
        f.write(f"Department(s): {', '.join(std_department)}\n")

    # Clear console screen and sleep after a few seconds
    time.sleep(5)
    os.system("cls")


# PROGRAM STARTS HERE

# TEST VALUES
# Currently using student details output from start_feature.py if the user input is:
# std_level == 'B', std_degree == 'B0', std_ID == '201006000'
student_ID = '201006000'
student_name = ['Ibrahim Ahmed Nemer', 'Ibrahim Ahmed Nemer', 'Ibrahim Ahmed Nemer']
student_college = ['College1', 'College1', 'College1']
student_department = ['C1Department1', 'C1Department1', 'C1Department1']
student_level = ['U', 'G', 'G']
student_terms = ['8', '4', '6']

# Calls the detailsFeature using user input from startFeature
detailsFeature(student_ID, student_name, student_college, student_department, student_level, student_terms)