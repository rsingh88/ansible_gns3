#! /usr/bin/python3
import os
import json


ihsm_dir = os.path.join(os.getcwd(),"snmp_write")
file_list =  os.listdir(ihsm_dir)
print(len(file_list))
temp = {}

for file in file_list:
    file_split = file.split(".")
    print(file)
    hostname = file_split[0]
    file_open = open(os.path.join(ihsm_dir,file), 'r')
    file_read = file_open.read()
    file_read = json.loads(file_read)
    temp[hostname] = []
    # print("\n\n\n")
    # print(file_read['stdout_lines'])
    for line in file_read['stdout_lines'][0]:
        # print(line)
        if "10.170.3.35" in line:
            # print(line)
            temp[hostname].append(line)
        if "10.242.3.68" in line:
            # print(line)
            temp[hostname].append(line)
        if "10.242.3.69" in line:
            # print(line)
            temp[hostname].append(line)
        if "10.242.3.55" in line:
            # print(line)
            temp[hostname].append(line)
        if "snmp-server community Cf9m9m7" in line:
            # print(line)
            temp[hostname].append(line)
        # if " 8" in line:
        #     print(line) 
        #     temp[hostname].append('ACL 8')

data = json.dumps(temp)
f = open("final_output.json", "w")
f.write(data)
print(data)
f.close

