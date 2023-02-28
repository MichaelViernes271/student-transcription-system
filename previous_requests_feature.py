from datetime import datetime


def previousRequestsFeature(history, stdID):
    # Prints header for previous requests 
    print("Previous requests: \nRequest\t\tDate\t\t\tTime")
    print("="*50)

    if history == []:
        print("No previous requests found.")
    else:
        for record in history:
            print(f"{record[0]}\t\t{record[1]}\t\t{record[2]}") # Prints request history in terminal

        filename = f"std{stdID}PreviousRequests.txt"
        with open(filename, 'a') as f:
            for record in history:   
                f.write(f"\n{record[0]}\t\t{record[1]}\t\t{record[2]}") # Writes request history into user's previous requests file


# Adds transcript request to request history
def add_request(choice, history):
    # Converts user choice into specific transcript type
    if choice == 3:
        choice = 'Major'
    elif choice == 4:
        choice = 'Minor'
    elif choice == 5:
        choice = 'Full'
    

    # Gets current date and time
    current_datetime = datetime.now()
    current_date = current_datetime.strftime("%d/%m/%Y")
    current_time = current_datetime.strftime("%H:%M %p")

    # Appends current request to request history
    current_request = [choice, current_date, current_time]
    history.append(current_request)


# PROGRAM STARTS HERE
# IMPORTANT - RequestHistory list & PreviousRequests txt file must be initialized first (can be intialized after getting stdID from startFeature)

stdID = '201006000' # Test value for stdID from startFeature

request_history = []    # Initializes empty request history list

# Creates RequestHistory list & PreviousRequests txt file with user's student ID
prev_requests_file = f"std{stdID}PreviousRequests.txt"
with open(prev_requests_file, 'w') as f:
    f.write("Request\t\tDate\t\t\tTime \n")
    f.write("="*40)


# PREVIOUS REQUEST FEATURE TEST STARTS HERE
# Currently using test values from user_input to test the program
user_input = 3
add_request(user_input, request_history)

user_input = 4
add_request(user_input, request_history)

user_input = 5
add_request(user_input, request_history)

# Calls previousRequestsFeature()
previousRequestsFeature(request_history, stdID)