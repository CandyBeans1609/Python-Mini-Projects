import os
import re

# Function to search for a phone number in a given file
def search(file, pattern=r'\d{3}-\d{3}-\d{4}'):
    f = open(file, 'r')
    text = f.read()
    
    # Search for the pattern in the file content
    if re.search(pattern, text):
        return re.search(pattern, text)
    else:
        return ''

# List to store results
results = []

# Walk through the directory and its subdirectories
for folder, sub_folders, files in os.walk(os.getcwd() + "\\Regular Expression\\extracted_content"):
    
    for f in files:
        full_path = folder + '\\' + f
         
        results.append(search(full_path)) 


for r in results:
    if r != '':
        print("Phone number found: ", r.group())
