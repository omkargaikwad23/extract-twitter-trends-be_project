# importing libraries
import nltk
# nltk.download('stopwords')
# stopwords = nltk.corpus.stopwords.words('english')
# from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Creating list of stopwords
stopList = []

# Stopwords are stored in a file stopwords.txt
with open('stopwords.txt', 'r') as f:
	for line in f:
		word = line.strip('\n')
		stopList.append(word)

# Input text - to summarize
text = """ There are many techniques available to generate extractive summarization to keep it simple, I will be using an unsupervised learning approach to find the sentences similarity and rank them. Summarization can be defined as a task of producing a concise and fluent summary while preserving key information and overall meaning. One benefit of this will be, you don’t need to train and build a model prior start using it for your project. It’s good to understand Cosine similarity to make the best use of the code you are going to see. Cosine similarity is a measure of similarity between two non-zero vectors of an inner product space that measures the cosine of the angle between them. Its measures cosine of the angle between vectors. The angle will be 0 if sentences are similar."""

# Tokenizing the text
stopWords = set(stopList)
words = word_tokenize(text)

# Creating a frequency table to keep the
# score of each word
freqTable = dict()
for word in words:
	word = word.lower()
	if word in stopWords:
		continue
	if word in freqTable:
		freqTable[word] += 1
	else:
		freqTable[word] = 1

# Creating a dictionary to keep the score
# of each sentence
sentences = sent_tokenize(text)
sentenceValue = dict()

print(sentences)

for sentence in sentences:
	for word, freq in freqTable.items():
		if word in sentence.lower():
			if sentence in sentenceValue:
				sentenceValue[sentence] += freq
			else:
				sentenceValue[sentence] = freq


sumValues = 0
for sentence in sentenceValue:
	sumValues += sentenceValue[sentence]

# Average value of a sentence from the original text

average = int(sumValues / len(sentenceValue))

# Storing sentences into our summary.
summary = ''
for sentence in sentences:
	if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
		summary += " " + sentence
print(summary)
