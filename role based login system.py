# Role-Based Login System

# Predefined credentials
correct_username = "john"
correct_role_admin = "admin"
correct_role_user = "user"

# ---------------- LOGIN VALIDATION ----------------
while True:
    username = input("Enter username: ")
    role = input("Enter role (admin/user): ").lower()

    if username == correct_username and role == correct_role_admin:
        print("\nLogin successful as Admin!\n")
        break

    elif username == correct_username and role == correct_role_user:
        print("\nLogin successful as User!\n")
        break

    else:
        print("Invalid credentials. Please try again.\n")


# ---------------- ROLE HANDLING ----------------
if role == "admin":

    # -------- Admin Menu (Nested While) --------
    while True:
        print("---- ADMIN MENU ----")
        print("1. View Reports")
        print("2. Manage Users")
        print("3. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Viewing Reports...\n")

        elif choice == "2":
            print("Managing Users...\n")

        elif choice == "3":
            print("Logging out...")
            break

        else:
            print("Invalid option. Try again.\n")


elif role == "user":

    # -------- User Menu (Nested While) --------
    while True:
        print("---- USER MENU ----")
        print("1. View Profile")
        print("2. Edit Profile")
        print("3. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Viewing Profile...\n")

        elif choice == "2":
            print("Editing Profile...\n")

        elif choice == "3":
            print("Logging out...")
            break

        else:
            print("Invalid option. Try again.\n")
