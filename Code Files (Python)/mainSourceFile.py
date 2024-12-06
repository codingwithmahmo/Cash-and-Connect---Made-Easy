import pickle
import os
import pathlib
import speech_recognition as sr
import pyttsx3


class Account:
    accNo = 0
    name = ''
    deposit = 0
    type = ''

    def createAccount(self):
        speak("Enter the account number")
        self.accNo = self.listen_input()
        speak("Enter the account holder name")
        self.name = self.listen_input()
        speak("Enter the type of account, C for Current or S for Saving")
        self.type = self.listen_input()
        speak("Enter the initial amount (minimum 500 for Savings and 1000 for Current)")
        self.deposit = self.listen_input_as_int()
        speak("Congrats! New Account Created")

    def showAccount(self):
        speak(f"Account Number: {self.accNo}")
        speak(f"Account Holder Name: {self.name}")
        speak(f"Type of Account: {self.type}")
        speak(f"Balance: {self.deposit}")

    def modifyAccount(self):
        speak(f"Account Number: {self.accNo}")
        speak("Modify Account Holder Name")
        self.name = self.listen_input()
        speak("Modify type of Account")
        self.type = self.listen_input()
        speak("Modify Balance")
        self.deposit = self.listen_input_as_int()

    def depositAmount(self, amount):
        self.deposit += amount

    def withdrawAmount(self, amount):
        if amount <= self.deposit:
            self.deposit -= amount
        else:
            speak("Insufficient funds")

    def report(self):
        print(self.accNo, self.name, self.type, self.deposit)

    def getAccountNo(self):
        return self.accNo

    def getAcccountHolderName(self):
        return self.name

    def getAccountType(self):
        return self.type

    def getDeposit(self):
        return self.deposit

    def listen_input(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        try:
            return r.recognize_google(audio)
        except sr.UnknownValueError:
            speak("Sorry, I could not understand that.")
            return self.listen_input()
        except sr.RequestError:
            speak("Sorry, there was an error with the speech service.")
            return self.listen_input()

    def listen_input_as_int(self):
        try:
            return int(self.listen_input())
        except ValueError:
            speak("Invalid number, please try again.")
            return self.listen_input_as_int()


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def intro():
    speak("Welcome to the Bank Management System developed by Jai Gora")
    input()


def writeAccount():
    account = Account()
    account.createAccount()
    writeAccountsFile(account)


def displayAll():
    file = pathlib.Path("accounts.data")
    if file.exists():
        try:
            with open('accounts.data', 'rb') as infile:
                mylist = pickle.load(infile)
                for item in mylist:
                    print(item.accNo, item.name, item.type, item.deposit)
        except Exception as e:
            speak(f"An error occurred: {e}")
    else:
        speak("No records to display")


def displaySp(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        try:
            with open('accounts.data', 'rb') as infile:
                mylist = pickle.load(infile)
            found = False
            for item in mylist:
                if item.accNo == num:
                    speak(f"Your account balance is {item.deposit}")
                    found = True
            if not found:
                speak("No existing record with this number")
        except Exception as e:
            speak(f"An error occurred: {e}")
    else:
        speak("No records to search")


def depositAndWithdraw(num1, num2):
    file = pathlib.Path("accounts.data")
    if file.exists():
        try:
            with open('accounts.data', 'rb') as infile:
                mylist = pickle.load(infile)
            os.remove('accounts.data')
            for item in mylist:
                if item.accNo == num1:
                    if num2 == 1:
                        speak("Enter the amount to deposit")
                        amount = int(input())
                        item.deposit += amount
                        speak("Your account is updated")
                    elif num2 == 2:
                        speak("Enter the amount to withdraw")
                        amount = int(input())
                        item.withdrawAmount(amount)
        except Exception as e:
            speak(f"An error occurred: {e}")
    else:
        speak("No records to search")
    try:
        with open('newaccounts.data', 'wb') as outfile:
            pickle.dump(mylist, outfile)
        os.rename('newaccounts.data', 'accounts.data')
    except Exception as e:
        speak(f"An error occurred while saving the file: {e}")


def deleteAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        try:
            with open('accounts.data', 'rb') as infile:
                oldlist = pickle.load(infile)
            newlist = [item for item in oldlist if item.accNo != num]
            os.remove('accounts.data')
            with open('newaccounts.data', 'wb') as outfile:
                pickle.dump(newlist, outfile)
            os.rename('newaccounts.data', 'accounts.data')
            speak("Account deleted successfully")
        except Exception as e:
            speak(f"An error occurred: {e}")
    else:
        speak("No records to delete")


def modifyAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        try:
            with open('accounts.data', 'rb') as infile:
                oldlist = pickle.load(infile)
            os.remove('accounts.data')
            for item in oldlist:
                if item.accNo == num:
                    item.name = input("Enter the Account Holder Name: ")
                    item.type = input("Enter the Account Type (C/S): ")
                    item.deposit = int(input("Enter the Amount: "))
            with open('newaccounts.data', 'wb') as outfile:
                pickle.dump(oldlist, outfile)
            os.rename('newaccounts.data', 'accounts.data')
            speak("Account modified successfully")
        except Exception as e:
            speak(f"An error occurred: {e}")
    else:
        speak("No records to modify")


def writeAccountsFile(account):
    file = pathlib.Path("accounts.data")
    if file.exists():
        try:
            with open('accounts.data', 'rb') as infile:
                oldlist = pickle.load(infile)
            oldlist.append(account)
            os.remove('accounts.data')
        except Exception as e:
            speak(f"An error occurred: {e}")
            return
    else:
        oldlist = [account]
    try:
        with open('newaccounts.data', 'wb') as outfile:
            pickle.dump(oldlist, outfile)
        os.rename('newaccounts.data', 'accounts.data')
    except Exception as e:
        speak(f"An error occurred while saving the file: {e}")


# Main
ch = ''
num = 0
intro()

while ch != '8':
    speak("\tMAIN MENU")
    speak("\t1. New Account")
    speak("\t2. Deposit Amount")
    speak("\t3. Withdraw Amount")
    speak("\t4. Balance Enquiry")
    speak("\t5. All Account Holder List")
    speak("\t6. Close an Existing Account")
    speak("\t7. Modify Information of any Account")
    speak("\t8. Exit")
    speak("Select Your Option from 1 to 8")
    ch = input()
    if ch == '1':
        writeAccount()
    elif ch == '2':
        speak("Enter the account number")
        num = int(input())
        depositAndWithdraw(num, 1)
    elif ch == '3':
        speak("Enter the account number")
        num = int(input())
        depositAndWithdraw(num, 2)
    elif ch == '4':
        speak("Enter the account number")
        num = int(input())
        displaySp(num)
    elif ch == '5':
        displayAll()
    elif ch == '6':
        speak("Enter the account number")
        num = int(input())
        deleteAccount(num)
    elif ch == '7':
        speak("Enter the account number")
        num = int(input())
        modifyAccount(num)
    elif ch == '8':
        speak("Thanks for using the bank management system")
        break
    else:
        speak("Invalid choice, please select a valid option")

    input("Press <ENTER>")
