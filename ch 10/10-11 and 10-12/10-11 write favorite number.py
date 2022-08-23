import json

number = input("what is your favorite number?: ")

with open('number.json', 'w') as f:
    json.dump(number, f)