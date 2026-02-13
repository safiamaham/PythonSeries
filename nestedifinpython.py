#Nested Decissions in Python
#multi decission program

print("***Welcome To Netflix***")

name=input("Enter Your Name:")
email=input("Enter Your Email:")
password=input("Enter Your Password:")
age=int(input("Enter Your Age:"))

if age>=18:
    print(f"Dear {name} , Welcome to Netflix.")
    if email=="safia@gmail.com" and password=="safia123":
        print(f"Dear {name} , Welcome to the Netflix Session , Please Select Catagory.")
    elif email=="maham@gmail.com" and password=="maham123":
        print(f"Dear {name} , Welcome to the Netflix Session , Please Select Catagory.")
    elif email=="khadija@gmail.com" and password=="khadija123":
        print(f"Dear {name} , Welcome to the Netflix Session , Please Select Catagory.")
    elif email=="kulsoom@gmail.com" and password=="kulsoom123":
        print(f"Dear {name} , Welcome to the Netflix Session , Please Select Catagory.")
    elif email=="anoosha@gmail.com" and password=="anoosha123":
        print(f"Dear {name} , Welcome to the Netflix Session , Please Select Catagory.")
    elif email=="batool@gmail.com" and password=="batool123":
        print(f"Dear {name} , Welcome to the Netflix Session , Please Select Catagory.")
    else:
        print(f"Dear {name} , Your Login Credentials Are Invalid.") 
else:
    print(f"Dear {name} , Please Watch Pogo.")