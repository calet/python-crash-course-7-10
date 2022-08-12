message = "write your toppings"
message += '\nor write quit to quit: '
choice = ""
pizza = []
joining = ""
while choice != "quit":
    choice = input(message)
    
    
    if choice != 'quit': 
        h = 0
        check = ""
        while h < len(choice)+1:
            if h < len(choice):
                check = choice[h]
            if h < len(choice) and check != ',' and check != ' ':
                joining += check
            else:
                if joining != '':
                    pizza.append('-' + joining)
                    joining = ""
            h+=1
        print("\nyour topings are:")
        print('\n'.join(pizza) + '\n')

            
        
      