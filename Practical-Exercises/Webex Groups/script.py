import json
import yaml
# load json file
with open('data.json') as json_file:
    data = json.load(json_file)

# Write a Python script to select the name of the first person in the first group
print("-----------------------1-------------------------")

# select first group and first person
first_group = data['groups'][0]['group']
first_person = first_group['members'][0]

# print the name of the first person
print(first_person['person_name'])

# Write a Python script to make a list of all names and email addresses
print("-------------------2---------------------------")

# create empty lists to store names and emails
names = []
emails = []

# iterate through groups and members
for group in data['groups']:
    for member in group['group']['members']:
        names.append(member['person_name'])
        emails.append(member['email'])

# print the lists
print("Names:", names)
print("Emails:", emails)

# Write a Python script to make a list of all names and email addresses of DEVASC_B
print("-----------------------3-----------------------")

# create empty lists to store names and emails
names = []
emails = []

# iterate through groups and members
for group in data['groups']:
    if group['group']['group_name'] == 'DEVASC_B':
        for member in group['group']['members']:
            names.append(member['person_name'])
            emails.append(member['email'])

# print the lists
print("Names:", names)
print("Emails:", emails)


print('')
print(">>>>>>>>>>>>>>>>>>>")
print('convert json to yaml')
print('>>>>>>>>>>>>>>>>>>>>>')
yaml_data = yaml.dump(data)
print(yaml_data)
