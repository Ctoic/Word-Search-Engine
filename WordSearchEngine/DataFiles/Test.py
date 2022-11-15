# Import Module
import os

# Folder Path
path = "Enter Folder Path"

# Change the directory
os.chdir(Algorithms/DataFiles)

# Read text File


def read_text_file(file_path):
	with open(file_path, 'r') as f:
		print(f.read())


# iterate through all file
for file in os.listdir():
	# Check whether file is in text format or not
	if file.endswith(".txt"):
		file_path = f"{path}/{file}"

		# call read text file function
		print(read_text_file(file_path))
