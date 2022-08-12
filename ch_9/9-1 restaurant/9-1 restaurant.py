class resturant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"restaurant name: ", self.restaurant_name)
        print(f"cuisine type: ", self.cuisine_type)
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")
    
#my restaurant is created, its now an object just like a pen is an object, 
# and the properties are its name and what food it serves
my_restaurant = resturant("da vinci", 'tai foods')

#we now call the behaviours of the restaurant which is what the restaurant does and when it does it
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

    
    