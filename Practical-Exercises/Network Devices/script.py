import json
import yaml
# load the JSON data from file
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

print("----------------------1--------------------------------------")
# Write a Python script to select the name and IP Address of the first device

# access the first device in the rack
first_device = data['rack'][0]['device']
# extract the name and IP address of the first device
name = first_device['dev_name']
ip_address = first_device['interfaces'][0]['ipaddress']

# print the name and IP address
print("Name:", name)
print("IP Address:", ip_address)

print("---------------------------2------------------------------")
# Write a Python script to display all network devices, interfaces and IP addresses

for device in data['rack']:
    name = device['device']['dev_name']

    # loop over all the interfaces of the device
    for interface in device['device']['interfaces']:
        # extract the interface name and IP address
        interface_name = interface['interface']
        ip_address = interface['ipaddress']

        # print the device name, interface name, and IP address
        print("Device:", name)
        print("Interface:", interface_name)
        print("IP Address:", ip_address)

print("----------------------3--------------------------------")
# Write a Python script to display all interfaces and IP addresses of device R1

# loop over all the devices
for device in data['rack']:
    # check if the device name is "R1"
    if device['device']['dev_name'] == "R1":
        # loop over all the interfaces of the device
        for interface in device['device']['interfaces']:
            # extract the interface name and IP address
            interface_name = interface['interface']
            ip_address = interface['ipaddress']

            # print the interface name and IP address
            print("Interface:", interface_name)
print('')
print(">>>>>>>>>>>>>>>>>>>>")
print('Convert json to yaml')
print(">>>>>>>>>>>>>>>>>>>>")
yaml_data = yaml.dump(data)
print(yaml_data)
