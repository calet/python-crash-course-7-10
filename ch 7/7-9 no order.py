sandwich_orders = ["grilled cheese", "grilled chicken", "turkey", "roast beef", "french dip"]

finished_sandwich = []

order = input("what would you like to order?: ")

sandwich_orders.insert(2, order)
sandwich_orders.insert(4, order)
sandwich_orders.insert(0, order)

for orders in sandwich_orders:
    print(f"orders: {orders}")

while order in sandwich_orders:
    sandwich_orders.remove(order)

new_order = order

while new_order == order:
    new_order = input(f"\nwe have run out of {order}, please order again!\n")

sandwich_orders.insert(2, new_order)
sandwich_orders.insert(4, new_order)
sandwich_orders.insert(0, new_order)

sandwich_orders.reverse()
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"your {sandwich} is done!")

    finished_sandwich.append('\n-' + sandwich)

print(f"\nfinnished sandiwiches: {''.join(finished_sandwich)}")