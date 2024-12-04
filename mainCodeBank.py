import mysql.connector
import pyttsx3
import speech_recognition as sr
from getpass import getpass

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",  # Update with your MySQL password
    database="BankManagement"
)
cursor = db.cursor()

# Voice assistant
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Speech recognition
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"Recognized: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return None

# User authentication
def login():
    username = input("Enter Username: ")
    password = getpass("Enter Password: ")
    query = "SELECT id, role FROM Users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    if user:
        print("Login Successful!")
        return user  # (user_id, role)
    else:
        print("Invalid credentials. Try again.")
        return None

# Account management
def create_account():
    username = input("Enter Username: ")
    password = getpass("Enter Password: ")
    full_name = input("Enter Full Name: ")
    cnic = input("Enter CNIC: ")
    role = input("Role (customer/admin): ").lower()
    try:
        query = "INSERT INTO Users (username, password, full_name, cnic, role) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (username, password, full_name, cnic, role))
        db.commit()
        print("Account created successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def delete_account(user_id):
    query = "DELETE FROM Users WHERE id = %s"
    cursor.execute(query, (user_id,))
    db.commit()
    print("Account deleted successfully.")

# Funds management
def deposit_funds(user_id):
    amount = float(input("Enter deposit amount: "))
    query = "UPDATE Users SET account_balance = account_balance + %s WHERE id = %s"
    cursor.execute(query, (amount, user_id))
    db.commit()
    print("Funds deposited successfully.")

def withdraw_funds(user_id):
    amount = float(input("Enter withdrawal amount: "))
    query = "SELECT account_balance FROM Users WHERE id = %s"
    cursor.execute(query, (user_id,))
    balance = cursor.fetchone()[0]
    if amount > balance:
        print("Insufficient funds.")
    else:
        query = "UPDATE Users SET account_balance = account_balance - %s WHERE id = %s"
        cursor.execute(query, (amount, user_id))
        db.commit()
        print("Funds withdrawn successfully.")

# Voice assistance
def voice_assistant():
    speak("Welcome to the Bank Management System. How can I assist you?")
    command = listen()
    if "balance" in command:
        check_balance()

def check_balance(user_id):
    query = "SELECT account_balance FROM Users WHERE id = %s"
    cursor.execute(query, (user_id,))
    balance = cursor.fetchone()[0]
    print(f"Your current balance is {balance}")
    speak(f"Your current balance is {balance}")

# Admin functionalities
def admin_panel(user_id):
    while True:
        print("\nAdmin Panel Options:")
        print("1. View User Transactions")
        print("2. Approve/Decline Loans")
        print("3. Logout")
        choice = input("Enter choice: ")
        if choice == "1":
            view_transactions()
        elif choice == "2":
            manage_loans()
        elif choice == "3":
            break

def view_transactions():
    user_id = int(input("Enter User ID to view transactions: "))
    query = "SELECT * FROM Transactions WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    transactions = cursor.fetchall()
    for t in transactions:
        print(t)

def manage_loans():
    query = "SELECT * FROM Loans WHERE status = 'pending'"
    cursor.execute(query)
    loans = cursor.fetchall()
    for loan in loans:
        print(loan)
    loan_id = int(input("Enter Loan ID to approve/decline: "))
    decision = input("Approve (a) or Decline (d): ").lower()
    status = "approved" if decision == "a" else "declined"
    query = "UPDATE Loans SET status = %s WHERE id = %s"
    cursor.execute(query, (status, loan_id))
    db.commit()
    print(f"Loan {status} successfully.")

# Main program
def main():
    while True:
        print("\nWelcome to Bank Management System")
        print("1. Login")
        print("2. Create Account")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            user = login()
            if user:
                user_id, role = user
                if role == "admin":
                    admin_panel(user_id)
                else:
                    voice_assistant()
        elif choice == "2":
            create_account()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

