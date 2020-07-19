print("This Program is for generating a time update in html file to append from this script")
import datetime
import os
import webbrowser
"""
last_updated = datetime.datetime.now()
x = f'Last Updated on :{last_updated}'
with open("file.txt", 'a') as file:
    file.write(x)
    file.close()
"""
f = open('file.txt','r+')
x = datetime.datetime.now()
lines = f.readlines() # read old content
f.seek(0) # go back to the beginning of the file
f.write(str(x)) # write new content at the beginning
for line in lines: # write old content after new
      f.write(line)
      f.close()