import json

json_obj = {
    "Name": "Shouvik", 
    "Branch":"CCE", 
    "Roll No.":27, 
    "Registration No.":210953174
    }

print(json.dumps(json_obj) + " " + str(type(json.dumps(json_obj))))

_str = "{\"Name\": \"Shouvik\", \"Branch\": \"CCE\", \"Roll No.\": 27, \"Registration No.\": 210953174}"

print(json.loads(_str), str(type(json.loads(_str))))

