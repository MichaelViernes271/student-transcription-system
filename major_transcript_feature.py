from transcript_feature import transcriptFeature

def majorTranscriptFeature(csv_stdID, csv_studentDetails, typeofcourse):
	transcriptFeature(csv_stdID, csv_studentDetails, typeofcourse)

if __name__ == "__main__":
	# testing the program
	csv_stdID = "201006000.csv"
	csv_studentDetails = "studentDetails.csv"
	typeofcourse =  "major"
	transcriptFeature(csv_stdID, csv_studentDetails, typeofcourse)