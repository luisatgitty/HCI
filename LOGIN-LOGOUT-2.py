class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.logged_in = False

    def login(self, username, password):
        if self.username == username and self.password == password:
            self.logged_in = True
            print("Logged in successfully!")
            self.prompt_logout()  # Prompt the user to log out after successful login
        else:
            print("Invalid username or password.")

    def logout(self):
        if self.logged_in:
            self.logged_in = False
            print("Logged out successfully!")
        else:
            print("You are not logged in.")

    def prompt_logout(self):
        logout_input = input("Do you want to log out? (yes/no): ")
        if logout_input.lower() == "yes":
            self.logout()

# Prompt the user for a username and password
username = input("Please enter your username: ")
password = input("Please enter your password: ")

# Create an account with the provided username and password
account = Account(username, password)

# Prompt the user for a username and password to login
login_username = input("Please enter your username to login: ")
login_password = input("Please enter your password to login: ")

# Try to login
account.login(login_username, login_password)
