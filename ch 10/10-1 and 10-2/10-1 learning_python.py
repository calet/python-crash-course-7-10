#prints line by line
with open('learning_python.txt') as learning:
    for line in learning:
        print(line.rstrip())
print('\n')
#prints whole txt file
with open('learning_python.txt') as learning:
    all = learning.read()
print(all)
print('\n')
#stores all lines in a list and then print line by line
with open('learning_python.txt') as learning:
    lines = learning.readlines()
file_lines = ""
for file_line in lines:
    file_lines+= file_line
print(file_lines)