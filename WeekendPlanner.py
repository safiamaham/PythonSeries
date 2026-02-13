# welcome to event planner
print("***Welcome To Event Planner***")

name=input("Enter Your Name:")
mood=input("Enter Your Mood (Happy/Sad/Tired)?").lower()
budget=int(input("Enter Your Budget ($):"))
weather=input("Weather Today? (Sunny/Rainy/Cold):").lower()
company=input("Who Are You With? (Alone/Friends/Family):").lower()

print("\n Planning Weekend...\n")

if mood=="happy":
    if budget > 1000:
        if weather=="sunny":
            if company=="friends":
                print(f"Dear {name},😎 Go For An Outdoor Movie + Street Food Party!.")
            else:
                print("Watch Block Buster Movie.")
        else:
            print("Order Pizza + Netflix At Home.")
    else:
        print("Watch Comedy Movie On Mobile With Snacks!!.")
elif mood=="sad":
    if company=="alone":
        print("Watch Motivational Movie And Order Comfort Food.")
    else:
        if budget > 500:
            print("Ice-Creame + Feel Good Movie With Loved One.")
        else:
            print("Team + Old Classic Movie.")
elif mood=="tired":
    if weather=="cold":
        print("Sleep Early + Light Music!")
    else:
        if budget > 300:
            print("Fast Food + And Watch Comedy Movie.!")
        else:
            print("Relax With Music Or Book!.")
else:
    print("Mood Not Recognized , Just Relax And Enjoy Your Time.! ")
    
    



