from my_locations import city_country
from display_all_locations import display_all as d_a

location = []
my_city = ""
my_country = "2"

while True:
    print("-country/city-")
    print("(write 1 to quit and 2 to display all country/city pairs)")
    my_city = input("write city: ")
    print("")
    if my_city == '1':
        break
    elif my_city == '2':
        if location:
            d_a(location)
        else:
            print("--no locations found--\n")
        
    else:
        while my_country == '2':
            my_country = input("write country: ")
            print("")
            if my_country == '1':
                exit()
            elif my_country == '2':
                if location:
                    d_a(location)
                    print(f"pending: {my_city}\n")
                else:
                    print("--no locations found--")
                    print(f"pending: {my_city}\n")
            else:
                location.append(city_country(my_city, my_country))
        my_country = '2'       


    
