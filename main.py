# This work done by group 3:
# Mary Joy Aban, 25%
# Leon Adriel Franco Acaoili, 25%
# Reiven Cabate, 25%
# Michael Viernes, 2021-05811-MN-0, 25%

from start_feature import startFeature
from menu_feature import menuFeature
from details_feature import detailsFeature
from statistics_feature import statisticFeature
# from user_input import userInput
from major_transcript_feature import majorTranscriptFeature
from minor_transcript_feature import minorTranscriptFeature
from full_transcript_feature import fullTranscriptFeature
from previous_requests_feature import previousRequestsFeature, add_request, create_history_list

import os, time


def main():
    """The main program."""
    
    # START FEATURE
    student_in_data, student_ID, student_name, student_college, student_department, student_level, student_terms = startFeature()
    if student_in_data == True:
        request_history = create_history_list()
        print("Student found in database! \n")
        
    running = True
    while running == True:
        user_input = menuFeature()
        try:
            if user_input == 1:
                detailsFeature(student_ID, student_name, student_college, student_department, student_level, student_terms)
            elif user_input == 2:
                statisticFeature(student_ID)
            elif user_input == 3:
                add_request(user_input, request_history)
            elif user_input == 4:
                add_request(user_input, request_history)
            elif user_input == 5:
                add_request(user_input, request_history)
            elif user_input == 6:
                previousRequestsFeature(request_history, student_ID)
            elif user_input == 7:
                pass
            elif user_input == 9:
                print("TERMINNATING")
            elif user_input == 11:
                print("CLEARING CONSOLE...")
                clearConsole()
            else:
                print("Select the options.")
                input("PROCESS COMPLETE".center(60, "="))
        except:
            input("Please use correct input.")
            print("CLEARING CONSOLE...")
            clearConsole()
            

    def clearConsole():
        """Clear screen."""
        time.sleep(1)
        os.system("cls")  # for windows_os == "clear", else for unix == "cls"
        # call("cls" if os.name == "nt" else "clear") # this sometimes not work



# 	# testing the customized modules
# 	menuFeature()
# 	# userInput()
# 	validate_full_transcript_feature()


# def validate_full_transcript_feature():
#     """Validates the files to be displayed and encoded in text files."""
#     csv_stdID= "201006000.csv"
#     csv_studentDetails = "studentDetails.csv"
#     typeofcourse =  "minor"
#     level = "U"

#     majorTranscriptFeature(csv_stdID, csv_studentDetails, level, typeofcourse)
#     print("x"*100)

#     typeofcourse = "major"
#     minorTranscriptFeature(csv_stdID, csv_studentDetails, level, typeofcourse)
#     print("x"*100)

#     typeofcourse = None
#     fullTranscriptFeature(csv_stdID, csv_studentDetails, level, typeofcourse)
    

# def validate_user_input():
    # pass


# def validate_menu_feature():
    # pass


if __name__ == "__main__":
	main()