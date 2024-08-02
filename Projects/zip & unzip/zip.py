import shutil

dir_to_zip = r"C:\Users\Akanksha\Documents\GitHub\Python-Mini-Projects\Projects\zip & unzip\input"
output = 'example'
shutil.make_archive(output, 'zip', dir_to_zip)
