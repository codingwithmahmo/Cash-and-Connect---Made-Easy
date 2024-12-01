def writeAccounts():
    account = Accounts()
    account.createAccounts()
    writeAccountsFile(account)

def displayAll():
        file = pathlib.Path("accounts.data")
        if file.exists():
            infile = open('accounts.data','rb')
            mylists =pickle.load(infile)
            for items in mylists :
                print(items.accountNo," ",items.name," ",items.type," ",items.deposit )
            infile.close()

        else:
            print("No records to display")

def displayssp(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open("accounts.data", "rb")
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for items in mylist:
            if items.accountNo == num:
                print("Your Account Balance is = ",items.deposit)
                found = True
    else:
        print("No records to search")
    if not found:
        print("No existing record with this number")