# Problem: Check if a string starts with a specific prefix. And Keep taking input until the input is correct

# taking input from user to check prefix
def main():
    while True:

        user_input = input("Enter you name with prefix Mr/Miss/Ms: ") # Taking input from the user
        prefix = ("Mr", "Miss", "Ms") # tuple of prefix to check
        if user_input.startswith(prefix):
            break # break the loop if the inpte is correct
        print("Invalide Input. Please try again.")
    print(f"Valide Input. Your Name: {user_input}") # Output


#crating a function to check that the prefix is present or not
def start_with_prefix(string, prefix):
    prefix = string.startswith(prefix)
    return prefix


main()


