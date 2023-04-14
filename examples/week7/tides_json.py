# Create and read from a json formatted file
# See: https://docs.python.org/3/library/json.html
import json

# Create a Python dictionary to store the 1 day of tide data
tides_dict = {'tides':
    [{'time': '12:02am', 'height': 1.20, 'kind': 'Low'},
     {'time': '06:23am', 'height': 9.60, 'kind': 'High'},
     {'time': '12:52pm', 'height': 0.09, 'kind': 'Low'},
     {'time': '07:13pm', 'height': 8.42, 'kind': 'High'}]}

# Create and write to the json file
with open('tides.json', 'w') as tides:
    json.dump(tides_dict, tides)

# Read and print the contents of the json file
with open('tides.json', 'r') as tides:
    print(json.dumps(json.load(tides), indent=4))