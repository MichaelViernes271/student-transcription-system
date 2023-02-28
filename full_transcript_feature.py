"""
OBJECTIVES:
(O) DISPLAYING THE USER DETAIL ABOVE
(O) RETRIEVING THE DATA FROM CSV
(O) DISPLAYING THE GRADES
(O) DISPLAYING THE COURSE AND AVERAGE ORGANIZED BY TERM
(O) PROPER FORMATTING FOR USER READABILITY
(O) STORING THE USER TRANSCRIPT TO THE FILE
"""

import csv, math, statistics, os, time

def transcriptFeature(student_ID, csv_studentDetails, level, typeofcourse=None):
    """DESC: Displays the record of student in the each term.
    Calculates the average of grades.
    Every tie the data will be stored, it will get printed first."""

    # create a student profile through dictionary conversion
    dictionary_student = createStudentDictionary(csv_studentDetails, student_ID, level)
        
    # Open the CSV file of student by id
    with open(student_ID, encoding="UTF-8-SIG") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        # select which is major and minor
        # count the max terms in list
        courses = [x for x in csv_reader]
        terms = [x[2] for x in courses if x[2].isdigit()]
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

            # store the each separated term in text and print it
            temp_data = "\n" + decoration + "\n" + course_desc + "\n"
            storeToText(temp_data, student_ID, typeofcourse)

            # for displaying the transcript
            temp_data = display_transcript(courses, term, typeofcourse)
            storeToText(temp_data, student_ID, typeofcourse)

        # mark the end of transcript
        temp_data = decorator(f"End of Transcript for Level ({level})") # marks successive terms and the end
        print(temp_data)
        storeToText("\n"+temp_data, student_ID, typeofcourse)


def display_transcript(courses, term, typeofcourse):
    """print the transcript based on major and minor"""

    # make an empty variable for the final output to hold the record
    temp_data = ""

    # for storing the data in separate subject matter each term
    major_grades = [] 
    minor_grades = []

    # only print the courses and grades of this current term
    for course in courses:
        if (not course[2].isdigit()) or (not course[7].isdigit()):
            # print("not a number")
            continue
        if term == int(course[2]):
            # print the course labels
            if course[5].lower() == "major":
                temps = printCourse(course)
                temp_data += temps + "\n"
                print(temps)
                # convert grades into int
                grade = int(course[7])
                major_grades.append(grade)
            elif course[5].lower() == "minor":
                temps = printCourse(course)
                temp_data += temps + "\n"
                print(temps)
                # convert grades into int
                grade = int(course[7])
                minor_grades.append(grade)

    # identify whether there is a minor or a major, else mark a zero
    # print(f"DEBUGGING \nmajor:{major_grades}\nmajor:{minor_grades}".center(50, "+"))
    if minor_grades == []: 
        minor_grades = 0
    else:
        minor_grades = average(minor_grades) # compute minors average each term and back to floats
        minor_grades = float(minor_grades)

    if major_grades == []: 
        major_grades = 0
    else:
        major_grades = average(major_grades) # compute minors average each term and back to floats
        major_grades = float(major_grades)



    # print(f"major: {major_grades}, \nminor: {minor_grades}\ntypes: major{type(major_grades)}, minor{type(minor_grades)}")
    term_average = [major_grades + minor_grades]
    term_average = average(term_average) # compute current term average
    all_term_average = overall_average(courses) # compute  overall term average

    text_major_average = "Major Average: {}".format(major_grades)
    print(text_major_average, end="\t")
    text_minor_average = "Minor Average: {}".format(minor_grades)
    print(text_minor_average)
    text_term_average = "Term Average: {}".format(term_average)
    print(text_term_average, end="\t")
    text_all_term_average = f"Overall Average: {all_term_average}"
    print(text_all_term_average, "\n")
    temp_data += "\n" + text_major_average + "\t" + text_minor_average + "\n"
    temp_data += text_term_average + "\t" + text_all_term_average + "\n"
    return temp_data


def storeToText(data, stdID, typeofcourse):
    """Stores the data after printing."""
    if typeofcourse is None:
        typeofcourse = "Full"
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
    """Compute the average of a list."""
    # rounded to 2 decimals by format
    # print(f"DEBUGGING {grades}".center(50, "+"))
    if grades == []:
        return grades
    else:
        overall_average = round(statistics.mean(grades), 3)
        overall_average = f"{overall_average:4.2f}"
    return overall_average


def overall_average(courses):
    """Returns the overall average of all terms"""
    grades = [] # for storing the data in separate course each term

    for course in courses:
        # convert grades into int
        if not course[7].isdigit():
            # print("not a number")
            continue
        grade = int(course[7])
        grades.append(grade)
    
    if len(grades) < 1:
        grade = grades
    else:
        # print("WILL IT RAISE?".center(50, "+"))
        grade = average(grades) # compute the whole terms

    return grade


def decorator(label):
    """Puts a design around a label (e.g. for each term."""
    decoration = "="*60  + "\n"  + "{:^15}".center(50, "*") + "\n" + "="*60
    return decoration.format(label)


def fullTranscriptFeature(csv_stdID, csv_studentDetails, level, typeofcourse):
    """Uses the transcriptFeature() in this code itself for all majors and minors"""
    transcriptFeature(csv_stdID, csv_studentDetails, level, typeofcourse)
    clearConsole()


def clearConsole():
    """Clears the console."""
    time.sleep(5)
    os.system("cls") # for windows_os / os.name==nt
    # call("cls" if os.name == "nt" else "clear") # this sometimes not work


def validate():
    """Validates the files to be displayed and encoded in text files."""
    csv_stdID= "201006000.csv"
    csv_studentDetails = "studentDetails.csv"
    typeofcourse =  None
    level = "U"
    transcriptFeature(csv_stdID, csv_studentDetails, level, typeofcourse)


if __name__ == "__main__":
	validate()
