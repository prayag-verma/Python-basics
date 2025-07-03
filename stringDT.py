user = input("Enter your name: ")
def greet_user(name):
    """Function to greet the user with their name."""
    return (f"Hello, {name}! Welcome to the program.")

print(greet_user(user))

# Example 2 --> Printing length of a string

name = "Prayag Verma"

print(f"The length of the string '{name}' is {len(name)} characters.")
