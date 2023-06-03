# validate user input exerxcise
# 1. Username is no more than 12 characters
# 2. Username must not contain spaces
# 3. Username must not contain digits

# Take input from user
username = input("Enter a Username: ")
# validate 1st condition
if len(username)>12:
    print("Username is no more than 12 characters")
# validate 2nd condition
elif username.find(" ") >= 0:
    print("Username must not contain spaces")
# validate 3rd condition
elif username.isalpha() is False:
    print("Username must not contain digits")
# if the username is valide give the output
else:
    print("Welcome,", username)