import json

file = 'number.json'
try:
    with open(file) as f:
        number = json.load(f)
except:
    print(f"{file} doesnt excist!")
else:
    print(f"your favorite number is: {number}")