# =========================================================
# Date: 07/29/2018
# Author: @SP
# Description: Essential CSV File Utility Scripts
# =========================================================

import csv
import os 
import re


# 1. ] Get Count of all rows in all csv files under any given path(also looks into sub directories)

def csvRowCount():

    filepath = 'C:/'  # Insert your file path

    count = 0  # Defining Counter to keep track of total rows

    for root, dirs, files in os.walk(filepath):
        for f in files:
            if f.endswith('.csv'):
                filepath = root + os.sep + f
                with open(filepath,"r") as my_file:
                    count = count + sum(1 for line in csv.reader(my_file,delimiter = ","))

    return count
	

# 2.] Get avg no of columns in all csv files under any given path (also looks into sub directories)

def csvAvgColumnCount():

    filepath = 'C:/'  # Insert your file path


    totalcols = 0
    totalfiles = 0
    for subdir, dirs, files in os.walk(filepath):
        for file in files:
            myfile = subdir + os.sep + file
            with open(myfile, 'r') as f1: 
                csvlines = csv.reader(f1, delimiter=',')
                if myfile.endswith(".csv"):
                    totalfiles = totalfiles + 1
                    for lineNum, line in enumerate(csvlines):
                        if lineNum == 0:
                            totalcols = totalcols + len(line)
                        else:
                            break
                else:
                    pass
    return int(totalcols/totalfiles)


# 3.] Get Frequency of every word in all csv files under any given path (also looks into sub directories) 

def wordFrequency():
	filepath = 'C:/'  # Insert your file path

	frequency = {}  # Defining a dictionary to store key, value pairs
	
	for subdir, dirs, files in os.walk(filepath):
	
		for file in files:

			myfile = subdir + os.sep + file
			
			if myfile.endswith(".csv"):
			
				document_text = open(myfile, 'r')
				text_string = document_text.read()
				match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
				
				for word in match_pattern:
				
					count = frequency.get(word,0)
					frequency[word] = count + 1

	return frequency