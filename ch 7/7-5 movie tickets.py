age = ""
while age != "quit":
    age = input("write age or quit to quit: ")

    if int(age) <= 3:
        ticket_price="free"
    if int(age) > 3 and int(age) <= 12:
        ticket_price = 10
    if int(age) > 12:
        ticket_price = 15
    print(f"the ticket cost is {ticket_price}!")
        
    
