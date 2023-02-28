# This work done by group 3:
# Mary Joy Aban, 25%
# Leon Adriel Franco Acaoili, 25%
# Reiven Cabate, 25%
# Michael Viernes, 2021-05811-MN-0, 25%

from user_input import userInput
from menu_feature import menuFeature
from major_transcript_feature import majorTranscriptFeature
from minor_transcript_feature import minorTranscriptFeature

def main():
	"""The main program."""

	# testing the customized modules
	# menuFeature()
	# userInput()
	validate()


def validate():
	"""Validates the files to be displayed and encoded in text files."""
	csv_stdID= "201006000.csv"
	csv_studentDetails = "studentDetails.csv"
	typeofcourse =  "minor"
	level = "U"

	majorTranscriptFeature(csv_stdID, csv_studentDetails, level, typeofcourse)
	print("x"*100)
	typeofcourse = "major"
	minorTranscriptFeature(csv_stdID, csv_studentDetails, level, typeofcourse)
	
if __name__ == "__main__":
	main()