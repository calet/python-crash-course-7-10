import json

'''functions'''
#open file and check if it excist
#if it excist print favorite number
#else input number
#what file

#run twice to check if it works
def my_file():
    file = 'number.json'
    return file

def load_number_file():
    file = my_file()
    try:
        with open(file) as f:
            number = json.load(f)
    except:
        return None
    else:
        return number

def input_number():
    number = input("what is your favorite number?: ")

    file = my_file()
    with open(file, 'w') as f:
        json.dump(number, f)

def print_number():
    my_number = load_number_file()

    if my_number:
        print(f"your number is: {my_number}")
    else:
        input_number()

print_number()