print("\tMAIN MANU")
print("\t1. NEW ACCOUNT")
print("\t2. DEPOSIT AMOUNT")
print("\t3. WITHDRAW AMOUNT")
print("\t4. BALANCE ENQUIRY")
print("\t5. ALL ACCOUNT HOLDER LIST")
print("\t6. CLOSE AN ACCOUNT")
print("\t7. MODIFY AN ACCOUNT")
print("\t8. EXIT")
print("\tSelect Your Option [1-8]")



while ch !=8:
    ch = input("Enter your choice :")
    if ch == '1':
        writeAccounts()
    elif ch == '2':
        num = int(input("\tEnter The Account No. : "))
        depositAndWithdraw(num,1)
    elif ch == '3':
        num = int(input("\tEnter The Account No. : "))
        depositAndWithdraw(num,2)
    elif ch == '4':
        num = int(input("\tEnter The Account No. : "))
        displayssp(num)
    elif ch == '6':
        num = int(input("\tEnter The Account No. : "))
        deleteAccounts(num)
    elif ch == '5':
        displayAll()
    elif ch == '7':
        num = int(input("\tEnter The Account No. : "))
        modifyAccounts(num)
    elif ch == '8':
        print("\tThanks for using Bank Management System")
        break
    else:
        print("Invalid Choice")