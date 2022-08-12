import build_car_profile as b_c_p

my_car_info = b_c_p.car_info("rolce royce", "phantom saloon", doors=2, color='white, gray', cost="2 000 000")

car_items = list(my_car_info.items())

mode = car_items[-1]
manu = car_items[-2]
cost = car_items[-3]

car_items.insert(0, manu)
car_items.insert(1, mode)
car_items.insert(2, cost)

my_car_info = dict(car_items)

print("my car:")
for i, k  in my_car_info.items():
    print(f"- {i}: {k}")