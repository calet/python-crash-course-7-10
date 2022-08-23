import os
def quit(choice):
    if choice == 'q':
        return False

while True:
    user_name = input("write your name (write q to quit): ")
    if quit(user_name) == False:
        break
    language = input("whats your programming language? (write q to quit): ")
    if quit(language) == False:
        break
    reason = input(f"whats your reason for liking {language}? (write q to quit): ")
    if quit(reason) == False:
        break
    
    print()
    
    save = f"{user_name}:\n{language}:\n\t-{reason}"
    
    with open('programming_poll.txt', 'a') as guest_list:
        guest_list.write(f"{save}\n")

if os.path.exists('programming_poll.txt'):   
    with open('programming_poll.txt') as read_guest_list:  
        guests = read_guest_list.read()

    print()
    print(guests)
