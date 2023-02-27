from transcript_feature import transcriptFeature

def majorTranscriptFeature(csv_stdID, csv_studentDetails, typeofcourse):
	"Uses the transcriptFeature() for all majors"
	transcriptFeature(csv_stdID, csv_studentDetails, typeofcourse)


def validate():
    """Validates the files to be displayed and encoded in text files."""
    csv_stdID= "201006000.csv"
    csv_studentDetails = "studentDetails.csv"
    typeofcourse =  "major"
    level = "U"
    transcriptFeature(csv_stdID, csv_studentDetails, level, typeofcourse)


if __name__ == "__main__":
	validate()