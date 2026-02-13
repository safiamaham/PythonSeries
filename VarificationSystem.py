name=input("Enter Your Name:")
t_class=int(input("Enter A Number Of Total Classes:"))
a_classes=int(input("Enter A Number Of Attendence / Classes Attended: (in No(s)):"))

per=(a_classes/t_class)*100

if per>=75:
    print(f"Dear {name}, You Are Allowed To Sit In Exam . No Medical Certificate.")
elif per>=20 and per<75:
    print(f"Dear {name}, Your Percentage Is Below 75%.")
    med_c=int(input("Do You Have Medical Certificate? : \nPress 1.For Yes \nPress 2. For No:"))
    if med_c == 1:
        print("Your Medical Certificate Is Proceed To Varification.")
        var=int(input("Let Me Know Is It Signed And Stampped? : \nPress 1.For Yes \nPress 2. For No:"))
        if var==1:
            print(f"Dear {name}, Despite Your Attendance Is Low , But Your Medical Certificate Is Verified And You Are Allowed To Sit In Exam.")
        elif var==2:
            print(f"Dear {name}, Your Attendance Is Low , And Your Medical Certificate Is Not Verified And You Are Not Allowed To Sit In Exam.")
        else:
            print("Invalid Input.")
    else:
        print("Your Are Not Allowed To Sit In Exam.")
else:
    print("Attendance Percentage Is Very Low ! You Are Not Allowed To Sit In Exam.")