f=open("data.json","w")
import json
content=[
    {"Name":"Arun","Age":23},
    {"Name":"Amal","Age":24}
    ]
json.dump(content,f) #json.dump() takes Python data and writes it into a file in JSON format.
f.close()