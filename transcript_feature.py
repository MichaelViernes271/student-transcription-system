"""
OBJECTIVES:
(O) DISPLAYING THE USER DETAIL ABOVE
(O) RETRIEVING THE DATA FROM CSV
(O) DISPLAYING THE GRADES
(O) DISPLAYING THE COURSE AND AVERAGE ORGANIZED BY TERM
(0) PROPER FORMATTING FOR USER READABILITY
(X) STORING THE USER TRANSCRIPT TO THE FILE

NOTE: IN THE display_transcript(), IT 
IS NOT FORMATTED YET LABELED MATCHING THE PROPER OUTPUT. PLEASE CHANGE THIS.

"""

import csv, math, statistics, os

def transcriptFeature(student_ID, csv_studentDetails, level, typeofcourse=None):
    """DESC: Displays the record of student in the each term.
    Calculates the average of grades.
    """

    # create a student profile through dictionary conversion
    dictionary_student = createStudentDictionary(csv_studentDetails, student_ID, level)
        
    # Open the CSV file of student by id
    with open(student_ID) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        # select which is major and minor
        # count the max terms in list
        courses = [x for x in csv_reader if x[5].lower() == typeofcourse]
        terms = [x[2] for x in courses]
        terms = int(max(terms))

        print_header(dictionary_student) # print the account detail

        # lists all the student information in each term by major or minor
        for term in range(1, int(terms)+1):
            decorator(f"Term {term}") # marks successive terms and the end
            # identify the respective columns for grade, courses, and credit hrs
            course_desc = "{:<15}{:<15}{:<15}{:<15}"
            print(course_desc.format("Course ID", "Course Name",
                "Credit Hours", "Grade"))

            display_transcript(courses, term, typeofcourse)
        decorator(f"End of Transcript for Level ()") # marks successive terms and the end

        # testing vars
        # print("Course names:\n", coursename)
        # print("CourseIDs:\n", courseid)
        # print("Credit Hours:\n", credithours)
        # print("Grade:\n", grade)
        # print("Overall Average:\n", overall_average)



def display_transcript(courses, term, typeofcourse):
    """print the transcript based on major and minor"""

    record_of_transcripts = None

    grades = [] # for storing the data in separate course each term


    for course in courses:
        if term == int(course[2]):
            # print("Student detail:\n", course)
            
            printCourse(course)
            # convert grades into int
            grade = int(course[7])
            grades.append(grade)
    
    subject_average = average(grades) # compute average each term
    overall_average = average(grades) # compute  overall term average

    print("Overall Average: ", overall_average, end=" ")
    print("{} Average: ".format(typeofcourse.title()), subject_average)


def storeToText(data, stdID, typeofcourse):
    filename = str(stdID) + typeofcourse + "Transcript"

    if os.path.exists(filename):
        print("File already exists.")
    else:
        with open(filename, "a") as f:
            f.write(data)



def print_header(dictionary_student):
    """Shows the top head of transcript."""

    # unpacking the dictionary
    name, stdid, college, department, major, minor, level, terms = dictionary_student.values()
    # show basic account information
    header_of_transcript = f"""\
Name: {name:<25} stdID: {stdid:<25}
College: {college:<25} Department: {department:<25}
Major: {major:<25} Minor: {minor:<25}
Level: {level:<25} No. of terms: {terms:<25}
"""
    print(header_of_transcript)


def createStudentDictionary(csv_file, student_ID, level):
    """Returns a dictionary of basic student account."""

    # opens the student roll and retrieve the data to vars
    # making the top header of the transcript
    student_dictionary = None
    with open(csv_file, "r", encoding="UTF-8-SIG") as csv_reader: 
        basename_id = student_ID.split(".")[0]
        csv_reader = csv.DictReader(csv_reader)
        for line in csv_reader:
            student_stdId=  line["stdID"]
            student_level =  line["Level"]
            if (basename_id in student_stdId) and (level in student_level):
                student_name = line["Name"]
                student_college = line["College"]
                student_major = line["Major"]
                student_minor =  line["Minor"]
                student_department =  line["Department"]
                student_terms =  line["Terms"]    

                # store the vars in dict
                student_dictionary = {
                "name": student_name,
                "stdid": student_stdId,
                "level": student_level,
                "college": student_college,
                "major": student_major,
                "minor": student_minor,
                "department": student_department,
                "terms": student_terms
                }
                break
    return student_dictionary


def printCourse(course):
    """Prints the information of student by course id,
    course name, credit hours, grade"""
    details = """\
{:<15}{:<15}{:<15}{:<15}
    """.format(course[1], course[3], course[6], course[7])
    print(details)

def average(grades):
    # rounded to 2 decimals by format
    overall_average = round(statistics.mean(grades), 3)
    overall_average = f"{overall_average:4.2f}"
    return overall_average

# # still working ....
def decorator(label):
    """Puts a design around a label (e.g. for each term."""
    decoration = "="*60  + "\n"  + "{:^15}".center(50, "*") + "\n" + "="*60
    print(decoration.format(label))


def validate():
    """Validates the files to be displayed and encoded in text files."""
    csv_stdID= "201006000.csv"
    csv_studentDetails = "studentDetails.csv"
    typeofcourse =  "major"
    level = "U"
    transcriptFeature(csv_stdID, csv_studentDetails, level, typeofcourse)

if __name__ == "__main__":
    validate()