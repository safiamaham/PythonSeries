#Multi Domain System
print("***Multi Domain System***")
uname=input("Enter User Name:")
password=input("Enter Password:")


if (uname=="safiamaham" or uname=="0333333333") and password=="safia123":
    print(f"Dear {uname} , Welcome To The Facebook .")
elif (uname=="safia123" or uname=="safia123@gmail.com") and password=="safia123":
    print(f"Dear {uname}, Welcome To The Linked In .")
elif (uname=="maham123" or uname=="maham123@gmail.com") and password=="maham123":
    print(f"Dear {uname}, Welcome To The Instagram .")
elif (uname=="khadija11" or uname=="khadija123@gmail.com") and password=="04feb2023":
    print(f"Dear {uname}, Welcome To The GitHub .")
else:
    print("Invalid User.")