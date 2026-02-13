# marks=int(input("Enter Your Total Marks:"))
# att=int(input("Enter Your Attendance in %:"))
# quiz=int(input("Enter Your Quiz Marks:"))
# assignment=int(input("Enter Your Assignment Marks:"))
# mid=int(input("Enter Your Mid Marks:"))
# final=int(input("Enter Final Marks:"))
# 
# if (marks>=80 and marks < 100 ) and att >= 85 and quiz >= 7 and assignment >=7 and mid >= 25 and final >= 45:
#     print("Excellent Performance - Eligible For 100% Scholarship.")
# elif (marks>=70 and marks < 100) and att >= 80 and quiz >= 6 and assignment >=6 and mid >= 20 and final >= 40:
#     print("Excellent Performance - Eligible For 90% Scholarship.")
# elif (marks>=60 and marks < 100) and att >= 70 and quiz >= 5 and assignment >=5 and mid >= 18 and final >= 35:
#     print("Excellent Performance - Eligible For 50% Scholarship.")
# 
# elif (marks >= 50 and marks < 100 )and att < 70 :
#     print("Average - Not Eligible For Scholarship For 50% Scholarship.")
# else:
#     print("Not Allowed To Sit In Exam.!")



#eval
# e=eval(input("Enter Your Input:"))
# print(type(e))
# print(e)


# multi user varification system

uname=input("Enter Your User Name:").lower()
password=input("Enter Your Password:")

if (uname=="safia" or uname=="syedasafiamaham@gmail.com" or uname=="03334455666") and (password=="safia123"):
    print(f"Dear {uname} , Welcome To The Portal.")
elif(uname=="maham" or uname=="syedamaham123456@gmail.com" or uname=="0316656783") and (password=="maham123"):
    print(f"Dear {uname} , Welcome To The Portal.")
elif(uname=="khadija" or uname=="syedahkhadijashah@gmail.com" or uname=="03334567890") and (password=="khadija123"):
    print(f"Dear {uname} , Welcome To The Portal.")
else:
    print(f"Dear {uname} , Invalid User.")
    













