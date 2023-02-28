from transcript_feature import transcriptFeature

def minorTranscriptFeature(csv_stdID, csv_studentDetails, level, typeofcourse):
	"""Uses the transcriptFeature() for all minors"""
	transcriptFeature(csv_stdID, csv_studentDetails, level, typeofcourse)


def validate():
    """Validates the files to be displayed and encoded in text files."""
    csv_stdID= "201006000.csv"
    csv_studentDetails = "studentDetails.csv"
    typeofcourse =  "minor"
    level = "U"
    transcriptFeature(csv_stdID, csv_studentDetails, level, typeofcourse)


if __name__ == "__main__":
	validate()