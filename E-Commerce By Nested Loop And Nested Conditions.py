#e-commerce Management System

print("***********E-Commerce System***************")
customer=int(input("1.Login \n2.Sign Up \nSelect Any One :"))
if customer==1:
    username=input("Enter Your User Name:")
    password=input("Enter Your Password:")
    if password=="123" and username=="user":
        flag=True
        while flag:
            ask=int(input("Do You Want To Buy Clothes ?1-yes 2- no:"))
            if ask==1:
                option=int(input("You Have These Options :\n1- Casual \n2- Night Wear \n3- Party:"))
                if option==1:
                    casuals=["loan" , "kurti"]
                    print("These Are Casual Suits:")
                    for casual in casuals:
                        print(f"{casual}")
                elif option==2:
                    nightwears=["Comfortable shirt and trouser" , "silk night wear"]
                    print("These Are Night Wear Suits:")
                    for nightwear in nightwears:
                        print(f"{casual}")
                else:
                    parties=["Long Frock" , "Lehanga"]
                    print("These Are Party Wear Suits:")
                    for party in parties:
                        print(f"{casual}")
                checkout=int(input("Have You Check Out And Place The Order Successfully ?\n1-Yes \n2-No :"))
                if checkout ==1:
                    print("You Have Successfully Placed An Order.")
                    flag = False 
                else :
                    print("Order Has Not Confirmed Yet.")
            else:
                print("Thank You For Visiting Store.")
                flag=False
    else:
        print("Try Again")
else:
    name=input("Enter Your Name :")
    email=input("Enter Your email:")
    test=True
    while test:
        password=input("Enter Your Password:")
        confirm=input("Confirm Password:")
        if password==confirm:
            print("You Have Successfully Signed Up")
            test=False
        else:
            print("Match Your Password.")
    
