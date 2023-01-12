sweets=int(input("how meny sweet do u have"))
people=int(input("how many people do the sweet need to be split between"))
how_many_each=sweets // people
left_over=sweets % people
print("each person will get ", how_many_each, "sweet with", left_over, "sweets left over,")

# Set
username = "Moses"
password = "Password"


# Get
user_username = input("Username: ")
user_password = input("Password: ")

# Check
if user_username == username and user_password == password:
    print("Welcome")
elif user_username == username and user_password != password:
    print("Password is wrong")
elif user_username != username and user_password == password:
    print("Username is wrong")
