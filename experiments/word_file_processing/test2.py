"""
read the text from the text file 
"""
text = 'datagy -- is. great!'
new_text = ''

for character in text:
    if character.isalnum():
        new_text += character

print(new_text)