"""
read the text from the text file 
"""
lst = []

with open('sample.txt') as f:
    [lst.append(line.strip()) for line in f.readlines()]

print(lst)