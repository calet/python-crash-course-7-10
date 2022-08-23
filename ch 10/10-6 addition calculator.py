def number_check(number):
    try:
        return int(number)
    except ValueError:
        print("you can only add numbers!\n")
       
while True: 
    h = input("write a number (write q to quit): ")
    if h == 'q':
        break
    if number_check(h):
        while True:
            u = input("write another number (write q to quit): ")
            if u == 'q':
                break
            if number_check(u):
                sum = number_check(h) + number_check(u)
                print(f"the sum is: {sum}\n")
                break
    
 
    
