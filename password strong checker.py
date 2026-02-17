# Password Strength Checker

while True:
    password = input("Enter a password: ")

    # Condition 1: Minimum 8 characters
    if len(password) >= 8:
        
        # Condition 2: At least one digit
        has_digit = False
        for char in password:
            if char.isdigit():
                has_digit = True
                break
        
        if has_digit:
            
            # Condition 3: At least one special character
            has_special = False
            for char in password:
                if not char.isalnum():   # Special character check
                    has_special = True
                    break
            
            if has_special:
                print("Strong Password ")
                break
            else:
                print("Medium Password - Add at least one special character.")
        
        else:
            print("Medium Password - Add at least one digit.")
    
    else:
        print("Weak Password - Must be at least 8 characters long.")
