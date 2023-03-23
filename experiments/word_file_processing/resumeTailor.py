"""
make the resume tailor system 
"""

#imports 
from docx import Document


#const paramaters 
txtFile_path = "sample.txt"
wordFile_path = "Resume_15.docx"


def readTxt_file(filePath):
	"""
	The funcltionm to take the text and parse 
	"""
	keyWord_lst = []

	with open(txtFile_path) as f:
		[keyWord_lst.append(line.strip()+" ,") for line in f.readlines()]

	return keyWord_lst


def updateWord_file(wordFile_path,wordLst):
	"""
	The function to mainputate the word file 

	"""
	doc = Document(wordFile_path)
	doc.add_paragraph(wordLst)

	doc.save(wordFile_path)




if __name__ == "__main__":
	
	wordLst = readTxt_file(txtFile_path)
	updateWord_file(wordFile_path,wordLst)