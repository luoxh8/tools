import json

with open('json1.json') as f: json1 = json.loads(f.read())
with open('json2.json') as f: json2 = json.loads(f.read())

json1.update(json2)
print(json1)
