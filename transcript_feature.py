"""
OBJECTIVES:
(X) DISPLAYING THE USER DETAIL ABOVE
(O) RETRIEVING THE DATA FROM CSV
(O) DISPLAYING THE GRADES
(O) DISPLAYING THE COURSE AND AVERAGE ORGANIZED BY TERM
(X) PROPER FORMATTING FOR USER READABILITY
(X) STORING THE USER TRANSCRIPT TO THE FILE

NOTE: IN THE display_transcript(), IT 
IS NOT FORMATTED YET LABELED MATCHING THE PROPER OUTPUT. PLEASE CHANGE THIS.

"""

import csv, math

def transcriptFeature(filename, typeofcourse=None):
    # Open the CSV file
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        # PSEUDOCODE
        # select which is major and minor
        courses = [x for x in csv_reader if x[5].lower() == typeofcourse]
        # count the terms
        terms = [x[2] for x in courses]
        terms = int(max(terms))
        print("max term: ", terms, type(terms))
        for term in range(1, int(terms)+1):
            # decorator(term) # delineates successive terms and marks the end
            display_transcript(courses, term, typeofcourse)

        # testing vars
        # print("Course names:\n", coursename)
        # print("CourseIDs:\n", courseid)
        # print("Credit Hours:\n", credithours)
        # print("Grade:\n", grade)
        # print("Overall Average:\n", overall_average)


def display_transcript(courses, term, typeofcourse):
    """print the transcript based on major and minor"""

    # for storing the data in separate course each term
    grades = []
    for course in courses:
        if term == int(course[2]):
            print("Student detail:\n", course)
            # convert grades into int
            grade = int(course[7])
            grades.append(grade)
    
    subject_average = average(grades) # compute average

    # compute the average the term and overall terms
    overall_average = average(grades)


    print("Overall Average:\n", overall_average)
    print("{} Average:\n".format(typeofcourse.title()), subject_average)


def average(grades):
    # rounded to 2 decimals by format
    overall_average = round((sum(grades)/len(grades)), 3)
    overall_average = f"{overall_average:4.2f}"
    return overall_average

# # still working ....
# def decorator(decors):
#     """Puts a design around the transcript."""
#     decoration = "="*60 + "{decors:^}".center(60, "*") + 
#     print()

if __name__ == "__main__":
    # testing
    transcriptFeature("201006000.csv", "major")