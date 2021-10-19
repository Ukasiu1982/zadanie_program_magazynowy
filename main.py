import sys

saldo = 0
magazyn = {}
historia = []

while True:
    komenda = []
    akcja = input()
    if akcja == 'stop':
        break
    elif akcja == "saldo":
        komenda.append('saldo')
        komenda.append(input())
        komenda.append(input())
        historia.append(komenda)
    elif akcja == "zakup":
        komenda.append('zakup')
        komenda.append(input())
        komenda.append(input())
        komenda.append(input())
        historia.append(komenda)
    elif akcja == "sprzedaz":
        komenda.append('sprzedaz')
        komenda.append(input())
        komenda.append(input())
        komenda.append(input())
        historia.append(komenda)
    else:
        print('Niedozwolona akcja')
        break

komenda = sys.argv[1:]
historia.append(komenda)

for komenda in historia:
    for x in komenda:
        print(x)
for akcja in komenda:
    print(akcja)

for komenda in historia:
    akcja = komenda[0]
    if akcja == 'saldo':
        saldo += int(komenda[1])
    elif akcja =='zakup':
        produkt = komenda[1]
        cena = int(komenda[2])
        ilosc = int(komenda[3])
        if saldo >= cena*ilosc:
            saldo -= ilosc * cena
            if magazyn.get(produkt):
                magazyn[produkt] += ilosc
            else:
                magazyn[produkt] = ilosc
        else:
            print('nie mozna kupic')
            break
    elif akcja == 'sprzedaz':
        produkt = komenda[1]
        cena = int(komenda[2])
        ilosc = int(komenda[3])
        if magazyn.get(produkt) and magazyn.get(produkt) >= ilosc:
            saldo += ilosc * cena
            magazyn[produkt] -= ilosc
        else:
            print('za malo produktow do transkacji')
            break
    elif akcja == 'konto':
        print('stan konta:', saldo)
    elif akcja == 'magazyn':
        print(magazyn)
        for produkt in komenda[1:]:
            print(produkt, ":", magazyn.get(produkt, 0))
        # print('stan magazynu:', magazyn)
    elif akcja == 'przeglad':
        od = int(komenda[1])
        do = int(komenda[2])
        print(historia[od:do])

