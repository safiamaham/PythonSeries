print("*********Wecome To AI Restaurant**************")

person = int(input("How Many Person You Are? \n1. 8 to 15 \n2. 6 to 8 \n3. 4 to 6 \n4. 2 to 4 \nSelect Any Of The Above?:"))
if person==1:
    person2=int(input("Whats The Count Of Person You Have?"))
    if  (person2 >= 8 and person2 <= 15):
        version=int(input("What Do You Want Us To Do For You?: \n1. Something Special\n2.Something In Mind\nSelect Any One?:"))
        print("===============================================")
        if version == 1:
            fav=int(input("What do you eat commonly? \n1.Biryani \n2.Karahi \n3.BBQ \nSelect Any One:"))
            print("===============================================")         
            if fav == 1:
                time=int(input("Do You Eat \n1.Regularly \n2.Week \n3.Monthly\nSelect Any Of Above?:"))
                print("===============================================")
                if time == 1:
                    varient=int(input("Do You Want:\n1.Chicken \n2.Mutton(Most Recommended ) \n3.Beef (Most Recommended)(Type Anything For Beef),:"))
                    print("===============================================")
                    if varient ==1:
                        typ=int(input("What Do You Want To Eat?\n1. Bombay Biryani \n2. Sindhi Biryani \n3. Hyderabadi Biryani\n4. Or Type Anything For Something Special In Rice\nSelect Any Specific Of Above:"))
                        print("===============================================")
                        if typ == 1:
                            print("********************Moving For Bombay Biryani Lover ****************")
                            bir_daigh=2200 #16500
                            sajji_per=2000 #15000
                            kunaffa=1500   #11250
                            gulabj=100     
                            #for the purpose to calculate total price of gulab jamun
                            gulabj_per=person2*2  #14000
                            special_dr=600   #9000
                            meetha_p=100     # 1500
                            daigh_kg=person2//3
                            quantity=person2//2
                            #calculation For Bill
                            bill=(bir_daigh*daigh_kg)+(sajji_per*quantity)+(kunaffa*quantity)+(gulabj*gulabj_per)+(special_dr*person2)+(meetha_p*person2)
                            tax=bill/10
                            print(f"Dear Customer! \nYour Order is here confirmed and here\n1. {daigh_kg} KG Fresh Live Chicken Bombay Biryaani\n____________________  \n2. Fresh Live {quantity} Sajji\n____________________  \n3. {quantity} Kunafah\n____________________  \n4.{gulabj_per} Gulaab Jamun \n____________________ \n5.{person2} Special Drink\n____________________  \n6. {person2} Special Meetha Paan\n____________________ ")
                            print(f"Dear Customer! \nYour Total Bill is: \n1. {daigh_kg}KG Fresh Live Chicken Bombay Biryaani Rs.{bir_daigh*daigh_kg}/-\n____________________   \n2. Fresh Live {quantity} Sajji Rs {sajji_per*quantity}/-\n____________________  \n3. {quantity} Kunafah Rs {kunaffa*quantity}/-\n____________________  \n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/-\n____________________  \n5.{person2} Special Drink Rs {special_dr*person2}/-\n____________________  \n6. {person2} Special Meetha Paan Rs {meetha_p*person2}/-\n____________________  \nTotal Bill: Rs{bill} + Tax {tax} \nGrand Total: {bill+tax}/-\n____________________  ")
                        elif typ == 2:
                            print("=============================")
                            print("********************Moving For Sindhi Biryani Lover ****************")
                            bir_daigh=2200 #16500
                            tikka_per=1500 #15000
                            kunaffa=1500   #11250
                            gulabj=100     
                            #for the purpose to calculate total price of gulab jamun
                            gulabj_per=person2*2  #14000
                            limca_dr=600   #9000
                            meetha_p=100     # 1500
                            daigh_kg=person2//3
                            quantity=person2//2
                            #calculation For Bill
                            bill=(bir_daigh*daigh_kg)+(tikka_per*quantity)+(kunaffa*quantity)+(gulabj*gulabj_per)+(limca_dr*person2)+(meetha_p*person2)
                            tax=bill/10
                            print(f"Dear Customer! \nYour Order is confirmed and here\n1. {daigh_kg} KG Fresh Live Chicken Sindhi Biryaani\n____________________  \n2. Fresh Live {quantity} Tikka\n____________________  \n3. {quantity} Kunafah\n____________________  \n4.{gulabj_per} Gulaab Jamun \n____________________ \n5.{person2} Limca Drink\n____________________  \n6. {person2} Special Meetha Paan\n____________________ ")
                            print("==================================================================")
                            print(f"Dear Customer! \nYour Total Bill is: \n1. {daigh_kg} KG Fresh Live Chicken Sindhi  Biryaani Rs.{bir_daigh*daigh_kg}/-\n____________________   \n2. Fresh Live {quantity} Tikka Rs {tikka_per*quantity}/-\n____________________  \n3. {quantity} Kunafah Rs {kunaffa*quantity}/-\n____________________  \n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/-\n____________________  \n5.{person2} Limca Drink Rs {limca_dr*person2}/-\n____________________  \n6. {person2} Special Meetha Paan Rs {meetha_p*person2}/-\n____________________  \nTotal Bill: Rs{bill} + Tax {tax} \n_______________\nGrand Total: {bill+tax}/-\n____________________  ")
                        elif typ == 3:
                            print("=============================")
                            print("********************Moving For Hyderabadi Biryani Lover ****************")
                            bir_daigh=2200 #16500
                            qeema_per=1500 #15000
                            rabri=1500   #11250
                            gulabj=100     
                            #for the purpose to calculate total price of gulab jamun
                            gulabj_per=person2*2  #14000
                            limca_dr=600   #9000
                            meetha_p=100     # 1500
                            daigh_kg=person2//3
                            quantity=person2//2
                            #calculation For Bill
                            bill=(bir_daigh*daigh_kg)+(qeema_per*quantity)+(rabri*quantity)+(gulabj*gulabj_per)+(limca_dr*person2)+(meetha_p*person2)
                            tax=bill/10
                            print(f"Dear Customer! \nYour Order is confirmed and here\n1. {daigh_kg} KG Fresh Live Chicken Hyderabadi Biryaani\n____________________  \n2. Fresh Live {quantity} KG Dum Qeema\n____________________  \n3. {quantity} KG rabri\n____________________  \n4.{gulabj_per} Gulaab Jamun \n____________________ \n5.{person2} Limca Drink\n____________________  \n6. {person2} Special Meetha Paan\n____________________ ")
                            print("==================================================================")
                            print(f"Dear Customer! \nYour Total Bill is: \n1. {daigh_kg} KG Fresh Live Chicken Hyderabadi Biryaani Rs.{bir_daigh*daigh_kg}/-\n____________________   \n2. Fresh Live {quantity} KG Dum Qeema Rs {qeema_per*quantity}/-\n____________________  \n3. {quantity} KG  Rabri Rs {rabri*quantity}/-\n____________________  \n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/-\n____________________  \n5.{person2} Limca Drink Rs {limca_dr*person2}/-\n____________________  \n6. {person2} Special Meetha Paan Rs {meetha_p*person2}/-\n____________________  \nTotal Bill: Rs{bill} + Tax {tax} \n_______________\nGrand Total: {bill+tax}/-\n____________________  ")
                        else:
                            print("")
                            print("=============================")
                            print("********************Moving For Our Special Suggestion For You In Rice ****************")
                            madbi_plat=6000 
                            dumpukht=2500 
                            icecream_falooda=1200   
                            gulabj=100
                            almond_milk=600
                            #for the purpose to calculate total price of gulab jamun
                            gulabj_per=person2*2  
                            fire_meetha_pan=150    
                            platter=person2//3.5
                            quantity=person2//2
                            #calculation For Bill
                            bill=(madbi_plat*platter)+(dumpukht*quantity)+(icecream_falooda*person2)+(gulabj*gulabj_per)+(almond_milk*person2)+(fire_meetha_pan*person2)
                            tax=bill/10
                            print(f"Dear Customer! \nYour Order is confirmed and here\n1. {platter} Fresh Afghani Special Platter \n____________________  \n2. Fresh Live {quantity} KG DumPukht\n____________________  \n3. {person2} Bowl Ice Cream Falooda\n____________________  \n4.{gulabj_per} Gulaab Jamun \n____________________ \n5.{person2} Almond Milk\n____________________  \n6. {person2} Special Fire Meetha Paan\n____________________ ")
                            print("==================================================================")
                            print(f"Dear Customer! \nYour Total Bill is: \n1. {platter}  Fresh Afghani Special Platter Rs.{madbi_plat*platter}/-\n____________________   \n2. Fresh Live {quantity} KG DumPukht Rs {dumpukht*quantity}/-\n____________________  \n3. {person2} Bowl Ice Cream Falooda Rs {icecream_falooda*person2}/-\n____________________  \n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/-\n____________________  \n5.{person2} Almond Milk Rs {almond_milk*person2}/-\n____________________  \n6. {person2} Special Fire Meetha Paan Rs {fire_meetha_pan*person2}/-\n____________________  \nTotal Bill: Rs{bill} + Tax {tax} \n_______________\nGrand Total: {bill+tax}/-\n____________________  ")
                    elif varient == 2:
                        typ=int(input("What Do You Want To Eat?\n1. Moroccan Lamb \n2. Classic Dumpukht Mutton Biryani \n3. Mutton Kabuli Pilao\n4. Or Type Anything For Something Special In Rice\nSelect Any Specific Of Above:"))
                        print("===============================================")
                        if typ == 1:
                            print("********************Moving For Moroccan Lamp Lover ****************")
                            lamb_rice=3000 #16500
                            saalam_lamb=3000 #15000
                            kunaffa=1500   #11250
                            gulabj=100     
                            #for the purpose to calculate total price of gulab jamun
                            gulabj_per=person2*2  #14000
                            special_dr=600   #9000
                            meetha_p=100# 1500
                            
                            platter_kg=person2//3
                            quantity=person2//2
                            #calculation For Bill
                            bill=(lamb_rice*platter_kg)+(saalam_lamb*quantity)+(kunaffa*quantity)+(gulabj*gulabj_per)+(special_dr*person2)+(meetha_p*person2)
                            tax=bill/10
                            print(f"Dear Customer! \nYour Order is here confirmed and here\n1. {Lamb_rice} KG Fresh Live Moroccon Lamb \n____________________  \n2. Fresh Live {quantity} Saalam Lamb\n____________________  \n3. {quantity} Kunafah\n____________________  \n4.{gulabj_per} Gulaab Jamun \n____________________ \n5.{person2} Special Drink\n____________________  \n6. {person2} Special Meetha Paan\n____________________ ")
                            print(f"Dear Customer! \nYour Total Bill is: \n1. {platter_kg} KG Fresh Live Moroccon Lamb Rs.{lamb_rice*platter_kg}/-\n____________________   \n2. Fresh Live {quantity} Saalam Lamb Rs {saalam_lamb*quantity}/-\n____________________  \n3. {quantity} Kunafah Rs {kunaffa*quantity}/-\n____________________  \n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/-\n____________________  \n5.{person2} Special Drink Rs {special_dr*person2}/-\n____________________  \n6. {person2} Special Meetha Paan Rs {meetha_p*person2}/-\n____________________  \nTotal Bill: Rs{bill} + Tax {tax} \nGrand Total: {bill+tax}/-\n____________________  ")
                        elif typ == 2:
                            print("=============================")
                            print("********************Moving For Classic Dumpukht Mutton Biryani Lover ****************")
                            mutton_bir=4500 #16500
                            mutton_rosh=3500 #15000
                            kunaffa=1500   #11250
                            gulabj=100     
                            #for the purpose to calculate total price of gulab jamun
                            gulabj_per=person2*2  #14000
                            limca_dr=600   #9000
                            meetha_p=100     # 1500
                            mutton_kg=person2//3
                            quantity=person2//2
                            #calculation For Bill
                            bill=(mutton_bir*mutton_kg)+(mutton_rosh*mutton_kg)+(kunaffa*quantity)+(gulabj*gulabj_per)+(limca_dr*person2)+(meetha_p*person2)
                            tax=bill/10
                            print(f"Dear Customer! \nYour Order is confirmed and here\n1. {mutton_kg} KG Fresh Live Classic Dumpukht Mutton Biryani\n____________________  \n2. Fresh Live {mutton_kg} Mutton Rosh\n____________________  \n3. {quantity} Kunafah\n____________________  \n4.{gulabj_per} Gulaab Jamun \n____________________ \n5.{person2} Limca Drink\n____________________  \n6. {person2} Special Meetha Paan\n____________________ ")
                            print("==================================================================")
                            print(f"Dear Customer! \nYour Total Bill is: \n1. {mutton_kg} KG Fresh Live Classic Dumpukht Mutton Biryani Rs.{mutton_kg*mutton_bir}/-\n____________________   \n2. Fresh Live {mutton_kg} KG Mutton Rosh Rs {mutton_rosh*mutton_kg}/-\n____________________  \n3. {quantity} Kunafah Rs {kunaffa*quantity}/-\n____________________  \n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/-\n____________________  \n5.{person2} Limca Drink Rs {limca_dr*person2}/-\n____________________  \n6. {person2} Special Meetha Paan Rs {meetha_p*person2}/-\n____________________  \nTotal Bill: Rs{bill} + Tax {tax} \n_______________\nGrand Total: {bill+tax}/-\n____________________  ")
                        elif typ == 3:
                            print("=============================")
                            print("********************Moving For Mutton Kabuli Pilao Lover ****************")
                            kabuli_pilao=3000 #16500
                            mutton_peti_kabab=2000 #15000
                            rabri=1500   #11250
                            gulabj=100     
                            #for the purpose to calculate total price of gulab jamun
                            gulabj_per=person2*2  #14000
                            limca_dr=600   #9000
                            meetha_p=100     # 1500
                            kabuli_kg=person2//3
                            quantity=person2//2
                            #calculation For Bill
                            bill=(kabuli_pilao*kabuli_kg)+(mutton_peti_kabab*person2)+(rabri*mutton_kg)+(gulabj*gulabj_per)+(limca_dr*person2)+(meetha_p*person2)
                            tax=bill/10
                            print(f"Dear Customer! \nYour Order is confirmed and here\n1. {kabuli_kg} KG Fresh Live Kabuli Mutton Pilao\n____________________  \n2. Fresh Live {person2} Mutton Peti Kabab\n____________________  \n3. {quantity} KG rabri\n____________________  \n4.{gulabj_per} Gulaab Jamun \n____________________ \n5.{person2} Limca Drink\n____________________  \n6. {person2} Special Meetha Paan\n____________________ ")
                            print("==================================================================")
                            print(f"Dear Customer! \nYour Total Bill is: \n1. {mutton_kg} KG Fresh Live kabuli Mutton Pilao Rs.{kabuli_pilao*mutton_kg}/-\n____________________   \n2. Fresh Live {person2} Mutton Peti Kabab Rs {mutton_peti_kabab*person2}/-\n____________________  \n3. {quantity} KG  Rabri Rs {rabri*quantity}/-\n____________________  \n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/-\n____________________  \n5.{person2} Limca Drink Rs {limca_dr*person2}/-\n____________________  \n6. {person2} Special Meetha Paan Rs {meetha_p*person2}/-\n____________________  \nTotal Bill: Rs{bill} + Tax {tax} \n_______________\nGrand Total: {bill+tax}/-\n____________________  ")
                        else:
                            print("")
                            print("=============================")
                            print("********************Moving For Our Special Suggestion For You In Rice ****************")
                            b_plat=6000 
                            salim_dumba=4500 
                            icecream_falooda=1200   
                            gulabj=100
                            almond_milk=600
                            #for the purpose to calculate total price of gulab jamun
                            gulabj_per=person2*2  
                            fire_meetha_pan=150    
                            platter=person2//3.5
                            quantity=person2//2
                            #calculation For Bill
                            bill=(b_plat*platter)+(salim_dumba*quantity)+(icecream_falooda*person2)+(gulabj*gulabj_per)+(almond_milk*person2)+(fire_meetha_pan*person2)
                            tax=bill/10
                            print(f"Dear Customer! \nYour Order is confirmed and here\n1. {platter} Fresh Badshahi Platter \n____________________  \n2. Fresh Live {quantity} KG Salim Dumba\n____________________  \n3. {person2} Bowl Ice Cream Falooda\n____________________  \n4.{gulabj_per} Gulaab Jamun \n____________________ \n5.{person2} Almond Milk\n____________________  \n6. {person2} Special Fire Meetha Paan\n____________________ ")
                            print("==================================================================")
                            print(f"Dear Customer! \nYour Total Bill is: \n1. {platter} KG  Fresh Badshahi Platter Rs.{b_plat*platter}/-\n____________________   \n2. Fresh Live {quantity} KG Salim Dumba Rs {salim_dumba*quantity}/-\n____________________  \n3. {person2} Bowl Ice Cream Falooda Rs {icecream_falooda*person2}/-\n____________________  \n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/-\n____________________  \n5.{person2} Almond Milk Rs {almond_milk*person2}/-\n____________________  \n6. {person2} Special Fire Meetha Paan Rs {fire_meetha_pan*person2}/-\n____________________  \nTotal Bill: Rs{bill} + Tax {tax} \n_______________\nGrand Total: {bill+tax}/-\n____________________  ")
                    else:
                        typ=int(input("What Do You Want To Eat?\n1. Classic Beef Special Daigh Biryani \n2. Or Type Anything For Something Special In Rice In Beef\nSelect Any Specific Of Above:"))
                        print("===============================================")
                        if typ == 1:
                            print("********************Classic Beef Special Daigh Biryani Lover ****************")
                            classic_daig=1947 #16500
                            behari_kabab=1408 #15000
                            kunaffa=1499  #11250
                            gulabj=78  
                            #for the purpose to calculate total price of gulab jamun
                            gulabj_per=person2*2  #14000
                            special_dr=547   #9000
                            meetha_p=73# 1500
                            daig_kg=person2//3
                            quantity=person2//2
                            #calculation For Bill
                            bill=(classic_daig*daig_kg)+(behari_kabab*person2*2)+(kunaffa*quantity)+(gulabj*gulabj_per)+(special_dr*person2)+(meetha_p*person2)
                            tax=bill//14
                            print(f"Dear Customer! \nYour Order is here confirmed and here\n1. {daig_kg} KG Classic Beef Special Daigh Biryani Lover\n____________________  \n2. Fresh Live {person2*2} Behari Kabab\n____________________  \n3. {quantity} Kunafah\n____________________  \n4.{gulabj_per} Gulaab Jamun \n____________________ \n5.{person2} Special Drink\n____________________  \n6. {person2} Special Meetha Paan\n____________________ ")
                            print(f"Dear Customer! \nYour Total Bill is: \n1. {daig_kg} KG Fresh Classic Beef Special Daigh Biryani Rs.{classic_daig*daig_kg}/-\n____________________   \n2. Fresh Live {person2*2} Bihari Kabab  Rs {behari_kabab*(person2*2)}/-\n____________________  \n3. {quantity} Kunafah Rs {kunaffa*quantity}/-\n____________________  \n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/-\n____________________  \n5.{person2} Special Drink Rs {special_dr*person2}/-\n____________________  \n6. {person2} Special Meetha Paan Rs {meetha_p*person2}/-\n____________________  \nTotal Bill: Rs{bill} + Tax {tax} \nGrand Total: {bill+tax}/-\n____________________  ")
                        
                        else:
                            print("")
                            print("=============================")
                            print("********************Moving For Our Special Suggestion For You In Rice With Beef****************")
                            beef_hyder_daigh=4359 
                            beef_baloochi_tikka=2569
                            
                            icecream_falooda=1200
                            gulabj=100
                            almond_milk=600
                            #for the purpose to calculate total price of gulab jamun
                            gulabj_per=person2*2  
                            fire_meetha_pan=150    
                            beef_daig=person2//3.5
                            quantity=person2//2
                            #calculation For Bill
                            bill=(beef_hyder_daigh*beef_daig)+(beef_baloochi_tikka*quantity)+(icecream_falooda*person2)+(gulabj*gulabj_per)+(almond_milk*person2)+(fire_meetha_pan*person2)
                            tax=bill/10
                            print(f"Dear Customer! \nYour Order is confirmed and here\n1. {beef_daig} Fresh Beef Hyderabadi Daig Biryani \n____________________  \n2. Fresh Live {quantity} Beef Balochi Tikka\n____________________  \n3. {person2} Bowl Ice Cream Falooda\n____________________  \n4.{gulabj_per} Gulaab Jamun \n____________________ \n5.{person2} Almond Milk\n____________________  \n6. {person2} Special Fire Meetha Paan\n____________________ ")
                            print("==================================================================")
                            print(f"Dear Customer! \nYour Total Bill is: \n1. {beef_daig}  Fresh Beef Hyderabadi Daig Biryani Rs.{beef_hyder_daigh*beef_daig}/-\n____________________   \n2. Fresh Live {quantity} Beef Balochi Tikka Rs {beef_baloochi_tikka*quantity}/-\n____________________  \n3. {person2} Bowl Ice Cream Falooda Rs {icecream_falooda*person2}/-\n____________________  \n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/-\n____________________  \n5.{person2} Almond Milk Rs {almond_milk*person2}/-\n____________________  \n6. {person2} Special Fire Meetha Paan Rs {fire_meetha_pan*person2}/-\n____________________  \nTotal Bill: Rs{bill} + Tax {tax} \n_______________\nGrand Total: {bill+tax}/-\n____________________  ")
                        
                elif time == 2: #weekly
                    varient=int(input("Do You Want:\n1.Chicken \n2.Mutton(Most Recommended ) \n3.Beef (Most Recommended)(Type Anything For Beef),:"))
                    print("===============================================")
                    if varient ==1:
                        typ=int(input("What Do You Want To Eat?\n1. Biryani \n2. Chinese \n3. Fast Food\n4. Or Type Anything For Something Special\nSelect Any Specific Of Above:"))
                        print("===============================================")
                        if typ == 1:
                            print("********************Moving For Biryani Lover ****************")
                            bir_daigh=2200 #16500
                            sajji_per=2000 #15000
                            kunaffa=1500   #11250
                            gulabj=100     
                            #for the purpose to calculate total price of gulab jamun
                            gulabj_per=person2*2  #14000
                            special_dr=600   #9000
                            meetha_p=100     # 1500
                            daigh_kg=person2//3
                            quantity=person2//2
                            #calculation For Bill
                            bill=(bir_daigh*daigh_kg)+(sajji_per*quantity)+(kunaffa*quantity)+(gulabj*gulabj_per)+(special_dr*person2)+(meetha_p*person2)
                            tax=bill/10
                            print(f"Dear Customer! \nYour Order is here confirmed and here\n1. {daigh_kg} KG Fresh Live Chicken Bombay Biryaani\n____________________  \n2. Fresh Live {quantity} Sajji\n____________________  \n3. {quantity} Kunafah\n____________________  \n4.{gulabj_per} Gulaab Jamun \n____________________ \n5.{person2} Special Drink\n____________________  \n6. {person2} Special Meetha Paan\n____________________ ")
                            print(f"Dear Customer! \nYour Total Bill is: \n1. {daigh_kg}KG Fresh Live Chicken Bombay Biryaani Rs.{bir_daigh*daigh_kg}/-\n____________________   \n2. Fresh Live {quantity} Sajji Rs {sajji_per*quantity}/-\n____________________  \n3. {quantity} Kunafah Rs {kunaffa*quantity}/-\n____________________  \n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/-\n____________________  \n5.{person2} Special Drink Rs {special_dr*person2}/-\n____________________  \n6. {person2} Special Meetha Paan Rs {meetha_p*person2}/-\n____________________  \nTotal Bill: Rs{bill} + Tax {tax} \nGrand Total: {bill+tax}/-\n____________________  ")
                        elif typ == 2:
                            print("=============================")
                            print("********************Moving For Chinese Food Lover ****************")
                            chinese_plat=2200 #16500
                            chinese_bowl=1500 #15000
                            lotus_tofu=1500   #meetha 
                            dumplings=200
                            bubble_tea=600
                            moon_cake=100
                            dumplings_per=person2*2
                            chinese_per=person2//2
                            quantity=person2//2
                            #calculation For Bill
                            bill=(chinese_plat*chinese_per)+(chinese_bowl*person2)+(lotus_tofu*person2)+(dumplings*dumplings_per)+(bubble_tea*person2)+(moon_cake*person2)
                            tax=bill/10
                            print(f"Dear Customer! \nYour Order is confirmed and here\n1. {chinese_per}  Fresh Live Jumbo Platter Of Chinese Cuisine\n____________________  \n2. Fresh Live {person2} Chinese Bowl Of Chowmin\n____________________  \n3. {person2} Lotus Tofu\n____________________  \n4.{dumplings_per} Dumplings \n____________________ \n5.{person2} Bubble Tea\n____________________  \n6. {person2} Special Moon Cake\n____________________ ")
                            print("==================================================================")
                            print(f"Dear Customer! \nYour Total Bill is: \n1. {chinese_per} Fresh Live Jumbo Platter Of Chinese Cuisine Rs.{chinese_plat*chinese_per}/-\n____________________   \n2. Fresh Live {person2} Chinese Bowl Rs {chinese_bowl*person2}/-\n____________________  \n3.  {person2} Lotus Tofu Rs {lotus_tofu*person2}/-\n____________________  \n4.{dumplings_per} Dumplings Rs {dumplings*dumplings_per}/-\n____________________  \n5.{person2} Bubble Tea Rs {bubble_tea*person2}/-\n____________________  \n6. {person2} Special Moon Cake Rs {moon_cake*person2}/-\n____________________  \nTotal Bill: Rs{bill} + Tax {tax} \n_______________\nGrand Total: {bill+tax}/-\n____________________  ")
                        elif typ == 3:
                            print("=============================")
                            print("********************Moving For Hyderabadi Biryani Lover ****************")
                            bir_daigh=2200 #16500
                            qeema_per=1500 #15000
                            rabri=1500   #11250
                            gulabj=100     
                            #for the purpose to calculate total price of gulab jamun
                            gulabj_per=person2*2  #14000
                            limca_dr=600   #9000
                            meetha_p=100     # 1500
                            daigh_kg=person2//3
                            quantity=person2//2
                            #calculation For Bill
                            bill=(bir_daigh*daigh_kg)+(qeema_per*quantity)+(rabri*person2)+(gulabj*gulabj_per)+(limca_dr*person2)+(meetha_p*person2)
                            tax=bill/10
                            print(f"Dear Customer! \nYour Order is confirmed and here\n1. {daigh_kg} KG Fresh Live Chicken Hyderabadi Biryaani\n____________________  \n2. Fresh Live {quantity} KG Dum Qeema\n____________________  \n3. {quantity} KG rabri\n____________________  \n4.{gulabj_per} Gulaab Jamun \n____________________ \n5.{person2} Limca Drink\n____________________  \n6. {person2} Special Meetha Paan\n____________________ ")
                            print("==================================================================")
                            print(f"Dear Customer! \nYour Total Bill is: \n1. {daigh_kg} KG Fresh Live Chicken Hyderabadi Biryaani Rs.{bir_daigh*daigh_kg}/-\n____________________   \n2. Fresh Live {quantity} KG Dum Qeema Rs {qeema_per*quantity}/-\n____________________  \n3. {quantity} KG  Rabri Rs {rabri*quantity}/-\n____________________  \n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/-\n____________________  \n5.{person2} Limca Drink Rs {limca_dr*person2}/-\n____________________  \n6. {person2} Special Meetha Paan Rs {meetha_p*person2}/-\n____________________  \nTotal Bill: Rs{bill} + Tax {tax} \n_______________\nGrand Total: {bill+tax}/-\n____________________  ")
                        else:
                            print("")
                            print("=============================")
                            print("********************Moving For Our Special Suggestion For You In Rice ****************")
                            madbi_plat=6000 
                            dumpukht=2500 
                            icecream_falooda=1200   
                            gulabj=100
                            almond_milk=600
                            #for the purpose to calculate total price of gulab jamun
                            gulabj_per=person2*2  
                            fire_meetha_pan=150    
                            platter=person2//3.5
                            quantity=person2//2
                            #calculation For Bill
                            bill=(madbi_plat*platter)+(dumpukht*quantity)+(icecream_falooda*person2)+(gulabj*gulabj_per)+(almond_milk*person2)+(fire_meetha_pan*person2)
                            tax=bill/10
                            print(f"Dear Customer! \nYour Order is confirmed and here\n1. {platter} Fresh Afghani Special Platter \n____________________  \n2. Fresh Live {quantity} KG DumPukht\n____________________  \n3. {person2} Bowl Ice Cream Falooda\n____________________  \n4.{gulabj_per} Gulaab Jamun \n____________________ \n5.{person2} Almond Milk\n____________________  \n6. {person2} Special Fire Meetha Paan\n____________________ ")
                            print("==================================================================")
                            print(f"Dear Customer! \nYour Total Bill is: \n1. {platter}  Fresh Afghani Special Platter Rs.{madbi_plat*platter}/-\n____________________   \n2. Fresh Live {quantity} KG DumPukht Rs {dumpukht*quantity}/-\n____________________  \n3. {person2} Bowl Ice Cream Falooda Rs {icecream_falooda*person2}/-\n____________________  \n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/-\n____________________  \n5.{person2} Almond Milk Rs {almond_milk*person2}/-\n____________________  \n6. {person2} Special Fire Meetha Paan Rs {fire_meetha_pan*person2}/-\n____________________  \nTotal Bill: Rs{bill} + Tax {tax} \n_______________\nGrand Total: {bill+tax}/-\n____________________  ")
                    elif varient == 2:
                        typ=int(input("What Do You Want To Eat?\n1. Moroccan Lamb \n2. Classic Dumpukht Mutton Biryani \n3. Mutton Kabuli Pilao\n4. Or Type Anything For Something Special In Rice\nSelect Any Specific Of Above:"))
                        print("===============================================")
                        if typ == 1:
                            print("********************Moving For Moroccan Lamp Lover ****************")
                            lamb_rice=3000 #16500
                            saalam_lamb=3000 #15000
                            kunaffa=1500   #11250
                            gulabj=100     
                            #for the purpose to calculate total price of gulab jamun
                            gulabj_per=person2*2  #14000
                            special_dr=600   #9000
                            meetha_p=100# 1500
                            
                            platter_kg=person2//3
                            quantity=person2//2
                            #calculation For Bill
                            bill=(lamb_rice*platter_kg)+(saalam_lamb*quantity)+(kunaffa*quantity)+(gulabj*gulabj_per)+(special_dr*person2)+(meetha_p*person2)
                            tax=bill/10
                            print(f"Dear Customer! \nYour Order is here confirmed and here\n1. {Lamb_rice} KG Fresh Live Moroccon Lamb \n____________________  \n2. Fresh Live {quantity} Saalam Lamb\n____________________  \n3. {quantity} Kunafah\n____________________  \n4.{gulabj_per} Gulaab Jamun \n____________________ \n5.{person2} Special Drink\n____________________  \n6. {person2} Special Meetha Paan\n____________________ ")
                            print(f"Dear Customer! \nYour Total Bill is: \n1. {platter_kg} KG Fresh Live Moroccon Lamb Rs.{lamb_rice*platter_kg}/-\n____________________   \n2. Fresh Live {quantity} Saalam Lamb Rs {saalam_lamb*quantity}/-\n____________________  \n3. {quantity} Kunafah Rs {kunaffa*quantity}/-\n____________________  \n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/-\n____________________  \n5.{person2} Special Drink Rs {special_dr*person2}/-\n____________________  \n6. {person2} Special Meetha Paan Rs {meetha_p*person2}/-\n____________________  \nTotal Bill: Rs{bill} + Tax {tax} \nGrand Total: {bill+tax}/-\n____________________  ")
                        elif typ == 2:
                            print("=============================")
                            print("********************Moving For Classic Dumpukht Mutton Biryani Lover ****************")
                            mutton_bir=4500 #16500
                            mutton_rosh=3500 #15000
                            kunaffa=1500   #11250
                            gulabj=100     
                            #for the purpose to calculate total price of gulab jamun
                            gulabj_per=person2*2  #14000
                            limca_dr=600   #9000
                            meetha_p=100     # 1500
                            mutton_kg=person2//3
                            quantity=person2//2
                            #calculation For Bill
                            bill=(mutton_bir*mutton_kg)+(mutton_rosh*mutton_kg)+(kunaffa*quantity)+(gulabj*gulabj_per)+(limca_dr*person2)+(meetha_p*person2)
                            tax=bill/10
                            print(f"Dear Customer! \nYour Order is confirmed and here\n1. {mutton_kg} KG Fresh Live Classic Dumpukht Mutton Biryani\n____________________  \n2. Fresh Live {mutton_kg} Mutton Rosh\n____________________  \n3. {quantity} Kunafah\n____________________  \n4.{gulabj_per} Gulaab Jamun \n____________________ \n5.{person2} Limca Drink\n____________________  \n6. {person2} Special Meetha Paan\n____________________ ")
                            print("==================================================================")
                            print(f"Dear Customer! \nYour Total Bill is: \n1. {mutton_kg} KG Fresh Live Classic Dumpukht Mutton Biryani Rs.{mutton_kg*mutton_bir}/-\n____________________   \n2. Fresh Live {mutton_kg} KG Mutton Rosh Rs {mutton_rosh*mutton_kg}/-\n____________________  \n3. {quantity} Kunafah Rs {kunaffa*quantity}/-\n____________________  \n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/-\n____________________  \n5.{person2} Limca Drink Rs {limca_dr*person2}/-\n____________________  \n6. {person2} Special Meetha Paan Rs {meetha_p*person2}/-\n____________________  \nTotal Bill: Rs{bill} + Tax {tax} \n_______________\nGrand Total: {bill+tax}/-\n____________________  ")
                        elif typ == 3:
                            print("=============================")
                            print("********************Moving For Mutton Kabuli Pilao Lover ****************")
                            kabuli_pilao=3000 #16500
                            mutton_peti_kabab=2000 #15000
                            rabri=1500   #11250
                            gulabj=100     
                            #for the purpose to calculate total price of gulab jamun
                            gulabj_per=person2*2  #14000
                            limca_dr=600   #9000
                            meetha_p=100     # 1500
                            kabuli_kg=person2//3
                            quantity=person2//2
                            #calculation For Bill
                            bill=(kabuli_pilao*kabuli_kg)+(mutton_peti_kabab*person2)+(rabri*mutton_kg)+(gulabj*gulabj_per)+(limca_dr*person2)+(meetha_p*person2)
                            tax=bill/10
                            print(f"Dear Customer! \nYour Order is confirmed and here\n1. {kabuli_kg} KG Fresh Live Kabuli Mutton Pilao\n____________________  \n2. Fresh Live {person2} Mutton Peti Kabab\n____________________  \n3. {quantity} KG rabri\n____________________  \n4.{gulabj_per} Gulaab Jamun \n____________________ \n5.{person2} Limca Drink\n____________________  \n6. {person2} Special Meetha Paan\n____________________ ")
                            print("==================================================================")
                            print(f"Dear Customer! \nYour Total Bill is: \n1. {mutton_kg} KG Fresh Live kabuli Mutton Pilao Rs.{kabuli_pilao*mutton_kg}/-\n____________________   \n2. Fresh Live {person2} Mutton Peti Kabab Rs {mutton_peti_kabab*person2}/-\n____________________  \n3. {quantity} KG  Rabri Rs {rabri*quantity}/-\n____________________  \n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/-\n____________________  \n5.{person2} Limca Drink Rs {limca_dr*person2}/-\n____________________  \n6. {person2} Special Meetha Paan Rs {meetha_p*person2}/-\n____________________  \nTotal Bill: Rs{bill} + Tax {tax} \n_______________\nGrand Total: {bill+tax}/-\n____________________  ")
                        else:
                            print("")
                            print("=============================")
                            print("********************Moving For Our Special Suggestion For You In Rice ****************")
                            b_plat=6000 
                            salim_dumba=4500 
                            icecream_falooda=1200   
                            gulabj=100
                            almond_milk=600
                            #for the purpose to calculate total price of gulab jamun
                            gulabj_per=person2*2  
                            fire_meetha_pan=150    
                            platter=person2//3.5
                            quantity=person2//2
                            #calculation For Bill
                            bill=(b_plat*platter)+(salim_dumba*quantity)+(icecream_falooda*person2)+(gulabj*gulabj_per)+(almond_milk*person2)+(fire_meetha_pan*person2)
                            tax=bill/10
                            print(f"Dear Customer! \nYour Order is confirmed and here\n1. {platter} Fresh Badshahi Platter \n____________________  \n2. Fresh Live {quantity} KG Salim Dumba\n____________________  \n3. {person2} Bowl Ice Cream Falooda\n____________________  \n4.{gulabj_per} Gulaab Jamun \n____________________ \n5.{person2} Almond Milk\n____________________  \n6. {person2} Special Fire Meetha Paan\n____________________ ")
                            print("==================================================================")
                            print(f"Dear Customer! \nYour Total Bill is: \n1. {platter} KG  Fresh Badshahi Platter Rs.{b_plat*platter}/-\n____________________   \n2. Fresh Live {quantity} KG Salim Dumba Rs {salim_dumba*quantity}/-\n____________________  \n3. {person2} Bowl Ice Cream Falooda Rs {icecream_falooda*person2}/-\n____________________  \n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/-\n____________________  \n5.{person2} Almond Milk Rs {almond_milk*person2}/-\n____________________  \n6. {person2} Special Fire Meetha Paan Rs {fire_meetha_pan*person2}/-\n____________________  \nTotal Bill: Rs{bill} + Tax {tax} \n_______________\nGrand Total: {bill+tax}/-\n____________________  ")
                    else:
                        typ=int(input("What Do You Want To Eat?\n1. Classic Beef Special Daigh Biryani \n2. Or Type Anything For Something Special In Rice In Beef\nSelect Any Specific Of Above:"))
                        print("===============================================")
                        if typ == 1:
                            print("********************Classic Beef Special Daigh Biryani Lover ****************")
                            classic_daig=1947 #16500
                            behari_kabab=1408 #15000
                            kunaffa=1499  #11250
                            gulabj=78  
                            #for the purpose to calculate total price of gulab jamun
                            gulabj_per=person2*2  #14000
                            special_dr=547   #9000
                            meetha_p=73# 1500
                            daig_kg=person2//3
                            quantity=person2//2
                            #calculation For Bill
                            bill=(classic_daig*daig_kg)+(behari_kabab*person2*2)+(kunaffa*quantity)+(gulabj*gulabj_per)+(special_dr*person2)+(meetha_p*person2)
                            tax=bill//14
                            print(f"Dear Customer! \nYour Order is here confirmed and here\n1. {daig_kg} KG Classic Beef Special Daigh Biryani Lover\n____________________  \n2. Fresh Live {person2*2} Behari Kabab\n____________________  \n3. {quantity} Kunafah\n____________________  \n4.{gulabj_per} Gulaab Jamun \n____________________ \n5.{person2} Special Drink\n____________________  \n6. {person2} Special Meetha Paan\n____________________ ")
                            print(f"Dear Customer! \nYour Total Bill is: \n1. {daig_kg} KG Fresh Classic Beef Special Daigh Biryani Rs.{classic_daig*daig_kg}/-\n____________________   \n2. Fresh Live {person2*2} Bihari Kabab  Rs {behari_kabab*(person2*2)}/-\n____________________  \n3. {quantity} Kunafah Rs {kunaffa*quantity}/-\n____________________  \n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/-\n____________________  \n5.{person2} Special Drink Rs {special_dr*person2}/-\n____________________  \n6. {person2} Special Meetha Paan Rs {meetha_p*person2}/-\n____________________  \nTotal Bill: Rs{bill} + Tax {tax} \nGrand Total: {bill+tax}/-\n____________________  ")
                        
                        else:
                            print("")
                            print("=============================")
                            print("********************Moving For Our Special Suggestion For You In Rice With Beef****************")
                            beef_hyder_daigh=4359 
                            beef_baloochi_tikka=2569 
                            icecream_falooda=1200
                            gulabj=100
                            almond_milk=600
                            #for the purpose to calculate total price of gulab jamun
                            gulabj_per=person2*2  
                            fire_meetha_pan=150    
                            beef_daig=person2//3.5
                            quantity=person2//2
                            #calculation For Bill
                            bill=(beef_hyder_daigh*beef_daig)+(beef_baloochi_tikka*quantity)+(icecream_falooda*person2)+(gulabj*gulabj_per)+(almond_milk*person2)+(fire_meetha_pan*person2)
                            tax=bill/10
                            print(f"Dear Customer! \nYour Order is confirmed and here\n1. {beef_daig} Fresh Beef Hyderabadi Daig Biryani \n____________________  \n2. Fresh Live {quantity} Beef Balochi Tikka\n____________________  \n3. {person2} Bowl Ice Cream Falooda\n____________________  \n4.{gulabj_per} Gulaab Jamun \n____________________ \n5.{person2} Almond Milk\n____________________  \n6. {person2} Special Fire Meetha Paan\n____________________ ")
                            print("==================================================================")
                            print(f"Dear Customer! \nYour Total Bill is: \n1. {beef_daig}  Fresh Beef Hyderabadi Daig Biryani Rs.{beef_hyder_daigh*beef_daig}/-\n____________________   \n2. Fresh Live {quantity} Beef Balochi Tikka Rs {beef_baloochi_tikka*quantity}/-\n____________________  \n3. {person2} Bowl Ice Cream Falooda Rs {icecream_falooda*person2}/-\n____________________  \n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/-\n____________________  \n5.{person2} Almond Milk Rs {almond_milk*person2}/-\n____________________  \n6. {person2} Special Fire Meetha Paan Rs {fire_meetha_pan*person2}/-\n____________________  \nTotal Bill: Rs{bill} + Tax {tax} \n_______________\nGrand Total: {bill+tax}/-\n____________________  ")
                elif time == 3:
                    print("")
                else:
                    print("")
            elif fav == 2:
                print("")
            elif fav == 3:
                print("")
            else:
                print("Wrong Input.Please Try Again.")
                fav=int(input("What You Eat Commonly?\n1. Biryani \n2.Karahi \n3. BBQ \nSelect Any Of Above?:"))
                if fav ==1:
                    print("")
                elif fav==2:
                    print("")
                elif fav==3:
                    print("")
                else:
                    print("Wrong Input , You Have Exceed Chance Of Choosing.")
        else:
            print("")
    else:
        print("Increase Your Budget As Your Count Of Person Is Huge!.")
        print("Thank You For Visiting.")
elif person==2:
    print("")
elif person==3:
    print("")
elif person==4:
    print("")
else:
    print("")

