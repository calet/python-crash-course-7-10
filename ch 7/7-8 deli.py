sandwich_orders = ["grilled cheese", "grilled chicken", "turkey", "roast beef", "french dip"]

finished_sandwich = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"your {sandwich} is done!")

    finished_sandwich.append('\n-' + sandwich)

print(f"\nfinnished sandiwiches: {''.join(finished_sandwich)}")
