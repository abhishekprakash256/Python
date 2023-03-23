"""
The program to process the text file and give out a text file of keywords not in the resume 
"""
#imports 
from docx import Document
import re

#file path 

keyWord_file = "jobkeyword.txt"
resume_file = "Resume_15.docx"
missing_file = "missingKeyword.txt"


def readKeyword(keyWord_file):
	"""
	The program to read the keyword file and generate the hashmap
	"""
	wordLst = []
	
	with open(keyWord_file) as f:
		
		for line in f:
			for word in line.split():
				wordLst.append(word)

	return wordLst

def findKeywords(resume_file,missing_file, wordLst):
	"""
	Find the missing keyword in the file and generate the missing keyword file 
	"""
	doc = Document(resume_file)

	match = "Abhishek"

	# Loop through each paragraph in the docx
	for para in doc.paragraphs:
		for word in para.text.split():
			 print(word)




	"""
	# Loop through each word in the paragraph
		for word in para.text.split():
			# If the word matches the search word, print the paragraph
			if word == wordLst[0]:
				print(para.text)

		else:
			print(word)
	"""







if __name__ == "__main__":
	res = readKeyword(keyWord_file)
	findKeywords(resume_file,missing_file,res)

	#findKeywords(resume_file,missing_file,res)

