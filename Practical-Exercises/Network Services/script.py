import json

with open("Network Services\data.json") as json_file:
    data = json.load(json_file)
print("--------------------1----------------------")
# Write Python code to make a list of all servers, services, ip addresses, protocol/ports
servers = []
services = []
ip_addresses = []
protocol_ports = []

for server in data["rack"]:
    servers.append(server["server"]["server_name"])
    ip_addresses.append(server["server"]["ip-address"])
    for service in server["server"]["services"]:
        services.append(service["service"])
        protocol_ports.append(f"{service['protocol']}/{service['port']}")

print("Servers: ", servers)
print("Services: ", services)
print("IP Addresses: ", ip_addresses)
print("Protocol/Ports: ", protocol_ports)

print("")
print("--------------------2---------------------------")
# Write Python code to select the name of the first server

first_server_name = data["rack"][0]["server"]["server_name"]
print("First Server: " + first_server_name)
print("")
print("-----------------3-----------------------")

# Write Python code to make a list of all services and protocol/ports of server S3
s3_services = []
s3_protocol_ports = []

for server in data["rack"]:
    if server["server"]["dev_id"] == "S3":
        for service in server["server"]["services"]:
            s3_services.append(service["service"])
            s3_protocol_ports.append(
                f"{service['protocol']}/{service['port']}")

print("Services of S3: ", s3_services)
print("Protocol/Ports of S3: ", s3_protocol_ports)
