guest_name = input("write your name: ")

with open('guests.txt', 'r+') as guest_list:
    guest_list.write(f"{guest_name}\n")
    
with open('guests.txt') as read_guest_list:  
    guests = read_guest_list.read()

print(guests)
