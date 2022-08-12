class resturant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("restaurant name: ", self.restaurant_name)
        print("cuisine type: ", self.cuisine_type)

    def set_number_served(self, amount_custumers):
        self.number_served = amount_custumers
        print("custumers served:", self.number_served)

    def increment_number_served(self, custumer_inc_dec):
        self.number_served += custumer_inc_dec
        print("custumers served:", self.number_served)
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")
    
#my restaurant is created, its now an object just like a pen is an object, 
# and the properties are its name and what food it serves
my_restaurant = resturant("da vinci", 'tai foods')
#we now call the behaviours of the restaurant which is what the restaurant does and when it does it
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

print("custumers served:", my_restaurant.number_served)
my_restaurant.number_served = 30
print("custumers served:", my_restaurant.number_served)

my_restaurant.set_number_served(50)
my_restaurant.set_number_served(30)

my_restaurant.increment_number_served(60)


