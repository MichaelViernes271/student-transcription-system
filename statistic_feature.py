import numpy as np
import csv, math

def statisticFeature(studentID_file):
    # the csv file
    csvfile = open(studentID_file, "r", encoding="UTF-8-SIG")
    data = csv.DictReader(csvfile, delimiter=",")
    # data = np.loadtxt(studentID_file, delimiter =",", dtype = str , skiprows = 1, encoding = 'bytes') #calling the file
    
    # gets the columns of grades and terms
    # for calculating: (1) averages and (2) max n min
    grades = []
    terms = []
    for line in data:
        # convert the data in float before appeding to list.
        # the list will be used for averaging
        grades.append(float(line['Grade']))
        terms.append(int(line['Term']))
    # debugging - ave_grade_terms
    # print("grades: ", grades)
    # print("terms: ", terms)
        
    stat_title = ["         Student Level         ", "="*60 ]
    print("="*60)
    for i in stat_title:
        if i == stat_title[0]: # for the title
            i = i.center(60, "*")
            print(i)
            continue
        i = "{:<}".format(i)
        print(i)
        
    def overAllAve():
        """Calculates overall averages."""
        ave_grade = round(sum(grades) / len(grades), 2)
        print("\nOverall average (major and minor) for all terms: ", str(ave_grade))

    def aveEachTerm():
        """Calculates average each term."""

        # initialize a list of averages in each term, 
        # max and min grade corresponding to term.
        term_list = []
        max_grade_in_term = 0
        min_grade_in_term = 0

        # get the max terms
        max_term = int(max(terms))
        # debugging
        # print("max terms: ", max_term, " type ", type(max_term), "\n"
            # "terms: ", terms, "type: ", type(terms))
        for n in range(1, max_term+1):
            # iterate till the max term, and match the term to calculate
            # filter only of same term
            term = []
            for i in range(len(terms)):
                # print("all grades", grades[i]) # debugging
                if n == terms[i]:
                    # print(grades[i])
                    term.append(grades[i])
            # term = [grades[i] for i in range(terms) if n == terms[i]]
            # CALCULATE AND PRINT THE TERM
            if len(term) > 0:
                term = sum(term)/len(term)
                term = math.floor(term)
                term_list.append(term)
            else:
                term_list.append(0)

        print("Average (major and minor) of each terms:", "\n")
        # print("terms length: ", max_term)
        # print("terms list: ", term_list)
        for i in range(1, max_term+1):
            print(f"\tTerm {i}: {term_list[i-1]:4.2f}", )
    
    def maxGrade():
        max_grade = max(grades)
        print ("\nMaximum grade(s) and in which term(s): ", max_grade)
        
    def minGrade():
        min_grade = min(grades)
        print ("Minimum grade(s) and in which term(s): ", min_grade)
    
    #def repeatedCourse(): # unused function
    #   pass


    overAllAve()    
    aveEachTerm()    
    maxGrade()
    minGrade()


def main():
    """Runs the main program."""
    # test values
    csv_file = input("Enter the csv file: ")
    csv_file = "201006000.csv"

    statisticFeature(csv_file)
    
if __name__ == '__main__':
    main()
