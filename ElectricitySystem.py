name=input("Enter Your Name:")
cust_t=int(input(f"Dear {name}, Which Customer Type Are You? \nPress 1. For Commercial \nPress 2.For Domestic:"))
if cust_t==1:
    print(f"Customer Type: Commercial \nInvoice Name:{name} ")
    units=int(input("Number Of Units You Consumed?:"))
    if units>=450 and units<800:
        print(f"Dear {name} , \nAs per your units:{units} , You Will Be Charged As Rs100/Unit For Commercial \nYour Bill Of Electricity For Current Month Is \nRs {(units*100)+1000}")
    elif units>=300 and units<450:
        print(f"Dear {name} , \nAs per your units:{units} , You Will Be Charged As Rs85/Unit For Commercial \nYour Bill Of Electricity For Current Month Is \nRs {(units*85)+500}")
    elif units<300:
        print(f"Dear {name} , \nAs per your units:{units} , You Will Be Charged As Rs65/Unit For Commercial \nYour Bill Of Electricity For Current Month Is \nRs {units*65}")
    else:
        print(f"Dear {name} , \nAs per your units:{units} , You Will Be Charged As Rs150/Unit For Commercial \nYour Bill Of Electricity For Current Month Is \nRs {units*150}")

elif cust_t==2:
    print(f"Customer Type: Domestic \nInvoice Name:{name} ")
    units=int(input("Number Of Units You Consumed?:"))
    if units>=450 and units<800:
        print(f"Dear {name} , \nAs per your units:{units} , You Will Be Charged As Rs 80/Unit For Domestic \nYour Bill Of Electricity For Current Month Is \nRs {(units*80)+800}")
    elif units>=300 and units<450:
        print(f"Dear {name} , \nAs per your units:{units} , You Will Be Charged As Rs 60/Unit For Domestic \nYour Bill Of Electricity For Current Month Is \nRs {(units*60)+400}")
    elif units<300:
        print(f"Dear {name} , \nAs per your units:{units} , You Will Be Charged As Rs 40/Unit For Domestic \nYour Bill Of Electricity For Current Month Is \nRs {units*40}")
    else:
        print(f"Dear {name} , \nAs per your units:{units} , You Will Be Charged As Rs 100/Unit For Domestic \nYour Bill Of Electricity For Current Month Is \nRs {units*150}")
else:
    print("Invalid Input")
    