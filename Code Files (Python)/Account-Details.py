def writeAccountsFile(account):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')

    else:
        oldlist =[account]
        outfile = open('newaccounts.data','wb')
        pickle.dump(oldlist,outfile)
        outfile.close()
        os.rename('newaccounts.data','accounts.data')