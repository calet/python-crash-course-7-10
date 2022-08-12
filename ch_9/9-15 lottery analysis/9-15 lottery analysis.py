from random import choice
from random import randint

lottery = ['a', 'h', '6', '1', 'f', 'u', '3', 'o', '9', '10', '2', '18', '13', '5', '7']
picked = 0
chosen = []
while picked < 4:
    chosen.append(choice(lottery))
    picked+=1
print("the winner is: " + ', '.join(chosen))

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

my_ticket = []
my_chosen_ticket = []
all_tickets = 0
while my_chosen_ticket != chosen:
    while len(my_ticket) < 15:
        my_ticket.append(str(randint(1, 20)))
        if len(my_ticket) < 15:
            my_ticket.append(choice(alphabet))
#if you want do so it doesnt include 
#already drawn tickets when selecting my_chosen_ticket
    while len(my_chosen_ticket) < 4:
        my_chosen_ticket.append(choice(my_ticket))
    all_tickets+=1
    if all_tickets%100000 == 0:
        print("current ticket: " + ', '.join(my_chosen_ticket))
        print(f"amount of tickets: {all_tickets}")
    if my_chosen_ticket != chosen:
        
        my_chosen_ticket = []
        my_ticket = []
  
    

print("my ticket is correct: " + ', '.join(my_chosen_ticket))

