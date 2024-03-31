stored_email = "habeyrolls01@gmail.com"
stored_password = "123abc"
print("Welcome to our login page")
entered_email = input("Enter your email: ")
entered_password = input("enter your password: ")
if stored_email == entered_email and stored_password == entered_password:
    print("logged in")
else:
    print("You can't login")
    
