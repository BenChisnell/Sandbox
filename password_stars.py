""" Ask user for password and repeat if it doesn't meet minimum length set by a variable"""
password_length = "    "
user_password = input("Password: ")
while len(user_password) < len(password_length):
    print("Doesn't meet minimum length set")
    user_password = input("Password: ")

for i in range (len(user_password)):
    print("*", end="")