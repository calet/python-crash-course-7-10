user_input = ""

while True:
    '''
    display = "write your name: "
    display += "\n(write q to quit) "
    '''
    display = "write your name (write q to quit): "
    user_input = input(display)
    if user_input == 'q':
        break
    with open('guest_book.txt', 'a') as guest_list:
        guest_list.write(f"{user_input}\n")
    
with open('guest_book.txt') as read_guest_list:  
    guests = read_guest_list.read()

print()
print(guests)
