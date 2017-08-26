import os
import time
import json
import urllib

dir_path_file = os.path.realpath(__file__) # Get the director path of this file
dir_path_this = os.path.dirname(dir_path_file)
os.chdir(dir_path_this) # Set the working directory to the folder we are in

URL = 'https://www.govtrack.us/data/congress/113/votes/2013/s11/data.json'
# That's some example URL to json data found in the following Stack Overflow thread
# https://stackoverflow.com/questions/19915010/python-beautiful-soup-how-to-json-decode-to-dict
# You find this format everywhere today

response = urllib.urlopen(URL)
raw_data = response.read()
data = json.loads(raw_data) # translate it to Python data
print(data)

filename = 'my_data.json'
with open(filename, 'w') as outfile:
    json.dump(data, outfile) # write Python data into a file

# MINUTES = 60 # sixty seconds
# for i in range(12*60*MINUTES):
#     print(i)
#     # <add some code here>
#     time.sleep(10*MIN)

#with open(filename) as infile:
#    loaded_data = json.load(infile)
