print("******************************* Gaming & Entertainment *********************************")
character=int(input("Enter Your Character Race:\n1. Human (Power:Health: Medium , Defense: Medium , Brain (Intelligence): Medium \n2. ELF (Power:Health: Less , Defense: Less ,Brain (Intelligence): More ) \n3. Dwarf (Power: Health: More , Defense: More ,Brain (Intelligence): Less) Type Anything  \nSelect Any Of Above:"))
class_select=int(input("Select Your Class :\n_____________________________\n1. Warrior (Fight: Fight style:Go near to enemy for figh , \nWeapon:(Sword, axe, shield ,Strength)\nStrength: (Heavy Brain , Bear More) \nWeakness: (Slow Speed, Cant Attact From Far )\n_______________________________________ \n2. Mage (Fight style:Attack From Far With magic attacks \nWeapon:Staff, spells \nStrength:Firewall, lightning — More brain \nWeakness:Health Less, Cant Fight From Near )\n__________________________________ \n3. Archer (Fight style:Fight From Far With Arrows \n Weapon:Bow & arrows \nStrength:Fast attacks, accurate shots \nWeakness:Defense less,weak in close fight ) \n________________________\nSelect Any Of Above:"))
print("===========================================================================================")
if character==1:
    skills=int(input("Enter Your Priority Skill \n1. Brain \n2. Health/ Defense \n3. Medium (type anything)\n=========================== \nSelect Any Of Above:"))
    if skills==1:
        point=10
        if point==10:
            print(f"Allocated Equiptment is , Weapon:(Staff, spells) and the points is {point}")
            print("Assigned Quest Is : Recover Ancient magic book Or spell.")
            print("____________________________________________________")
        else:
            print("Not Enough Points")
    elif skills==2:
        point=11
        if point==11:
            print(f"Allocated Equiptment is , Weapon:(Sword, axe, shield ,Strength) and the point is {point} ")
            print("Assigned Quest Is : Defeat Enemy Boss Face To Face in Fight .")
        else:
            print("Not Enough Points")
    else:
        point= 12
        if point==12:
            print(f"Allocated Equiptment is , Weapon:Bow & arrows and the points is {point}")
            print("Assigned Quest Is : To Defeat The Enemy In Forest From Far With Arrows.")
        else:
            print("Not Enough Points")
    
    
elif character == 2:
    skills=int(input("Enter Your Priority Skill \n1. Brain \n2. Health/ Defense \n3. Medium (type anything) \nSelect Any Of Above:"))
    if skills==1:
        point=15
        if point==15:
            print(f"Allocated Equiptment is , Weapon:(Staff, spells) and the points is {point}")
            print("Assigned Quest Is : Recover Ancient magic book Or spell.")
        else:
            print("Not Enough Points")
    elif skills==2:
        point=16
        if point==16:
            print(f"Allocated Equiptment is , Weapon:(Sword, axe, shield ,Strength) and the point is {point} ")
            print("Assigned Quest Is : Defeat Enemy Boss Face To Face in Fight .")
            
        else:
            print("Not Enough Points")
    else:
        point= 17
        if point==17:
            print(f"Allocated Equiptment is , Weapon:Bow & arrows and the points is {point}")
            print("Assigned Quest Is : To Defeat The Enemy In Forest From Far With Arrows.")
        else:
            print("Not Enough Points")
    
else:
    skills=int(input("Enter Your Priority Skill \n1. Brain \n2. Health/ Defense \n3. Medium (type anything) \nSelect Any Of Above:"))
    if skills==1:
        point=18
        if point==18:
            print(f"Allocated Equiptment is , Weapon:(Staff, spells) and the points is {point}")
            print("Assigned Quest Is : Recover Ancient magic book Or spell.")
        else:
            print("Not Enough Points")
    elif skills==2:
        point=19
        if point==19:
            print(f"Allocated Equiptment is , Weapon:(Sword, axe, shield ,Strength) and the point is {point} ")
            print("Assigned Quest Is : Defeat Enemy Boss Face To Face in Fight .")
        else:
            print("Not Enough Points")
    else:
        point= 20
        if point==20:
            print(f"Allocated Equiptment is , Weapon:Bow & arrows and the points is {point}")
            print("Assigned Quest Is : To Defeat The Enemy In Forest From Far With Arrows.")
        else:
            print("Not Enough Points")