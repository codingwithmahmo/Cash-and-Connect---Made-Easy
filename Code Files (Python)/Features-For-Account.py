    def modifyAccounts(self):
        print("Account Number : ",self.accountNo)
        self.name = input("Modify Account Holder Name : ")
        self.deposit = int(input("Modify Balance : "))

    def getAccountsNo(self):
        return self.accountNo

    def getAccountsHolderName(self):
        return self.name

    def getAccountsType(self):
        return self.type