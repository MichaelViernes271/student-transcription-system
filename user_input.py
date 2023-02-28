from menu_feature import menuFeature
from details_feature import detailsFeature


import os, time

def userInput(student_ID, student_name, student_college, student_department, student_level, student_terms):
    """Executes the selected option in menu."""
    usr_input = int(input("Enter your feature: "))
    try:
        if usr_input == 1:
            detailsFeature(student_ID, student_name, student_college, student_department, student_level, student_terms)
            menuFeature()
            userInput()

        elif usr_input == 2:
            pass
        elif usr_input == 3:
            pass
        elif usr_input == 4:
            pass
        elif usr_input == 5:
            pass
        elif usr_input == 6:
            pass
        elif usr_input == 7:
            pass
        elif usr_input == 9:
            print("TERMINNATING")
        elif usr_input == 11:
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
