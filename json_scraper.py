import time
import os
import json
import urllib

unix_time = str(int(time.time()))
print(unix_time)

dir_path_this = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path_this)

URL = 'https://www.govtrack.us/data/congress/113/votes/2013/s11/data.json'
# That's some example URL to json data found in the SO thread
# 19915010/python-beautiful-soup-how-to-json-decode-to-dict
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

#with open(file_name) as infile:
#    loaded_data = json.load(infile)