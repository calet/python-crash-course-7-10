from random import choice

lottery = ['a', 'h', '6', '1', 'f', 'u', '3', 'o', '9', '10', '2', '18', '13', '5', '7']
picked = 0
chosen = []
while picked < 5:
    chosen.append(choice(lottery))
    picked+=1
print("the winner is: " + ', '.join(chosen))

