login = []

while True:
     print("\n==== Login System ===="),
     print("1. Register"),
     print("2. Login"),
     print("3. View All Users")
     print("4. Change Password")
     print("5. Delete User Account")
     print("6. Exit")

     choice = input("Enter Your Choice: ")

     if choice == "1":
          user_name=input("Enter Your Name: ")
          password=input("Enter Your Password: ")

          with open("users.txt", "a") as file:
           file.write(f"{user_name},{password}\n")

          print("Registration Successful!")

     elif choice == "2":
         user_name=input("Enter User Name: ")
         password=input("Enter Your Password: ")

         with open("users.txt","r") as file:
             users = file.readlines()
             for user in users:
                 saved_username,saved_password=user.split(",")
                 if user_name == saved_username and password == saved_password.strip():
                    
                         print("Login Successful!")
                         break
             else:
                 print("Invalid Username or Password!")

     elif choice == "3":
           with open("users.txt" , "r") as file:
                users = file.readlines()
                for user in users:
                     saved_username,saved_password=user.split(",")
                     print("-----------------------------")
                     print(f"Username: {saved_username}")
                     print(f"Password: {saved_password.strip()}")
     elif choice == "4":
          user_name=input("Enter Your Name: ")
          password=input("Enter your old password: ")
          new_password=input("Enter your new password: ")

          with open("users.txt", "r")as file:
               users = file.readlines()
          found=False
          updated_users = []

          for user in users:
                 saved_username, saved_password = user.split(",")
                 if user_name == saved_username and password == saved_password.strip():
                        found=True
                        updated_users.append(f"{saved_username},{new_password}\n")
                 else:
                      updated_users.append(user)
          with open("users.txt","w")as file:
                    file.writelines(updated_users)

                    
          if found:
                print("Password Changed Successfully!")
          else:
                print("Invalid Username or Password!")

     elif choice == "5":
           user_name=input("Enter your Name: ")
           password=input("Enter your Password: ")
           with open("users.txt","r")as file:
                 users=file.readlines()
                 found=False
                 deleted_users=[]

                 for user in users:
                    saved_username,saved_password=user.split(",")
                    if user_name == saved_username and password == saved_password.strip():
                         found=True
                         confirm=input("Are you sure you want to delete your account? (yes/no):").lower()
                         if confirm == "yes":
                              print("Account Deleted Successfully!")
                              break
                         else:
                            deleted_users.append(user)
                            print("Account Deletion Cancelled.")
                            break
                    else:
                          deleted_users.append(user)
                    
           with open("users.txt","w")as file:
                file.writelines(deleted_users)
                
           if not found:
                print("Invalid Username or Password!")

     elif choice == "6":
          print("Exiting the program...")
          break
     else:
         print("Invalid Choice! Please Try Again.")
         break