#ATM Transaction System

print("********-----------------ATM Machine----------------*******")

balance=5000
users=1
pin=1234
while users<=2:
    print(f"User No# {users}")  
    user_pin=int(input("Enter Your PIN:"))
    
    if user_pin == pin:
        attempts=0
        while attempts <3:
            print(f"\n------ Main Menu (attempts {attempts +1})----")
            print("\n1.check Balance \n2. Withraw Money \n3. Deposit Money \n4. Mini Statement \n5. Exit")
            choice=int(input("Choose Option:"))
            
            #Nested-if-Else
            if choice==1:
                print(f"Your Current Balance {balance}")
                
            elif choice == 2:
                amount = int(input("Amount to Withdraw: "))
                
                # nested if in withdraw
                
                if amount <= balance:
                     balance -= amount
                     print(f"Withdrawn Amount {amount}")
                     print(f"Remaining Balance is  {balance}")                 
#                     if amount <=5000:
#                         balance -= amount
#                         print(f"Withdrawn Amount {amount}")
#                         print(f"Remaining Balance is  {balance}")
#                     else:
#                         print("Maximum Withdrawl limit is 5000!")
                else:
                    print("Insufficient balance!")
            elif choice==3:
                amount=int(input("Enter your amount to deposit:"))
                
                if amount>0:
                    if amount <=balance:
                        balance += amount
                        print(f"Deposited amount {amount}")
                        print(f"New Balance is {balance}")
                    else:
                        print("Maximum Deposit Limit i.e Rs{balance} is is Reached!")
                else:
                    print("Invalid Amount!")
                    
            elif choice==4:
                # Nested for loop - Mini Statement
                
                print("Mini Statement")
                transactions = ["Salary","Groceries","Bills","Savings"]
                amounts=[5000, -500, -1000, 2000]
                
                for i in range(len(transactions)):
                    print(f" {transactions[i]} :  Rs.{amounts[i]}")
                    
            elif choice ==5: #exit
                print("Thank you For Banking Us!")
                break
            
            else:
                print("Invalid Option!")
                
            attempts += 1
            if attempts >=3:
                print("Maximum Attempt Reached!")
#             else:
#                 print("We're Un-operational!")
    else:
        print("Wrong Pin!")
             
    users += 1
    
print("*********ATM is Shutting Down***********")