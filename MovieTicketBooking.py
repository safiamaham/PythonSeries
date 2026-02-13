print("*******************Movie Ticket System************************")
select=int(input("Which Type Of Movie You Want ? \n1. 2D \n2. 3D \n3. IMAX(Type Anything) \nSelect Any Of Above:"))
if select==1:
    print("***Welcome To The 2D Movie Section*** ")
    timing=int(input("Select Time:\n1. Morning \n2. Afternoon \n3. Evening \n4. Night(Type Any Thing)\n Select Any Of Above:"))
    if timing == 1:
        print("You have selected morning")
        seat=int(input("Which Seat You Want :\n1. Standard \n2. Premium \n3. VIP(Type Anything) \nSelect Any Of Above:"))
        if seat == 1:
            print("You Have Selected Standard Sitting. ")
            days=int(input("Enter Dasy:\n1. Holidays \n2. Weekends \nSelect Any Of Above:"))
            if days==1:
                print("You Are Coming In Holiday")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 3000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Morning with Standard Sitting in Holiday Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 12000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Morning with Standard Sitting in Holiday with Group.\n Bill Is :{budget} and with 10% Tax Is {tax} Final Bill Is {budget+tax}. ")      
            else:
                print("You Are Coming In Weekends")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 5000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Morning with Standard Sitting in Weekend Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}.Final Bill Is {budget+tax} ")
                else:
                    budget= 20000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Morning with Standard Sitting in Weekend with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}.Final Bill Is {budget+tax} ")      

        elif seat==2:
            print("You Have Selected Premium Sitting. ")
            days=int(input("Enter Dasy:\n1. Holidays \n2. Weekends \nSelect Any Of Above:"))
            if days==1:
                print("You Are Coming In Holiday")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 6000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Morning with Premium Sitting in Holiday Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}.Final Bill Is {budget+tax} ")
                else:
                    budget= 24000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Morning with Premium Sitting in Holiday with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. Final Bill Is {budget+tax}")      
            else:
                print("You Are Coming In Weekends")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 10000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Morning with Premium Sitting in Weekend Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}.Final Bill Is {budget+tax} ")
                else:
                    budget= 40000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Morning with Premium Sitting in Weekend with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. Final Bill Is {budget+tax}")      
        else:
            print("You Have Selected VIP Sitting. ")
            days=int(input("Enter Dasy:\n1. Holidays \n2. Weekends \nSelect Any Of Above:"))
            if days==1:
                print("You Are Coming In Holiday")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 12000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Morning with VIP Sitting in Holiday Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 60000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Morning with VIP Sitting in Holiday with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
            else:
                print("You Are Coming In Weekends")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 15000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Morning with Standard Sitting in Weekend Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 70000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Morning with Standard Sitting in Weekend with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      

        
    elif timing ==2:
        print("You have selected Afternoon")
        seat=int(input("Which Seat You Want :\n1. Standard \n2. Premium \n3. VIP(Type Anything) \nSelect Any Of Above:"))
        if seat == 1:
            print("You Have Selected Standard Sitting. ")
            days=int(input("Enter Dasy:\n1. Holidays \n2. Weekends \nSelect Any Of Above:"))
            if days==1:
                print("You Are Coming In Holiday")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 3000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Afternoon with Standard Sitting in Holiday Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 12000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Afternoon with Standard Sitting in Holiday with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
            else:
                print("You Are Coming In Weekends")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 5000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Afternoon with Standard Sitting in Weekend Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 20000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Afternoon with Standard Sitting in Weekend with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      

        elif seat==2:
            print("You Have Selected Premium Sitting. ")
            days=int(input("Enter Dasy:\n1. Holidays \n2. Weekends \nSelect Any Of Above:"))
            if days==1:
                print("You Are Coming In Holiday")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 6000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Afternoon with Premium Sitting in Holiday Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 24000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Afternoon with Premium Sitting in Holiday with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
            else:
                print("You Are Coming In Weekends")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 10000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Afternoon with Premium Sitting in Weekend Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 40000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Afternoon with Premium Sitting in Weekend with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
        else:
            print("You Have Selected VIP Sitting. ")
            days=int(input("Enter Dasy:\n1. Holidays \n2. Weekends \nSelect Any Of Above:"))
            if days==1:
                print("You Are Coming In Holiday")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 12000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Afternoon with VIP Sitting in Holiday Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 60000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Afternoon with VIP Sitting in Holiday with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
            else:
                print("You Are Coming In Weekends")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 15000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Afternoon with Standard Sitting in Weekend Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 70000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Afternoon with Standard Sitting in Weekend with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      

    elif timing ==3:
        print("You have selected Evening")
        seat=int(input("Which Seat You Want :\n1. Standard \n2. Premium \n3. VIP(Type Anything) \nSelect Any Of Above:"))
        if seat == 1:
            print("You Have Selected Standard Sitting. ")
            days=int(input("Enter Dasy:\n1. Holidays \n2. Weekends \nSelect Any Of Above:"))
            if days==1:
                print("You Are Coming In Holiday")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 3000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Evening with Standard Sitting in Holiday Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 12000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Evening with Standard Sitting in Holiday with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
            else:
                print("You Are Coming In Weekends")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 5000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Evening with Standard Sitting in Weekend Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 20000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Evening with Standard Sitting in Weekend with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      

        elif seat==2:
            print("You Have Selected Premium Sitting. ")
            days=int(input("Enter Dasy:\n1. Holidays \n2. Weekends \nSelect Any Of Above:"))
            if days==1:
                print("You Are Coming In Holiday")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 6000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Evening with Premium Sitting in Holiday Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 24000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Evening with Premium Sitting in Holiday with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
            else:
                print("You Are Coming In Weekends")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 10000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Evening with Premium Sitting in Weekend Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 40000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Evening with Premium Sitting in Weekend with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
        else:
            print("You Have Selected VIP Sitting. ")
            days=int(input("Enter Dasy:\n1. Holidays \n2. Weekends \nSelect Any Of Above:"))
            if days==1:
                print("You Are Coming In Holiday")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 12000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Evening with VIP Sitting in Holiday Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 60000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Evening with VIP Sitting in Holiday with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
            else:
                print("You Are Coming In Weekends")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 15000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Evening with Standard Sitting in Weekend Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 70000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Evening with Standard Sitting in Weekend with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      

    else:
        print("You have selected Night")
        seat=int(input("Which Seat You Want :\n1. Standard \n2. Premium \n3. VIP(Type Anything) \nSelect Any Of Above:"))
        if seat == 1:
            print("You Have Selected Standard Sitting. ")
            days=int(input("Enter Dasy:\n1. Holidays \n2. Weekends \nSelect Any Of Above:"))
            if days==1:
                print("You Are Coming In Holiday")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 3000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Night with Standard Sitting in Holiday Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 12000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Night with Standard Sitting in Holiday with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
            else:
                print("You Are Coming In Weekends")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 5000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Night with Standard Sitting in Weekend Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 20000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Night with Standard Sitting in Weekend with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      

        elif seat==2:
            print("You Have Selected Premium Sitting. ")
            days=int(input("Enter Dasy:\n1. Holidays \n2. Weekends \nSelect Any Of Above:"))
            if days==1:
                print("You Are Coming In Holiday")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 6000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Night with Premium Sitting in Holiday Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 24000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Night with Premium Sitting in Holiday with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
            else:
                print("You Are Coming In Weekends")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 10000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Night with Premium Sitting in Weekend Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 40000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Night with Premium Sitting in Weekend with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
        else:
            print("You Have Selected VIP Sitting. ")
            days=int(input("Enter Dasy:\n1. Holidays \n2. Weekends \nSelect Any Of Above:"))
            if days==1:
                print("You Are Coming In Holiday")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 12000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Night with VIP Sitting in Holiday Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 60000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Night with VIP Sitting in Holiday with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
            else:
                print("You Are Coming In Weekends")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 15000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Night with Standard Sitting in Weekend Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 70000
                    tax = budget//10
                    print(f"As You Have Selected 2D Movie at Night with Standard Sitting in Weekend with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      

        
elif select==2:
    print("***Welcome To The 3D Movie Section***")
    timing=int(input("Select Time:\n1. Morning \n2. Afternoon \n3. Evening \n4. Night(Type Any Thing)\n Select Any Of Above:"))
    if timing == 1:
        print("You have selected morning")
        seat=int(input("Which Seat You Want :\n1. Standard \n2. Premium \n3. VIP(Type Anything) \nSelect Any Of Above:"))
        if seat == 1:
            print("You Have Selected Standard Sitting. ")
            days=int(input("Enter Dasy:\n1. Holidays \n2. Weekends \nSelect Any Of Above:"))
            if days==1:
                print("You Are Coming In Holiday")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 3000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Morning with Standard Sitting in Holiday Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 12000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Morning with Standard Sitting in Holiday with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
            else:
                print("You Are Coming In Weekends")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 5000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Morning with Standard Sitting in Weekend Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 20000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Morning with Standard Sitting in Weekend with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      

        elif seat==2:
            print("You Have Selected Premium Sitting. ")
            days=int(input("Enter Dasy:\n1. Holidays \n2. Weekends \nSelect Any Of Above:"))
            if days==1:
                print("You Are Coming In Holiday")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 6000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Morning with Premium Sitting in Holiday Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 24000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Morning with Premium Sitting in Holiday with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
            else:
                print("You Are Coming In Weekends")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 10000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Morning with Premium Sitting in Weekend Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 40000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Morning with Premium Sitting in Weekend with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
        else:
            print("You Have Selected VIP Sitting. ")
            days=int(input("Enter Dasy:\n1. Holidays \n2. Weekends \nSelect Any Of Above:"))
            if days==1:
                print("You Are Coming In Holiday")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 12000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Morning with VIP Sitting in Holiday Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 60000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Morning with VIP Sitting in Holiday with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
            else:
                print("You Are Coming In Weekends")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 15000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Morning with Standard Sitting in Weekend Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 70000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Morning with Standard Sitting in Weekend with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      

        
    elif timing ==2:
        print("You have selected Afternoon")
        seat=int(input("Which Seat You Want :\n1. Standard \n2. Premium \n3. VIP(Type Anything) \nSelect Any Of Above:"))
        if seat == 1:
            print("You Have Selected Standard Sitting. ")
            days=int(input("Enter Dasy:\n1. Holidays \n2. Weekends \nSelect Any Of Above:"))
            if days==1:
                print("You Are Coming In Holiday")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 3000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Afternoon with Standard Sitting in Holiday Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 12000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Afternoon with Standard Sitting in Holiday with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
            else:
                print("You Are Coming In Weekends")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 5000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Afternoon with Standard Sitting in Weekend Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 20000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Afternoon with Standard Sitting in Weekend with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      

        elif seat==2:
            print("You Have Selected Premium Sitting. ")
            days=int(input("Enter Dasy:\n1. Holidays \n2. Weekends \nSelect Any Of Above:"))
            if days==1:
                print("You Are Coming In Holiday")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 6000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Afternoon with Premium Sitting in Holiday Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 24000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Afternoon with Premium Sitting in Holiday with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
            else:
                print("You Are Coming In Weekends")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 10000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Afternoon with Premium Sitting in Weekend Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 40000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Afternoon with Premium Sitting in Weekend with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
        else:
            print("You Have Selected VIP Sitting. ")
            days=int(input("Enter Dasy:\n1. Holidays \n2. Weekends \nSelect Any Of Above:"))
            if days==1:
                print("You Are Coming In Holiday")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 12000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Afternoon with VIP Sitting in Holiday Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 60000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Afternoon with VIP Sitting in Holiday with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
            else:
                print("You Are Coming In Weekends")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 15000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Afternoon with Standard Sitting in Weekend Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 70000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Afternoon with Standard Sitting in Weekend with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      

    elif timing ==3:
        print("You have selected Evening")
        seat=int(input("Which Seat You Want :\n1. Standard \n2. Premium \n3. VIP(Type Anything) \nSelect Any Of Above:"))
        if seat == 1:
            print("You Have Selected Standard Sitting. ")
            days=int(input("Enter Dasy:\n1. Holidays \n2. Weekends \nSelect Any Of Above:"))
            if days==1:
                print("You Are Coming In Holiday")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 3000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Evening with Standard Sitting in Holiday Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 12000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Evening with Standard Sitting in Holiday with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
            else:
                print("You Are Coming In Weekends")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 5000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Evening with Standard Sitting in Weekend Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 20000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Evening with Standard Sitting in Weekend with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      

        elif seat==2:
            print("You Have Selected Premium Sitting. ")
            days=int(input("Enter Dasy:\n1. Holidays \n2. Weekends \nSelect Any Of Above:"))
            if days==1:
                print("You Are Coming In Holiday")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 6000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Evening with Premium Sitting in Holiday Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 24000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Evening with Premium Sitting in Holiday with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
            else:
                print("You Are Coming In Weekends")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 10000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Evening with Premium Sitting in Weekend Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 40000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Evening with Premium Sitting in Weekend with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
        else:
            print("You Have Selected VIP Sitting. ")
            days=int(input("Enter Dasy:\n1. Holidays \n2. Weekends \nSelect Any Of Above:"))
            if days==1:
                print("You Are Coming In Holiday")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 12000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Evening with VIP Sitting in Holiday Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 60000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Evening with VIP Sitting in Holiday with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
            else:
                print("You Are Coming In Weekends")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 15000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Evening with Standard Sitting in Weekend Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 70000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Evening with Standard Sitting in Weekend with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      

    else:
        print("You have selected Night")
        seat=int(input("Which Seat You Want :\n1. Standard \n2. Premium \n3. VIP(Type Anything) \nSelect Any Of Above:"))
        if seat == 1:
            print("You Have Selected Standard Sitting. ")
            days=int(input("Enter Dasy:\n1. Holidays \n2. Weekends \nSelect Any Of Above:"))
            if days==1:
                print("You Are Coming In Holiday")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 3000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Night with Standard Sitting in Holiday Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 12000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Night with Standard Sitting in Holiday with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
            else:
                print("You Are Coming In Weekends")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 5000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Night with Standard Sitting in Weekend Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 20000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Night with Standard Sitting in Weekend with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      

        elif seat==2:
            print("You Have Selected Premium Sitting. ")
            days=int(input("Enter Dasy:\n1. Holidays \n2. Weekends \nSelect Any Of Above:"))
            if days==1:
                print("You Are Coming In Holiday")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 6000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Night with Premium Sitting in Holiday Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 24000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Night with Premium Sitting in Holiday with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
            else:
                print("You Are Coming In Weekends")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 10000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Night with Premium Sitting in Weekend Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 40000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Night with Premium Sitting in Weekend with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
        else:
            print("You Have Selected VIP Sitting. ")
            days=int(input("Enter Dasy:\n1. Holidays \n2. Weekends \nSelect Any Of Above:"))
            if days==1:
                print("You Are Coming In Holiday")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 12000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Night with VIP Sitting in Holiday Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 60000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Night with VIP Sitting in Holiday with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
            else:
                print("You Are Coming In Weekends")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 15000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Night with Standard Sitting in Weekend Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 70000
                    tax = budget//10
                    print(f"As You Have Selected 3D Movie at Night with Standard Sitting in Weekend with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      

else:
    print("***Welcome To The IMAX Movie Section***")
    timing=int(input("Select Time:\n1. Morning \n2. Afternoon \n3. Evening \n4. Night(Type Any Thing)\n Select Any Of Above:"))
    if timing == 1:
        print("You have selected morning")
        seat=int(input("Which Seat You Want :\n1. Standard \n2. Premium \n3. VIP(Type Anything) \nSelect Any Of Above:"))
        if seat == 1:
            print("You Have Selected Standard Sitting. ")
            days=int(input("Enter Dasy:\n1. Holidays \n2. Weekends \nSelect Any Of Above:"))
            if days==1:
                print("You Are Coming In Holiday")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 3000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Morning with Standard Sitting in Holiday Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 12000
                    tax = budget//10
                    print(f"As You Have Selected  Movie at Morning with Standard Sitting in Holiday with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
            else:
                print("You Are Coming In Weekends")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 5000
                    tax = budget//10
                    print(f"As You Have Selected  Movie at Morning with Standard Sitting in Weekend Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 20000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Morning with Standard Sitting in Weekend with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      

        elif seat==2:
            print("You Have Selected Premium Sitting. ")
            days=int(input("Enter Dasy:\n1. Holidays \n2. Weekends \nSelect Any Of Above:"))
            if days==1:
                print("You Are Coming In Holiday")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 6000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Morning with Premium Sitting in Holiday Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 24000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Morning with Premium Sitting in Holiday with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
            else:
                print("You Are Coming In Weekends")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 10000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Morning with Premium Sitting in Weekend Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 40000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Morning with Premium Sitting in Weekend with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
        else:
            print("You Have Selected VIP Sitting. ")
            days=int(input("Enter Dasy:\n1. Holidays \n2. Weekends \nSelect Any Of Above:"))
            if days==1:
                print("You Are Coming In Holiday")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 12000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Morning with VIP Sitting in Holiday Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 60000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Morning with VIP Sitting in Holiday with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
            else:
                print("You Are Coming In Weekends")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 15000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Morning with Standard Sitting in Weekend Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 70000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Morning with Standard Sitting in Weekend with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      

        
    elif timing ==2:
        print("You have selected Afternoon")
        seat=int(input("Which Seat You Want :\n1. Standard \n2. Premium \n3. VIP(Type Anything) \nSelect Any Of Above:"))
        if seat == 1:
            print("You Have Selected Standard Sitting. ")
            days=int(input("Enter Dasy:\n1. Holidays \n2. Weekends \nSelect Any Of Above:"))
            if days==1:
                print("You Are Coming In Holiday")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 3000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Afternoon with Standard Sitting in Holiday Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 12000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Afternoon with Standard Sitting in Holiday with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
            else:
                print("You Are Coming In Weekends")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 5000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Afternoon with Standard Sitting in Weekend Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 20000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Afternoon with Standard Sitting in Weekend with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      

        elif seat==2:
            print("You Have Selected Premium Sitting. ")
            days=int(input("Enter Dasy:\n1. Holidays \n2. Weekends \nSelect Any Of Above:"))
            if days==1:
                print("You Are Coming In Holiday")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 6000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Afternoon with Premium Sitting in Holiday Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 24000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Afternoon with Premium Sitting in Holiday with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
            else:
                print("You Are Coming In Weekends")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 10000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Afternoon with Premium Sitting in Weekend Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 40000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Afternoon with Premium Sitting in Weekend with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
        else:
            print("You Have Selected VIP Sitting. ")
            days=int(input("Enter Dasy:\n1. Holidays \n2. Weekends \nSelect Any Of Above:"))
            if days==1:
                print("You Are Coming In Holiday")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 12000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Afternoon with VIP Sitting in Holiday Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 60000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Afternoon with VIP Sitting in Holiday with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
            else:
                print("You Are Coming In Weekends")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 15000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Afternoon with Standard Sitting in Weekend Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 70000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Afternoon with Standard Sitting in Weekend with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      

    elif timing ==3:
        print("You have selected Evening")
        seat=int(input("Which Seat You Want :\n1. Standard \n2. Premium \n3. VIP(Type Anything) \nSelect Any Of Above:"))
        if seat == 1:
            print("You Have Selected Standard Sitting. ")
            days=int(input("Enter Dasy:\n1. Holidays \n2. Weekends \nSelect Any Of Above:"))
            if days==1:
                print("You Are Coming In Holiday")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 3000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Evening with Standard Sitting in Holiday Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 12000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Evening with Standard Sitting in Holiday with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
            else:
                print("You Are Coming In Weekends")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 5000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Evening with Standard Sitting in Weekend Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 20000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Evening with Standard Sitting in Weekend with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      

        elif seat==2:
            print("You Have Selected Premium Sitting. ")
            days=int(input("Enter Dasy:\n1. Holidays \n2. Weekends \nSelect Any Of Above:"))
            if days==1:
                print("You Are Coming In Holiday")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 6000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Evening with Premium Sitting in Holiday Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 24000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Evening with Premium Sitting in Holiday with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
            else:
                print("You Are Coming In Weekends")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 10000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Evening with Premium Sitting in Weekend Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 40000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Evening with Premium Sitting in Weekend with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
        else:
            print("You Have Selected VIP Sitting. ")
            days=int(input("Enter Dasy:\n1. Holidays \n2. Weekends \nSelect Any Of Above:"))
            if days==1:
                print("You Are Coming In Holiday")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 12000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Evening with VIP Sitting in Holiday Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 60000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Evening with VIP Sitting in Holiday with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
            else:
                print("You Are Coming In Weekends")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 15000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Evening with Standard Sitting in Weekend Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 70000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Evening with Standard Sitting in Weekend with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      

    else:
        print("You have selected Night")
        seat=int(input("Which Seat You Want :\n1. Standard \n2. Premium \n3. VIP(Type Anything) \nSelect Any Of Above:"))
        if seat == 1:
            print("You Have Selected Standard Sitting. ")
            days=int(input("Enter Dasy:\n1. Holidays \n2. Weekends \nSelect Any Of Above:"))
            if days==1:
                print("You Are Coming In Holiday")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 3000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Night with Standard Sitting in Holiday Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 12000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Night with Standard Sitting in Holiday with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
            else:
                print("You Are Coming In Weekends")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 5000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Night with Standard Sitting in Weekend Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 20000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Night with Standard Sitting in Weekend with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      

        elif seat==2:
            print("You Have Selected Premium Sitting. ")
            days=int(input("Enter Dasy:\n1. Holidays \n2. Weekends \nSelect Any Of Above:"))
            if days==1:
                print("You Are Coming In Holiday")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 6000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Night with Premium Sitting in Holiday Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 24000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Night with Premium Sitting in Holiday with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
            else:
                print("You Are Coming In Weekends")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 10000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Night with Premium Sitting in Weekend Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 40000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Night with Premium Sitting in Weekend with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
        else:
            print("You Have Selected VIP Sitting. ")
            days=int(input("Enter Dasy:\n1. Holidays \n2. Weekends \nSelect Any Of Above:"))
            if days==1:
                print("You Are Coming In Holiday")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 12000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Night with VIP Sitting in Holiday Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 60000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Night with VIP Sitting in Holiday with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
            else:
                print("You Are Coming In Weekends")
                members=int(input("Coming With Group Or Individuals:\n1. Individuals \n2. Group(4 Member)Type Anything \nSelect Any Of Above:"))
                if members==1:
                    budget= 15000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Night with Standard Sitting in Weekend Individual.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")
                else:
                    budget= 70000
                    tax = budget//10
                    print(f"As You Have Selected IMAX Movie at Night with Standard Sitting in Weekend with Group.\n Bill Is :{budget} and with 10% Tax Is {tax}. ")      
