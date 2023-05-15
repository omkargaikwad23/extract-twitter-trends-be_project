# extractive summary

import os
import openai

# Set your API key
openai.api_key = "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"

CWD = os.getcwd()
CLEANED_DIR = os.path.join(CWD, 'cleaned')
SUMMARY_DIR = os.path.join(CWD, 'summary')


def getSummaryUtil(text):
    LENGTH = 2000 # define the summary length

    model_engine = "text-davinci-002"
    prompt = (f"Summarize the following text in {LENGTH} words or fewer: "
            f"{text}")
    completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=LENGTH, n=1,stop=None,temperature=0.5)
    summary = completions.choices[0].text

    return summary


def getFileSummary(path, filename):
    filename = os.path.join(SUMMARY_DIR, filename.strip())
    WRITE_HANDLER = open(filename, 'a')

    
    for line in open(path, 'r'):
        fileSummary = getSummaryUtil(line)
        WRITE_HANDLER.write(fileSummary + "\n")
	

for root, dirs, files in os.walk(CLEANED_DIR): # gets all the files from subfolders recrsively
	for name in files:
		absolute_path = os.path.join(root, name)
		# print(name, absolute_path)
		if os.path.isfile(absolute_path):
			filename = getFileSummary(absolute_path, name)
	