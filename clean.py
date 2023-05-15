# clean.py Removes twitter specific stop words from the data 
# To run: python3 clean.py path_to_tweets_folder path_to_store_tweets 
# Command: python3 clean.py data cleaned
# Output: a file for tweets pertaining to each topic/hashtag
# output is in cleaned folder

import sys
import os
import re
import string
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk import pos_tag
				
def clean(path, filename):
	filename = os.path.join(CLEANED_DATA, filename.strip())
	WRITE_HANDLER = open(filename, 'w')
	tweets = dict()

	para = ''''''
	paraTokenCount = 0

	for line in open(path, 'r'):
		line = re.sub(r'[.,"!]+', '', line, flags=re.MULTILINE) # removes the characters specified
		line = re.sub(r'^RT[\s]+', '', line, flags=re.MULTILINE) # removes RT
		line = re.sub(r'https?:\/\/.*[\r\n]*', '', line, flags=re.MULTILINE) #remove link
		line = re.sub(r'[:]+', '', line, flags=re.MULTILINE)	
		line = list(filter(lambda x: x in string.printable, line)) # filter non-ascii characers
		
		new_line = ""	
	
		for i in line: # remove @ and #words, punctuataion
			if not i.startswith('@') and not i.startswith('#') and i not in string.punctuation:
				new_line+=i	
		
		# check if tweet is already added in our dictionary
		if(new_line in tweets):
			continue
		else:
			tweets[new_line] = 1

		new_line = new_line.strip()
		paraTokenCount += len(new_line.split())

		if paraTokenCount > 1000:
			WRITE_HANDLER.write(para + '\n')
			para = ''''''
			paraTokenCount = 0
		else:
			para += new_line + '.'

		# if(len(new_line.strip())>0):
		# 	WRITE_HANDLER.write(new_line + '.')
	
	if paraTokenCount <= 1000:
		WRITE_HANDLER.write(para)
	return filename

CWD = os.getcwd()		
DATA_FOLDER = os.path.join(CWD, "data")
CLEANED_DATA = os.path.join(CWD, "cleaned")

for root, dirs, files in os.walk(DATA_FOLDER): # gets all the files from subfolders recrsively
	for name in files:
		absolute_path = os.path.join(root, name)
		print(name, absolute_path)
		if os.path.isfile(absolute_path):
			clean(absolute_path, name)