import csv, math

def transcriptFeature(filename, typeofcourse=None):
    # Open the CSV file
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        # Initialize variables for major/minor courses and grades
        row = csv_reader
        courseid = []
        coursename = []
        credithours = []
        grade = []
        terms = []
        courses = [x for x in row if x[5].lower() == typeofcourse]

        # Read each row in the CSV file
        # by the respective columns of vars based on majors
        for x in courses:
            coursename.append(x[3])
            courseid.append(x[4])
            grade.append(int(x[7]))
            credithours.append(int(x[6]))
            terms.append(int(x[2]))

        overall_average = average(grade) # compute overall average in terms
        
        print("Course names:\n", coursename)
        print("CourseIDs:\n", courseid)
        print("Credit Hours:\n", credithours)
        print("Grade:\n", grade)
        print("Overall Average:\n", overall_average)

        for term in range(1, max(terms)+1):
            display_transcript(term, terms,
                coursename, courseid, grade, credithours)


def display_transcript(term, terms, coursename, courseid, grade, credithours):
    """print the transcript based on major and minor"""

    grades = []
    print(f"for the term {term}:")
    for i in range(len(terms)):
        if term == terms[i]:
            # selecting grades of this term
            grades.append(grade[i])

            print(coursename[i])
            print(courseid[i])
            print(credithours[i])
            print(grade[i])

    print(f"average for this {term} sem: {average(grades)}", )

def average(grade):
    # rounded to 2 decimals by format
    overall_average = round((math.fsum(grade)/len(grade)), 3)
    overall_average = f"{overall_average:4.2f}"
    return overall_average

if __name__ == "__main__":
    # testing
    transcriptFeature("201006000.csv", "major")