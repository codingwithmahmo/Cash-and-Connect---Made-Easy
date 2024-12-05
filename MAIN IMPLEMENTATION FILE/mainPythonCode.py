import pickle
import os
import tkinter as tk
from tkinter import messagebox

class Account:
    def __init__(self):
        self.accNo = 0
        self.name = ''
        self.deposit = 0
        self.type = ''

    def createAccount(self):
        self.accNo = int(entry_acc_no.get())
        self.name = entry_name.get()
        self.type = entry_type.get()
        self.deposit = int(entry_initial_amount.get())
        accounts_list.append(self)
        write_accounts_file()
        messagebox.showinfo("Success", "Account created successfully.")

    def depositAmount(self):
        acc_no = int(entry_acc_no.get())
        amount = int(entry_amount.get())
        for account in accounts_list:
            if account.accNo == acc_no:
                account.deposit += amount
                write_accounts_file()
                messagebox.showinfo("Success", f"Deposited {amount} into Account {acc_no}.")
                break

    def withdrawAmount(self):
        acc_no = int(entry_acc_no.get())
        amount = int(entry_amount.get())
        for account in accounts_list:
            if account.accNo == acc_no:
                if account.deposit >= amount:
                    account.deposit -= amount
                    write_accounts_file()
                    messagebox.showinfo("Success", f"Withdrew {amount} from Account {acc_no}.")
                else:
                    messagebox.showerror("Error", "Insufficient balance.")
                break

    def balanceEnquiry(self):
        acc_no = int(entry_acc_no.get())
        for account in accounts_list:
            if account.accNo == acc_no:
                messagebox.showinfo("Balance Enquiry", f"Account Balance for Account {acc_no}: {account.deposit}")
                break

    def displayAll(self):
        all_accounts = ""
        for account in accounts_list:
            all_accounts += f"Account Number: {account.accNo}, Account Holder Name: {account.name}, Type of Account: {account.type}, Balance: {account.deposit}\n"
        messagebox.showinfo("All Account Holders", all_accounts)

    def deleteAccount(self):
        acc_no = int(entry_acc_no.get())
        for account in accounts_list:
            if account.accNo == acc_no:
                accounts_list.remove(account)
                write_accounts_file()
                messagebox.showinfo("Success", f"Closed Account {acc_no}.")
                break

    def modifyAccount(self):
        acc_no = int(entry_acc_no.get())
        for account in accounts_list:
            if account.accNo == acc_no:
                account.name = entry_name.get()
                account.type = entry_type.get()
                account.deposit = int(entry_amount.get())
                write_accounts_file()
                messagebox.showinfo("Success", f"Modified Account {acc_no}.")
                break

def write_accounts_file():
    with open('accounts.data', 'wb') as file:
        pickle.dump(accounts_list, file)

def read_accounts_file():
    if os.path.exists('accounts.data'):
        with open('accounts.data', 'rb') as file:
            accounts_list = pickle.load(file)
    else:
        accounts_list = []
    return accounts_list

accounts_list = read_accounts_file()

root = tk.Tk()
root.title("Bank Management System")

frame = tk.Frame(root)
frame.pack()

# Create and configure GUI elements (labels, buttons, entry widgets, etc.) here.
label_acc_no = tk.Label(frame, text="Account No:")
label_name = tk.Label(frame, text="Account Holder Name:")
label_type = tk.Label(frame, text="Type of Account:")
label_initial_amount = tk.Label(frame, text="Initial Amount:")
label_amount = tk.Label(frame, text="Amount:")

entry_acc_no = tk.Entry(frame)
entry_name = tk.Entry(frame)
entry_type = tk.Entry(frame)
entry_initial_amount = tk.Entry(frame)
entry_amount = tk.Entry(frame)

button_create_account = tk.Button(frame, text="Create Account", command=Account().createAccount)
button_deposit = tk.Button(frame, text="Deposit", command=Account().depositAmount)
button_withdraw = tk.Button(frame, text="Withdraw", command=Account().withdrawAmount)
button_balance_enquiry = tk.Button(frame, text="Balance Enquiry", command=Account().balanceEnquiry)
button_all_account_holders = tk.Button(frame, text="All Account Holders", command=Account().displayAll)
button_close_account = tk.Button(frame, text="Close Account", command=Account().deleteAccount)
button_modify_account = tk.Button(frame, text="Modify Account", command=Account().modifyAccount)
button_exit = tk.Button(frame, text="Exit", command=exit)

# Layout the GUI elements using grid
label_acc_no.grid(row=0, column=0)
label_name.grid(row=1, column=0)
label_type.grid(row=2, column=0)
label_initial_amount.grid(row=3, column=0)
label_amount.grid(row=4, column=0)

entry_acc_no.grid(row=0, column=1)
entry_name.grid(row=1, column=1)
entry_type.grid(row=2, column=1)
entry_initial_amount.grid(row=3, column=1)
entry_amount.grid(row=4, column=1)

button_create_account.grid(row=5, column=0)
button_deposit.grid(row=5, column=1)
button_withdraw.grid(row=6, column=0)
button_balance_enquiry.grid(row=6, column=1)
button_all_account_holders.grid(row=7, column=0)
button_close_account.grid(row=7, column=1)
button_modify_account.grid(row=8, column=0)
button_exit.grid(row=8, column=1)
root.mainloop()