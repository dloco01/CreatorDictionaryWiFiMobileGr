from tqdm import tqdm

phoneMobileCos = 6970000000
phoneMobileVod = 6940000000
phoneMobileWind = 693000000
phoneStable = 2000000000
phoneMobileWhatUp = 6980000000

def banner():
    print("\t\t --- Create By DloCo01 CDWM ---")
    print("\t\t --- Forum Site Worksession.ddns.net ---")
    print("\t Plase Select For Dictionary Cracking Wifi\n\t\t ---- For Help Press 7 -----\n")
    print(" Press 1 For Cosmote Nubmer ")
    print(" Press 2 For Vodafon Nubmer")
    print(" Press 3 For Wind Nubmer")
    print(" Press 4 For Stable Nubmer")
    print(" Press 6 For Make your Numbers")

def helper():
    print("\t\t ----Help----")
    print(" \nCosmote number start to 697XXXXXXX")
    print(" What'Up number start to 698XXXXXXX")
    print(" Vodafon Number Start to 694XXXXXXX")
    print(" Wind Number Start to 693XXXXXXX")
    print("\n Gia stathera Ellada to kathe meros exei ton dikotou kwdiko\n Eksartate apo to pou vriskeste 210 p.x Gia athina")
    print("\n Stin ellada einai sinithismeno na xrisimopioun airthmos stathelou\n tilefono eite kinitou gia kwdiko WiFi\n")
    print("\t\t ----sample---- ")
    print("\t ---How to make your Dictionary---")
    print(" Type you number to start create Dictionary: 2662000000")
    print(" Type you number to stop create Dictionary: 26620999999\n")
    print("\n Ama o ginitonas mas exei allaksai to ergostasiko kwdiko!")
    print(" Xrisimopihste aircrack-ng")
    close = input("\nPress any key... for Close!")

def creater(phone,stop,nameFile):
    maker = open(nameFile, "a")
    pbar = tqdm(total=100)
    phone-=1
    while not int(phone) == stop:
        pbar.update()
        phone+=1
        maker.write(str(phone)+ "\n")
    print("\n\tDictionary Success!")

def MyCreater(start,stop,nameFile):
    maker = open(nameFile, "a")
    pbar = tqdm(total=100)
    start-=1
    while not int(start) == stop:
        pbar.update()
        start+=1
        maker.write(str(start) + "\n")
    print("\n\tDictionary Success!")

banner()
select = int(input(" Plase Select a Number For make your Dictionary!: "))
 
if select == 1:
    stop = 6979999999
    name = "CosmotePass.txt"
    creater(phoneMobileCos,stop,name)
    
elif select == 2:
    stop = 6949999999
    name = "VodafonePass.txt"
    creater(phoneMobileVod,stop,name)

elif select == 3:
    stop = 6939999999
    name = "WindPass.txt"
    creater(phoneMobileWind,stop,name)

elif select == 4:
    stop = 6989999999
    name = "WhatUpPass.txt"
    creater(phoneMobileWhatUp,stop,name)

elif select == 5:
    stop = 2999999999
    name = "WhatUpPass.txt"
    creater(phoneStable,stop,name)

elif select == 6:
    start = int(input("Type you number to START! create Dictionary: "))
    stop = int(input("Type you number to STOP! create Dictionary: "))
    name = "MyPass.txt"
    MyCreater(start,stop,name)

elif select == 7:
    helper()

else:
    print("Plase Type a Number 1-7!")
    helper()
