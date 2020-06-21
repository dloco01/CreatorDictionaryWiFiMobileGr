from tqdm import tqdm

phoneMobileCos = 6970000000
phoneMobileVod = 6940000000
phoneMobileWind = 693000000
phoneStable = 2000000000
phoneMobilewhatUp = 6980000000

print("Plase Select For Dictionary Cracking Wifi\n ---- For Help Press 6 -----\n")
print("Press 1 For Cosmote Nubmer ")
print("Press 2 For Vodafon Nubmer")
print("Press 3 For Wind Nubmer")
print("Press 4 For Stable Nubmer")
print("Press 5 For Make your Numbers")
select = int(input("Plase Select a Number For make your Dictionary!: "))
if select > 4:
    maker = open("Dic_YourNumber.txt" , "a")
    yourSelectStart = int(input("Type you number to START! create Dictionary: "))
    yourSelectStop = int(input("Type you number to STOP! create Dictionary: "))
    pbar = tqdm(total=100)
    while not int(yourSelectStart) == yourSelectStop:
        pbar.update()
        yourSelectStart+=1
        maker.write(str(yourSelectStart) + "\n")
    print("Dictionary Success!")

if select == 1:
    maker = open("Dic_CosmPhon.txt" , "a")
    pbar = tqdm(total=100)
    while not int(phoneMobileCos) == 6979999999:
        pbar.update()
        phoneMobileCos+=1
        maker.write(str(phoneMobileCos)+ "\n")
    print("Dictionary Success!")
    
elif select == 2:
    pbar = tqdm(total=100)
    maker = open("Dic_VodPhon.txt" , "a")
    while not int(phoneMobileVod) == 6949999999:
        phoneMobileVod+=1
        pbar.update()
        maker.write(str(phoneMobileVod)+ "\n")
    print("Dictionary Success!")

elif select == 3:
    pbar = tqdm(total=100)
    maker = open("Dic_WindPhon.txt" , "a")
    while not int(phoneMobileWind) == 6939999999:
        pbar = tqdm(total=100)
        phoneMobileWind+=1
        pbar.update(1)
        maker.write(str(phoneMobileWind)+ "\n")
    print("Dictionary Success!")

elif select == 4:
    pbar = tqdm(total=100)
    maker = open("Dic_StablePhone.txt" , "a")
    while not int(phoneStable) == 2999999999:
        phoneStable+=1
        pbar.update()
        maker.write(str(phoneStable)+ "\n")
    print("Dictionary Success!")

elif select == 5:
    pbar = tqdm(total=100)
    maker = open("Dic_StablePhone.txt" , "a")
    while not int(phoneMobilewhatUp) == 6989999999:
        phoneMobilewhatUp+=1
        pbar.update()
        maker.write(str(phoneMobilewhatUp)+ "\n")
    print("Dictionary Success!")

elif select == 6:
    print("\t ----Help----")
    print("Cosmote number start to 697XXXXXXX")
    print("What'Up number start to 698XXXXXXX")
    print("Vodafon Number Start to 694XXXXXXX")
    print("Wind Number Start to 693XXXXXXX")
    print("Gia stathera Ellada to kathe meros exei ton dikotou kwdiko\n Eksartate apo to pou vriskeste 210 p.x Gia athina")
    print("Stin ellada einai sinithismeno na xrisimopioun airthmos stathelou tilefono\n eite kinitou gia kwdiko WiFi")
    print("Ama o ginitonas mas exei allaksai to ergostasiko kwdiko!")
    print("\t ----sample---- ")
    print("Type you number to start create Dictionary: 2662000000")
    print("Type you number to stop create Dictionary: 26620999999")
    print("\nXrisimopihste aircrack-ng")


else:
    print("Plase Type a Number 1-7!")
