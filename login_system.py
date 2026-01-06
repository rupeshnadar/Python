correct_username = "rupesh"
correct_password = "python123"

username = input("Enter Username: ")
password = input("Enter Password: ")

if correct_username == username.lower() and correct_password == password:
    print("Login Successful")
else:
    print("Login Failed")
