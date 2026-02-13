#Multiple App Player

Print=("***Multiple App player***")
select=int(input("Select An APP You Want To Work:\n1.Calculator \n2.Student Marksheet\n3.Clothing Store \n4.Car Recommendation :"))

if select==1:
    method=input("What You Want To Do ?\n1.Addition \n2.Subraction \n3.Devision \n4.Multiply:")
    num1=eval(input("Enter Number 1 To Proceed:"))
    num2=eval(input("Enter Number 2 To Proceed:"))
    if method=="1":
        print(f"This Is Your Addition:{num1+num2}.")
    elif method=="2":
        print(f"This Is Your Subraction:{num1-num2}.")
    elif method=="3":
        print(f"This Is Your Devision:{num1/num2}.")
    elif method=="4":
        print(f"This Is Your Multiplication:{num1*num2}.")
    else:
        print("Invalid Input.")
elif select==2:
    name=input("Enter Your Name:")
    physics=eval(input("Enter Physics Marks:"))
    maths=eval(input("Enter Your Maths Marks:"))
    english=eval(input("Enter Your English Marks:"))
    total=300
    obtainmarks=physics+maths+english
    per=(obtain/total)*100
    if per>=90:
        print(f"Dear {name} , Your Percentage is {per} and Your Grade Is A++.")
    elif per>=80:
        print(f"Dear {name} , Your Percentage is {per} and Your Grade Is A+.")
    elif per>=70:
        print(f"Dear {name} , Your Percentage is {per} and Your Grade Is A.")
    elif per>=60:
        print(f"Dear {name} , Your Percentage is {per} and Your Grade Is B.")
    elif per>=50:
        print(f"Dear {name} , Your Percentage is {per} and Your Grade Is C.")
    else:
        print(f"Dear {name} , You Have Failed.")
elif select==3:
    name=input("Enter Your Name:")
    budget=int(input("Enter Your Budget To Watch Which Clothes You Lie On:"))
    if (budget>=50000 and budget <1000000):
        print(f"Dear {name} , You Can Buy Party Wear.")
    elif (budget>=30000 and budget <50000):
        print(f"Dear {name} , You Can Buy Formal Wear.")
    elif (budget>=4000 and budget <30000):
        print(f"Dear {name} , You Can Buy Casual Wear.")
    else:
        print(f"Dear {name} , Please Increase Your Budget.")
elif select==4:
    name=input("Enter Your Name:")
    budget=int(input("Enter Your Budget For Car Recommendation:"))
    if budget>=500000 and budget <200000:
        print(f"Dear {name} , You Can Buy, \n1.Mehran \n2.Kia Seltos\n3.Hyundai Creta")
    elif budget>=200000 and budget <5000000:
        print(f"Dear {name} , You Can Buy, \n1.Hyundai Tucson\n2.Honda Civic\n3.Toyota Urban Cruiser Hyryder")
    elif budget>=5000000:
        print(f"Dear {name} , You Can Buy, \n1.Toyota Land Cruiser\n2.Mercedes-Benz GLA / GLB / GLC\n3.Audi Q3 / Q5")
    else:
        print(f"Dear {name}, Please Increase Your Budget.")
else:
    print("Invalid Input.")
    