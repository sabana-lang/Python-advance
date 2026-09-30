f=open("data.json","r")
import json
content=json.load(f)
print(content)
f.close()