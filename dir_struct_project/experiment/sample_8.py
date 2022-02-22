"""
read the data from the json file 
"""

import json

#opening the json file

config_file = open("config.json")

#loading the data as dictionary 
data = json.load(config_file)


#accessing the elements 
print(data['repo_details'][0]['project_name'])

#accessing the elements 
print(data['repo_details'][0]['author'])

#accessing the elements 
print(data['repo_details'][0]['version'])

config_file.close()