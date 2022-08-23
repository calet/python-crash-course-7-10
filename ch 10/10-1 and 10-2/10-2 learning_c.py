#stores all lines in a list and then print line by line
with open('learning_python.txt') as learning:
    lines = learning.readlines()

file_lines = ""
for file_line in lines:
    file_lines+= file_line

modified_lines = file_lines.replace('python', 'c#')
print(modified_lines)