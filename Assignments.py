# 
# 
# #Eligibility For Exam
# print("***Eligibility For Exam***")
# 
# numberOfClasses=int(input("Enter Your Number Of Classes , (30 , 40 , 50)?"))
# attendedClass=int(input("How Many Classes You Attended?"))
# medicalCertificate=input("Do You Have Medical Certificate?(Yes/No)").lower()
# 
# if numberOfClasses == 30 :
#     if attendedClass >=15:
#         if medicalCertificate=="yes":
#             print("You Are Allowed To Sit In Exam.")
#             print("You will Have Extra 10 Minutes To Complete Your Exam Because You Have Medical Certificate.")
#         else:
#             print("You Are Allowed To Sit In Exam.But You Will Not Be Given Extra Premisis.Because You Dont Have MC.")
#     else:
#         print("You Are Not Allowed To Sit In The Class Because Of Low Attended Class.")
# elif numberOfClasses == 40 :
#     if attendedClass >=20:
#         if medicalCertificate=="yes":
#             print("You Are Allowed To Sit In Exam.")
#             print("You will Have Extra 10 Minutes To Complete Your Exam Because You Have Medical Certificate.")
#         else:
#             print("You Are Allowed To Sit In Exam.But You Will Not Be Given Extra Premisis.Because You Dont Have MC.")
#     else:
#         print("You Are Not Allowed To Sit In The Class Because Of Low Attended Class.")
# elif numberOfClasses == 50 :
#     if attendedClass >=25:
#         if medicalCertificate=="yes":
#             print("You Are Allowed To Sit In Exam.")
#             print("You will Have Extra 10 Minutes To Complete Your Exam Because You Have Medical Certificate.")
#         else:
#             print("You Are Allowed To Sit In Exam.But You Will Not Be Given Extra Premisis.Because You Dont Have MC.")
#     else:
#         print("You Are Not Allowed To Sit In The Class Because Of Low Attended Class.")
# else:
#     print("Invalid Number Of Classes.")



#Bill Calculation

# name=input("Enter Your Name:")
# units=int(input("Enter Your Units Of Bill:"))
# customerType=input("Which Type Of Customer You Are?(Domestic/Commercial):").lower()
# 
# if units>=300:
#     if customerType=="commercial":
#         print(f"Dear {name} , Your Units Is {units} and You are {customerType} So Extra Surcharge Will Be Taken.")
#         calculate=(units*35)+2000
#         print(f"Dear {name} , Your Bill is {calculate}.")
#     else:
#         calculate=(units*25)+2000
#         print(f"Dear {name}, Your Unit Is {units} , Your Final Bill Is {calculate} Because Your Are {customerType}.")
# elif units>=200:
#     if customerType=="commercial":
#         print(f"Dear {name} , Your Units Is {units} and You are {customerType} So Extra Surcharge Will Be Taken.")
#         calculate=(units*30)
#         print(f"Dear {name} , Your Bill is {calculate}.")
#     else:
#         calculate=(units*20);
#         print(f"Dear {name}, Your Unit Is {units} , Your Final Bill Is {calculate} Because Your Are {customerType}.")
# elif units>=100:
#     if customerType=="commercial":
#         print(f"Dear {name} , Your Units Is {units} and You are {customerType}.")
#         calculate=(units*20)
#         print(f"Dear {name} , Your Bill is {calculate}.")
#     else:
#         calculate=(units*15);
#         print(f"Dear {name}, Your Unit Is {units} , Your Final Bill Is {calculate} Because Your Are {customerType}.")
# else:
#     if customerType=="commercial":
#         print(f"Dear {name} , Your Units Is {units} and You are {customerType}.")
#         calculate=(units*15)
#         print(f"Dear {name} , Your Bill is {calculate}.")
#     else:
#         print(f"Dear {name} , Your Units Is {units} and You are {customerType}.")
#         calculate=(units*10)
#         print(f"Dear {name} , Your Bill is {calculate}.")
        























