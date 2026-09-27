accounts = []

while True:
        print("\n====Bank Management System====")
        print("1. Create Account")
        print("2. View Accounts")
        print("3. Search Account")
        print("4. Deposit Money")
        print("5. Withdraw Money")
        print("6. Check Balance")
        print("7. Delete Account")
        print("8. Exit")

        choice= input("Enter Your Choice: ")

        if choice == "1":
                user_name=input("Enter Your Name: ")
                account_number=int(input("Enter Your Account Number: "))
                account_balance=float(input("Enter Your Account Balance: "))
                account_password=int(input("Enter Your Account Password: "))

                account = {
                       "Name": user_name,
                       "Number":account_number,
                       "Balance":account_balance,
                       "Password":account_password
                }

                accounts.append (account)
                print("Account Created Successfully!")

        elif choice =="2":
                if len(accounts) == 0:
                        print("No Account Available")
                else:
                    print("\nAccounts List: ")   
                    for account in accounts:   
                            print("Name: ",account["Name"]),
                            print("Number: ",account["Number"]),
                            print("Balance: ",account["Balance"]),
                            print(".............................")

        elif choice == "3":
            search_account=int(input("Enter Account Number:"))  
            for account in accounts:
                    if account ["Number"] == search_account:
                        print("Name: ",account["Name"]),
                        print("Number: ",account["Number"]),
                        print("Balance: ",account["Balance"]),
                        print(".............................") 
                        break
            else:
                        print("Account Not Found!!") 

        elif choice == "4":
               search_account=int(input("Enter Your Account Number: "))
               deposit_money=float(input("Enter Your Amount: "))
               for account in accounts:
                      if account ["Number"] == search_account:
                        account["Balance"] += deposit_money
                        print("Amount Deposited Successfully!")
                        break
               else:
                      print("Account Not Found..")

        elif choice == "5":
               search_account=int(input("Enter Your Account Number: "))
               withdraw_money=float(input("Enter Your Amount: "))
               for account in accounts:
                     if account ["Number"] == search_account:
                            if account ["Balance"] >= withdraw_money:
                                   account["Balance"] -= withdraw_money
                                   print("Amount Withdrawn Successfully!")
                                   break
                            else:
                                   print("Insufficient Balance!")
                                   break
               else: 
                      print("Account Not Found!")

        elif choice == "6":
               search_account=int(input("Enter Your Account Number: "))
               for account in accounts:
                      if account["Number"] == search_account:
                        print("Current Balance:", account["Balance"])
                        break
               else: 
                      print("Account Not Found!")    

        elif choice == "7":
               search_account=int(input("Enter Your Account Number: "))
               for account in accounts:
                      if account["Number"] == search_account:
                             confirm=input("Are You Sure? Yes/No: ").lower()
                             if confirm == "yes":
                              accounts.remove(account)
                              print("Account Deleted Successfully!") 
                              break  
                             else:
                                    print("Deletion Cancelled!")
                                    break
               else:
                      print("Account Not Found!")

        elif choice == "8":
                        print("Program Closed.")
                        break
                                                      
                      
 