#this is a class which means its the blueprint of our restaurants.
#to create a restaurant we first need to create the properties of them,
#that is called instantiation, because (in this example) 
#the restaurant da vinci isnt the the restaurant victoria, but they use the same properties, 
#and followed by the behaviours (open and description) is called a blueprint which is used to create more restaurants.
class Resturant:
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
my_restaurant = Resturant("da vinci", "tai foods")

#we now call the behaviours of the restaurant which is what the restaurant does and when it does it
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

#we now do the same but for two other restaurants, as in we create two more restaurants
your_restaurant = Resturant("victoria", "pizza")
your_restaurant.describe_restaurant()
your_restaurant.open_restaurant()

#we have now created three different restaurants, which is called instances, 
#since they are not the same restaurant but they all uses the same blueprint 
our_friends_restaurant = Resturant("canton", "tai foods")
our_friends_restaurant.describe_restaurant()
our_friends_restaurant.open_restaurant()