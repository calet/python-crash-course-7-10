number = int(input("say a number: "))
if number % 10 == 0:
    print(f"{number} is divisible by 10")
    print(f"10 goes {number//10} times in {number}")
else:
    print(f"{number} is not divisible by 10, because the remainder is {number%10}")
    print(f"10 goes {number//10} times in {number}")
    if number < 10:
        print(f"for it to be divisible by 10 you need atleast {10-number} more")