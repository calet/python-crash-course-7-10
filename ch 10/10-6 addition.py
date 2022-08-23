try:
    h = int(input("write a number: "))
    u = int(input("write another number: "))
except ValueError:
    print("you can only add numbers!")
else:
    j = h+u
    print(f"the sum of {h} and {u} is:", j)