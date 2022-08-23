with open('txt_files\\million_pi.txt') as file_object:
    lines = file_object.readlines()

line = ""
for l in lines:
    line+=l

if str(9) in line:
    print("your id number is in pi!")
else:
    print("your id number is not in pi!")

print(len(line))