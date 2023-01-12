import json

# load the JSON data from file
with open('data.json', 'r') as json_file:
    response_json = json.load(json_file)

# DISPLAY FILTERED RESULTS
print("Displaying partial information")
# print(type(res))
print("Name: " + response_json['displayName'])
print("Created: " + response_json['created'])
print("User Type: " + response_json['type'])
print("User Status: " + response_json['status'])
