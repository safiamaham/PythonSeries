# while True:
#     user_id=input("Enter Your User Id:").lower()
#     password=input("Enter Your Password:").lower()
#     if (user_id=="124" or user_id=="1234" or user_id=="000") and (password=="abcd"):
#         print("Welcome to the system.")
#         
#         break
#     else:
#         print("This is a wrong password or user name.")
#         rerun=input("Do You want to Try again?").lower()
#         if rerun=="no":
#             break
#         else:
#             print("OK!")
#             continue


control=True
while control:
    card=int(input("Enter Your Card :\n1.Card Inserted \n2.Card Error :"))
    if card==1:
        chance=3
        while chance>=0:
            pin=int(input("Enter Your Pin:"))
            if pin==1234:
                print("Welcome To The ATM.")
                balance=50000
                select=input("Select Any Option :\n1. Fast Cash\n2. Cash Withdrawl \n3. Balance Inquiry \n4. Type Anything For Exit   :")
                if select=="1":
                    print(f"Proceeding To Fast Cash, Have Your Total Amount {balance}.")
                elif select=="2":
                    print("Proceeding To Cash Withdrawl.")
                elif select=="3":
                    print("Proceeding To Balance Inquiry {balance}.")
                else:
                    print("Proceeding To Exit.")
                control=False
                break
            else:
                print(f"You Have {chance} Chances Left!")
                chance=chance-1
                continue
        else:
            print("Card Has Been Captured.")
            break
    else:
        print("Card Error.")
        rerun=int(input("Do You Want To Insert Card Again? \n1. Yes \n2. No :"))
        if rerun==1:
            continue 
        else:
            print("Thank You For Visiting.")
            break 
