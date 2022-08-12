class User:
    def __init__(self, first_name, last_name, password, user_time=None, admin=False):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.user_time = user_time
        self.admin = admin

    def describe_user(self):
        username = f"{self.first_name} {self.last_name}"
        print(f"- admin: {self.admin}")
        print(f"- username: {username}")
        print(f"- password: {self.password}")
        print(f"- online time (in days): {self.user_time}\n")

class Admin(User):
    def __init__(self, first_name, last_name, password, user_time=None, admin=True):
        super().__init__(first_name, last_name, password, user_time, admin)
        self.privileges = ["can add post", "can delete post", "ban users", "give privileges", "remove privileges"]
        
    
    def showPrivileges(self):
        print("privileges:")
        for priv in self.privileges:
            print(f"- {priv}")
        print("----------------------")

admin = User("roto", "foto", "hello_world")

user_2 = User("toto", "motto", "shrserg", 100)

user_3 = User("sotto", "ottoson", "hjsnca", 20)

user_4 = User("koto", "karlson", "knoafierf", 30)


users = [admin, user_2, user_3, user_4]

print("users:")
print("-----------------")
for the_user in users:
    the_user.describe_user()
    if the_user == admin:
        admin.showPrivileges()
        print()
