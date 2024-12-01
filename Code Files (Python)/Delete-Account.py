def deleteAccounts(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for items in oldlist:
            if items.accountNo != num:
                newlist.append(items)
        os.remove('accounts.data')
        outfile =open('newaccounts.data','wb')
        pickle.dump(newlist,outfile)
        outfile.close()
        os.rename('newaccounts.data','accounts.data')