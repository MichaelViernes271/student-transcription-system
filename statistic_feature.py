import numpy as np

def statisticFeature():
    file = "201006000.csv" # the csv file
    data = np.loadtxt(file, delimiter =",", dtype = str , skiprows = 1, encoding = 'bytes') #calling the file
    
    grades = np.asarray(data[:,7], dtype = int)
    terms = np.asarray(data[:,2], dtype = int)
    terms_w_grade = np.column_stack((terms,grades))

    
    #ave_grade_terms
        
    stat_title = ["         Undergraduate level         ", "="*60 ]
    print("="*60)
    for i in stat_title:
        if i == stat_title[0]: # for the title
            i = i.center(60, "*")
            print(i)
            continue
        i = "{:<}".format(i)
        print(i)
        
    def overAllAve(): 
        ave_grade = sum(grades) / len(grades)
        print("\nOverall average (major and minor) for all terms: ", str(ave_grade))

    def aveEachTerm():
        term1 = sum(terms_w_grade[0:3,1])/len(terms_w_grade[0:3,1])
      
        term2 = sum(terms_w_grade[3:6,1])/len(terms_w_grade[3:6,1])
               
        term3 = sum(terms_w_grade[6:7,1])/len(terms_w_grade[6:7,1])
        
        print("Average (major and minor) of each terms:","\n    Term 1: ", term1, "\n    Term 2: ",term2, "\n    Term 3: ", term3)
    
    def maxGrade():
        max_grade = max(grades)
        print ("\nMaximum grade(s) and in which term(s): ", max_grade)
        
    def minGrade():
        min_grade = min(grades)
        print ("Minimum grade(s) and in which term(s): ", min_grade)
    
    #def repeatedCourse():
    overAllAve()    
    aveEachTerm()    
    maxGrade()
    minGrade()
statisticFeature()
