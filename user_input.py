# Contributed by: Team 3
import os, time

def userInput():
    """Executes the selected option in menu."""
    usr_input = int(input("Enter your feature: "))
    try:
        if usr_input == 1:
            pass
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
