import os
import time

def previousRequestsFeature(studentID):
    filename = f"std{studentID}PreviousRequests.txt"
    if os.path.exists(filename):
        with open(filename, "r") as f:
            previous_requests = f.readlines()
        if previous_requests:
            print("Previous requests:")
            for req in previous_requests:
                print(req.strip())
        else:
            print("No previous requests found.")
    else:
        print("No previous requests found.")

    # Prompt the user to continue
    input("Press Enter to continue...")
    # Clear the screen
    os.system("cls" if os.name == "nt" else "clear")
    # Sleep for a few seconds
    time.sleep(2)


if __name__ == "__main__":
    previousRequestsFeature(201006000)