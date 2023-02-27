"""
OBJECTIVES:
(O) DISPLAYING THE USER DETAIL ABOVE
(O) RETRIEVING THE DATA FROM CSV
(O) DISPLAYING THE GRADES
(O) DISPLAYING THE COURSE AND AVERAGE ORGANIZED BY TERM
(O) PROPER FORMATTING FOR USER READABILITY
(O) STORING THE USER TRANSCRIPT TO THE FILE

NOTE: IN THE display_transcript(), IT 
IS NOT FORMATTED YET LABELED MATCHING THE PROPER OUTPUT. PLEASE CHANGE THIS.

"""

import csv, math, statistics, os

def transcriptFeature(student_ID, csv_studentDetails, level, typeofcourse=None):
    """DESC: Displays the record of student in the each term.
    Calculates the average of grades.
    Every tie the data will be stored, it will get printed first."""

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

        # retrieve only the basename of csv student id without ".csv"
        student_ID = student_ID.split(".")[0] 
        temp_data = print_header(dictionary_student)
        storeToText(temp_data, student_ID, typeofcourse)

        # lists all the student information in each term by major or minor
        for term in range(1, int(terms)+1):
            # marks successive terms and the end
            decoration = decorator(f"Term {term}") 
            print(decoration)
            
            # identify the respective columns for grade, courses, and credit hrs
            course_desc = "{:<15}{:<15}{:<15}{:<15}"
            course_desc = course_desc.format("Course ID", "Course Name",
                "Credit Hours", "Grade")
            print(course_desc)

            # store the data in text
            temp_data = "\n" + decoration + "\n" + course_desc
            storeToText(temp_data, student_ID, typeofcourse)

            # for displaying the transcript
            temp_data = display_transcript(courses, term, typeofcourse)
            storeToText(temp_data, student_ID, typeofcourse)

        temp_data = decorator(f"End of Transcript for Level ()") # marks successive terms and the end
        print(temp_data)
        storeToText("\n"+temp_data, student_ID, typeofcourse)


def display_transcript(courses, term, typeofcourse):
    """print the transcript based on major and minor"""

    # make an empty variable for the final output to hold the record
    temp_data = None

    grades = [] # for storing the data in separate course each term


    for course in courses:
        if term == int(course[2]):
            # print the course labels
            temp_data = printCourse(course)
            print(temp_data)
            # convert grades into int
            grade = int(course[7])
            grades.append(grade)
    
    subject_average = average(grades) # compute average each term
    overall_average = average(grades) # compute  overall term average

    text_average = "{} Average: ".format(typeofcourse.title())
    print(text_average, end="\t")
    text_overall_average = f"Overall Average: {overall_average}"
    print(text_overall_average)
    return "\n" + temp_data + "\n" + text_average + "\t" + text_overall_average


def storeToText(data, stdID, typeofcourse):
    """Stores the data after printing."""
    filename = str(stdID) + typeofcourse + "Transcript"
    with open(filename+".txt", "a") as f:
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
    return header_of_transcript


def printCourse(course):
    """Prints the information of student by course id,
    course name, credit hours, grade"""
    details = """\
{:<15}{:<15}{:<15}{:<15}
    """.format(course[1], course[3], course[6], course[7])
    return details


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


def average(grades):
    # rounded to 2 decimals by format
    overall_average = round(statistics.mean(grades), 3)
    overall_average = f"{overall_average:4.2f}"
    return overall_average


def decorator(label):
    """Puts a design around a label (e.g. for each term."""
    decoration = "="*60  + "\n"  + "{:^15}".center(50, "*") + "\n" + "="*60
    return decoration.format(label)


def validate():
    """Validates the files to be displayed and encoded in text files."""
    csv_stdID= "201006000.csv"
    csv_studentDetails = "studentDetails.csv"
    typeofcourse =  "major"
    level = "U"
    transcriptFeature(csv_stdID, csv_studentDetails, level, typeofcourse)

if __name__ == "__main__":
    validate()