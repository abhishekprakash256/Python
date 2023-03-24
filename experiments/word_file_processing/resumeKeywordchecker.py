"""
The program to process the text file and give out a text file of keywords not in the resume 
"""
#imports 
from docx import Document
import re

#file path 

keyWord_file = "jobkeyword.txt"
resume_file = "Resume_14.docx"
missing_file = "missingKeyword.txt"


def readKeyword(keyWord_file):
	"""
	The program to read the keyword file and generate the hashmap
	"""
	wordLst = []
	
	with open(keyWord_file) as f:
		
		for line in f:
			for word in line.split():
				wordLst.append(word.lower())

	return wordLst

def findKeywords(resume_file,missing_file, wordLst):
	"""
	Find the missing keyword in the file and generate the missing keyword file 
	"""
	doc = Document(resume_file)
	resumeWords_lst = []

	# Loop through each paragraph in the docx
	for para in doc.paragraphs:
		
		for word in para.text.split():
			new_text = ""
			for character in word:
				if character.isalnum():
					new_text += character
			resumeWords_lst.append(new_text.lower())

	return resumeWords_lst


def missingKey(missing_file,wordLst,resumeWords_lst):
	"""
	Find the missing words in the resume and put it in the file
	"""
	missingWords = []
	len_wordLst = len(wordLst)
	len_resumeWords = len(resumeWords_lst)

	wordLst = set(wordLst)
	resumeWords = set(resumeWords_lst)

	#compare the two list 
	commonWords = (wordLst.intersection(resumeWords))
	missingWords = (wordLst - commonWords)

	#adding to the file 
	file = open(missing_file, "w")  # write mode
	
	for words in missingWords:
		file.write(words+"\n")

	#find the percentage of the words 
	percentageMissing = (len(commonWords)/len(wordLst))*100

	print("The percentage of the matching with the job description:" + " " + str(round(percentageMissing)) + '%')


if __name__ == "__main__":
	wordLst = readKeyword(keyWord_file)
	resumeWords_lst = findKeywords(resume_file,missing_file,wordLst)
	missingKey(missing_file,wordLst,resumeWords_lst)