import json


# load the JSON data from file
with open('data.json', 'r') as json_file:
    docker_dict = json.load(json_file)

print("---------1--------")
print("Converting json string to dict, and showing keys at level 1")

print(docker_dict[0].keys())
print("---------2--------")
print("Converting dict to raw json")
docker_json2 = json.dumps(docker_dict)
print("Filtering from dict")
print(docker_dict[0]["Name"])
print(docker_dict[0]["Created"])
print(docker_dict[0]["Containers"]
      ["4e99a64e10dfcf6608a1d47f4349676c745bf234cebd52826d786db9a3be2811"]["IPv4Address"])
