import pyttsx3
import sqlite3

class BankingSystem:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.connection = sqlite3.connect("banking_system.db")  # Connect to the SQLite database
        self.create_admin_table()  # Ensure the admin table exists

    def speak(self, text):
        """Voice output for the program."""
        self.engine.say(text)
        self.engine.runAndWait()

    def create_admin_table(self):
        """Creates the AdminCredentials table if it doesn't exist and populates it."""
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS AdminCredentials (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL
            );
            """)
            # Insert example data only if the table is empty
            cursor.execute("SELECT COUNT(*) FROM AdminCredentials")
            if cursor.fetchone()[0] == 0:
                cursor.executemany(
                    "INSERT INTO AdminCredentials (username, password) VALUES (?, ?)",
                    [('mahmood', 'khan'), ('uzair', 'baig'), ('mehboob', 'rasheed')]
                )
                self.connection.commit()

    def fetch_admin_credentials(self):
        """Fetch admin credentials from the database."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT username, password FROM AdminCredentials")
        return dict(cursor.fetchall())

    def welcome_message(self):
        """Displays and speaks the welcome message."""
        welcome_message = "Welcome to Cash and Connect - Made Easy!"
        print("\t*********************************************")
        print(f"\t   {welcome_message}    ")
        print("\t*********************************************")
        self.speak(welcome_message)

    def greeting_message(self):
        """Displays and speaks the greeting message."""
        calvin_message = "Let me introduce myself! I am Calvin, your voice assistant for today! Buckle up and embrace this banking journey!"
        happiness_message = "Esteemed Customer! I am glad you are here today! Thanks for lighting my day!"
        print(calvin_message)
        self.speak(calvin_message)
        print(happiness_message)
        self.speak(happiness_message)

    def get_user_choice(self):
        """Prompts the user to choose an operation."""
        print("Which operation would you like to initiate today?")
        self.speak("Dear Customer. Which operation would you like to initiate today?")
        menu = ("\n1 - Admin Panel\n"
                "2 - Customer Panel\n"
                "3 - Exit System Panel")
        print(menu)
        self.speak("Enter 1 for Admin Panel, 2 for Customer Panel, or 3 to Exit.")
        print()
        while True:
            try:
                choice = int(input("\nEnter your choice (1/2/3): "))
                if choice in [1, 2, 3]:
                    return choice
                else:
                    raise ValueError
            except ValueError:
                print("Invalid input. Please enter 1, 2, or 3.")
                self.speak("Invalid input. Please enter 1, 2, or 3.")

    def admin_panel_menu(self):
        """Displays the admin panel menu in a formatted and visually pleasing way."""
        menu_options = [
            "1 - Edit Account",
            "2 - Create Account",
            "3 - Restrict Account",
            "4 - Delete Account",
            "5 - View Transaction History",
            "6 - Authorize Large Transactions",
            "7 - Increase Account Limits",
            "8 - Remove Staff Members",
            "9 - Approve Loans",
            "0 - Logout"
        ]

        print("\n" + "*" * 50)
        print(f"{'Admin Panel':^50}")
        print("*" * 50)
        for option in menu_options:
            print(f"* {option:<46}*")
        print("*" * 50)

    def handle_admin_panel(self):
        """Handles admin panel operations."""
        while True:
            self.admin_panel_menu()
            self.speak("Please choose an option from the admin panel.")
            try:
                choice = int(input("Enter your choice (0 to logout): "))
                if choice == 0:
                    print("Logging out from Admin Panel.")
                    self.speak("Logging out from Admin Panel.")
                    break
                elif choice == 1:
                    print("You selected 'Edit Account'.")
                    self.speak("You selected Edit Account.")
                    # Add functionality for editing account
                elif choice == 2:
                    print("You selected 'Create Account'.")
                    self.speak("You selected Create Account.")
                    # Add functionality for creating account
                elif choice == 3:
                    print("You selected 'Restrict Account'.")
                    self.speak("You selected Restrict Account.")
                    # Add functionality for restricting account
                elif choice == 4:
                    print("You selected 'Delete Account'.")
                    self.speak("You selected Delete Account.")
                    # Add functionality for deleting account
                elif choice == 5:
                    print("You selected 'View Transaction History'.")
                    self.speak("You selected View Transaction History.")
                    # Add functionality for viewing transaction history
                elif choice == 6:
                    print("You selected 'Authorize Large Transactions'.")
                    self.speak("You selected Authorize Large Transactions.")
                    # Add functionality for authorizing large transactions
                elif choice == 7:
                    print("You selected 'Increase Account Limits'.")
                    self.speak("You selected Increase Account Limits.")
                    # Add functionality for increasing account limits
                elif choice == 8:
                    print("You selected 'Remove Staff Members'.")
                    self.speak("You selected Remove Staff Members.")
                    # Add functionality for removing staff members
                elif choice == 9:
                    print("You selected 'Approve Loans'.")
                    self.speak("You selected Approve Loans.")
                    # Add functionality for approving loans
                else:
                    print("Invalid choice. Please choose a valid option.")
                    self.speak("Invalid choice. Please choose a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")
                self.speak("Invalid input. Please enter a number.")

    # Update the admin_login method to call handle_admin_panel
    def admin_login(self):
        """Handles admin login with 3 attempts."""
        print("Welcome to the Admin Panel. Please provide your credentials.")
        self.speak("Welcome to the Admin Panel. Please provide your credentials.")
        admin_credentials = self.fetch_admin_credentials()  # Fetch credentials from the database
        attempts = 3

        while attempts > 0:
            username = input("Enter admin username: ").lower()
            password = input("Enter admin password: ")  # No masking applied here
            if admin_credentials.get(username) == password:
                print("Login successful. Welcome, Admin!")
                self.speak("Login successful. Welcome, Admin!")
                self.handle_admin_panel()  # Call the admin panel handler after successful login
                return  # Exit the login function on success
            else:
                attempts -= 1
                print(f"Invalid credentials. {attempts} attempts remaining.")
                self.speak(f"Invalid credentials. {attempts} attempts remaining.")

        print("Attempted tries have been exceeded. Returning to the main menu.")
        self.speak("Attempted tries have been exceeded. Returning to the main menu.")

    def customer_panel(self):
        """Handles customer panel operations."""
        print("Welcome to the Customer Panel!")
        self.speak("Welcome to the Customer Panel!")
        print("Are you an existing user? (yes/no)")
        self.speak("Are you an existing user? Yes or No?")
        is_existing = input("Enter your response (yes/no): ").strip().lower()
        if is_existing == "yes":
            print("Please provide your credentials.")
            self.speak("Please provide your credentials.")
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            print(f"Welcome back, {username}!")
            self.speak(f"Welcome back, {username}!")
        elif is_existing == "no":
            print("Would you like to create an account? (yes/no)")
            self.speak("Would you like to create an account? Yes or No?")
            create_account = input("Enter your response (yes/no): ").strip().lower()
            if create_account == "yes":
                print("Let's create your account!")
                self.speak("Let's create your account!")
                username = input("Enter a username: ")
                password = input("Enter a password: ")
                print(f"Account created successfully! Welcome, {username}!")
                self.speak(f"Account created successfully! Welcome, {username}!")
            else:
                print("Thank you for visiting. Goodbye!")
                self.speak("Thank you for visiting. Goodbye!")
        else:
            print("Invalid response. Exiting.")
            self.speak("Invalid response. Exiting.")

    def main(self):
        """Main driver function."""
        self.welcome_message()
        self.greeting_message()
        while True:
            choice = self.get_user_choice()
            if choice == 1:
                self.admin_login()
            elif choice == 2:
                self.customer_panel()
            elif choice == 3:
                print("Exiting the system. Thank you for using Cash and Connect!")
                self.speak("Exiting the system. Thank you for using Cash and Connect!")
                break

if __name__ == "__main__":
    banking_system = BankingSystem()
    banking_system.main()
