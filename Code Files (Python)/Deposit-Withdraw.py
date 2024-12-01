

def depositAndWithdraw(num1,num2):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open("accounts.data","rb")
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for items in mylist:
            if items.accountNo == num1 :
                if num2 == 1:
                    amount = int(input("Enter the amount of deposit : "))
                    items.deposit += amount
                    print("Your account is updated")

                elif num2 == 2:
                    amount = int(input("Enter the amount to withdraw : "))
                    if amount <= items.deposit:
                        items.deposit -= amount
                    else :
                        print("You cannot withdraw larger amount")

    else:
        print("No records to Search")

    outfile = open('newaccounts.data','wb')
    pickle.dump(mylist,outfile)
    outfile.close()
    os.rename('newaccounts.data','accounts.data')
