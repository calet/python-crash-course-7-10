class User:
    def __init__(self, first_name, last_name, password, user_time):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.user_time = user_time
    def describe_user(self):
        username = f"{self.first_name} {self.last_name}"
        print(f"- username: {username}")
        print(f"- password: {self.password}")
        print(f"- online time (in days): {self.user_time}\n")
        
my_user = User("roto", "foto", "hello_world", 60)

user_2 = User("toto", "motto", "shrserg", 100)

user_3 = User("sotto", "ottoson", "hjsnca", 20)

user_4 = User("koto", "karlson", "knoafierf", 30)


users = [my_user, user_2, user_3, user_4]

print("users:")
print("-----------------")
for the_user in users:
    the_user.describe_user()
