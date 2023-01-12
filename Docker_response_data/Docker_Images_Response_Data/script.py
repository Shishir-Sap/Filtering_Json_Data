import json

# load the JSON data from file
with open('data.json', 'r') as json_file:
    docker_dict = json.load(json_file)
print("---------1--------")
print("Converting json string to dict, and showing keys at level 1")

print(docker_dict[0].keys())
print("---------2--------")
print("Converting dict to raw json")
docker_json = json.dumps(docker_dict)
print("---------3--------")
print("Filtering from dict")
print(docker_dict[0]["Created"])
print(docker_dict[0]["Architecture"])
print(docker_dict[0]["Os"])
