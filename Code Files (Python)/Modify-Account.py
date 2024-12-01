def modifyAccounts(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for items in oldlist :
            if items.accountNo == num:
                items.name = input("Enter the account holder name : ")
                items.type = input("Enter the account type : ")
                items.deposit = int(input("Enter the amount : "))
        outfile = open('newaccounts.data','wb')
        pickle.dump(oldlist,outfile)
        outfile.close()
        os.rename('newaccounts.data','accounts.data')