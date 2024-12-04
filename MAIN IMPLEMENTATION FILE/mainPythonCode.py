import pyttsx3
import sqlite3

class BankingSystem:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.db_connection = sqlite3.connect("banking_system.db")  # Connect to SQLite database
        self.cursor = self.db_connection.cursor()
        self.setup_database()

    def setup_database(self):
        """Initialize the database and populate it with admin credentials."""
        # Create adminDetails table
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS adminDetails (
            username TEXT PRIMARY KEY,
            password TEXT
        );
        """)
        # Insert admin credentials (if not already present)
        self.cursor.executemany("""
        INSERT OR IGNORE INTO adminDetails (username, password) VALUES (?, ?);
        """, [
            ('mahmood', 'khan'),
            ('mehboob', 'rasheed'),
            ('uzair', 'baig')
        ])
        self.db_connection.commit()

    def speak(self, text):
        """Voice output for the program."""
        self.engine.say(text)
        self.engine.runAndWait()

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
        print("Let us start with the program implementation now!")
        self.speak("Let us start with the program implementation now!")
        self.speak("Which operation would you like to initiate?")
        menu = ("\n1 - Admin Panel\n"
                "2 - Customer Panel\n"
                "3 - Exit System Panel")
        print(menu)
        print("Enter 1 for Admin Panel,\n 2 for Customer Panel,\n or 3 to Exit.")
        self.speak("Enter 1 for Admin Panel,\n 2 for Customer Panel,\n  or 3 to Exit.")
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

    def admin_login(self):
        """Handles admin login with SQL validation."""
        print("Welcome to the Admin Panel. Please provide your credentials.")
        self.speak("Welcome to the Admin Panel. Please provide your credentials.")
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")

        # Fetch credentials from the database
        self.cursor.execute("SELECT * FROM adminDetails WHERE username = ? AND password = ?", (username, password))
        result = self.cursor.fetchone()

        if result:
            print("Login successful. Welcome, Admin!")
            self.speak("Login successful. Welcome, Admin!")
        else:
            print("Access denied! Invalid credentials.")
            self.speak("Access denied! Invalid credentials.")

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
            if self.users.get(username) == password:
                print(f"Welcome back, {username}!")
                self.speak(f"Welcome back, {username}!")
            else:
                print("Invalid credentials. Access denied.")
                self.speak("Invalid credentials. Access denied.")
        elif is_existing == "no":
            print("Would you like to create an account? (yes/no)")
            self.speak("Would you like to create an account? Yes or No?")
            create_account = input("Enter your response (yes/no): ").strip().lower()
            if create_account == "yes":
                print("Let's create your account!")
                self.speak("Let's create your account!")
                username = input("Enter a username: ")
                password = input("Enter a password: ")
                self.users[username] = password
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
