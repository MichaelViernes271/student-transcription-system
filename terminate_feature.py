def terminateFeature(counts):
	"""Prints the counted number of accesses in the options menu,then exits."""

	input("There were {} accessed options. ".format(counts))
	return 0


def main():
	"""Runs the main program.
	NOTE: COPY THIS SNIPPET OF MAIN() TO THE MAIN.PY, AND ADJUST THE CODE."""

	counts = 0 # counter for accessed options
	while True:
		try:
			userInput = input("Enter your option: ")

			if userInput == "quit":
				terminateFeature(counts)
				break
			
			counts+=1 # counts every access options
		except:
			print("Enter Appropriate data.")


if __name__ == '__main__':
	main()