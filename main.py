'''
NB  2023.03.20

Feladat :  Adj meg 5 tetszőleges számot és mentsd el egy változóba - input
            Generálj 5 egész számot 1 és 90 között mentsd el egy változóba a halmazt - random
            Hasonlítsd össze az inputtal bekért számokat a random generált számok halmazával
            Írd ki, hogy hány szám egyezett meg

'''
import random

print('-------- fogadás  --------')
# 5 tetszőleges szám bekérése a felhasználótól, 5x kér be számot.

input_szamok = []
for i in range(5):
    szam = int(input("Kérlek adj meg egy számot 0 és 90 között: "))
    if szam > 90 or szam < 1:   # a szám nem lehet 90-nél nagyobb és 1 nél kisebb
        print("HIBÁS fogadás")
        quit()  # hiba miatt kilép

#  add hozzá a fent megadott számokat az üres listához
    input_szamok.append(szam)

if len(input_szamok) != len(set(input_szamok)):
    print("HIBÁS fogadás: nem lehet két azonos szám a tippben.")
    quit()




# 5 véletlenszerű egész szám generálása 1 és 90 között
random_szamok = set()
while len(random_szamok) < 5:    #- megyszámolja az elemek számát és ismétli amíg 5 nem lesz
    random_szam = random.randint(1, 90)
    random_szamok.add(random_szam)  # hozzáadja a halmazhoz

# Bekért számok és generált számok összehasonlítása
talalt_szamok = set(input_szamok).intersection(random_szamok)  # a két halmaz metszetének meghatározása -intersection

print('-------- sorsolás  --------')
# Találatok kiírása
print("A te tipped :  ", input_szamok)
print("Generált számok: ", random_szamok)
print("Találatok: ", len(talalt_szamok))

if len(talalt_szamok) > 0 :    # a két halmaz metszetelemeinek száma
    print('Szerencséd volt! Van találat')
else :
    print('Nem nyertél !')