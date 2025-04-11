osalejad = []
punktid = []
n = int(input("Mitu osalejat? "))
for i in range(n):
    nimi=input(f"Sisesta osaleja {i + 1} nimi: ")
    punkt =int(input(f"Sisesta osaleja {i + 1} punktid: "))
    osalejad.append(nimi)
    punktid.append(punkt)

while True:
    print("1. Näita osalejaid, kes pääsesid edasi")
    print("2. Sorteeri osalejad tähestiku järgi")
    print("3. Näita osalejaid madalaimate punktidega")
    print("4. Näita keskmist punktisummat")
    print("5. Välju")
    valik = input("Vali tegevus (1-5): ")
    if valik == "1":
        miinimum_punktid = int(input("Sisesta miinimum punktide arv edasipääsuks: "))
        edasipääsenud = []
        for i in range(n):
            if punktid[i] >= miinimum_punktid:
                edasipääsenud.append(osalejad[i])
            
        if len(edasipääsenud) > 0:
            print("Edasipääsenud osalejad:", ", ".join(edasipääsenud))
        else:
            print("Ühtegi osalejat ei pääsenud edasi.")
    elif valik == "2":
        sorteeritud_osalejad = []
        for i in range(n):
            sorteeritud_osalejad.append((osalejad[i], punktid[i]))
            sorteeritud_osalejad.sort() 
            print("Osalejad tähestiku järjekorras:")
        for item in sorteeritud_osalejad:
            print(f"{item[0]}: {item[1]}")
    elif valik == "3":
        punktide_osalejad = []
        for i in range(n):
            punktide_osalejad.append((punktid[i], osalejad[i]))
            punktide_osalejad.sort()
            print("Osalejad madalaimate punktidega:")
        for i in range(3):
            if i < len(punktide_osalejad):
                print(f"{punktide_osalejad[i][1]}: {punktide_osalejad[i][0]}")

    elif valik == "4":
        summa = 0

        for punkt in punktid:
            summa += punkt
            keskmine = summa / n
            print(f"Keskmine punktisumma: {keskmine}")
    elif valik == "5":
        print("Väljutakse...")
        break
    else:
        print("Vigane valik. Palun proovi uuesti.")
