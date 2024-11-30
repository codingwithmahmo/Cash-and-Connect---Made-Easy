class Accounts:
    accountNo = 0
    name = ''
    deposit = 0
    type = ''

    def createAccounts(self):
        self.accountNo= int(input("Enter thr account no : "))
        self.name= input("Enter the account holder name : ")
        self.type= input("Enter the type of account [C/S] : ")
        self.deposit= int(input("Enter The Initial amount(>= 500 for Saving and >=1000 for current : "))
        print("\n\n\nAccount Created")

    def showAccounts(self):
        print("Account Number : ",self.accountNo)
        print("Account Holder Name : ",self.name)
        print("Type of Account :",self.type)
        print("Balance : ",self.deposit)