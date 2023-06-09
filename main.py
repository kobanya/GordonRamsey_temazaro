# Nagy Béla 2023-05-15   Témazáró vizsga feladat

import magyar  # sortörés, ékezetes abc-be rendezés, kerekítés
def beolvasas():  # a szükséges adatállomány beolvasása
    with open('GordonRamsayRestorants.csv', encoding='utf-8') as f:
        lines = f.readlines()  # sorok beolvasása
        fejlec = lines[0]  # a fejléc listába mentése, ez nem feladat
        sorok = [line.strip().split('\t') for line in lines[1:]]  # A sorokat az 1-es indextől feldarabolom, tabulátorral
        print(f"1. feladat : Beolvasás ... készen van! ({len(sorok)} rekord)")  # kiírom a minta szerint, nincs behúzás
        return sorok

def mentes_fajlba():   # formázott fájlba mentée

    with open('adatok.txt', 'w', encoding='utf-8') as f:
        f.write(f"1. feladat : Beolvasás ... készen van! ({len(sorok)} rekord)\n")
        f.write(f'2. feladat: \tGordon Ramsey {len(sorok)} étteremmel került kapcsolatba.\n')
        f.write(f"3. feladat: \tJelenleg {muvekodo_ettermek_szama} étterem működik.\n")
        f.write(f"4. feladat: \tAz éttermek {kerekitett_arany:.0f} %-a zárt be\n")
        f.write("5. feladat: \tMichelin-csillagot már kaptak az alábbi éttermek:\n")
        f.write('\n'.join([f"\t\t{sor[0]:40.40} \t {sor[1]}" for sor in sorok if int(sor[5]) > 0]))
        f.write("\n6. feladat: \tLegkevésbé sikeres éttermek adatai:\n")
        f.write('\n'.join(eredmeny))
        f.write("\n7. feladat: \tA jelenleg is működő éttermek közül a legtöbb csillaga a következő(k)nek van:\n")
        f.write('\n'.join(legjobb_ettermek_kimenet))
        f.write("\n8. feladat: \tGordon Ramsey a következő országokban nyitott éttermeket:\n")
        f.write(formazott)
        f.write("\n9. feladat: \tÚjranyitott éttermek:\n")
        f.write('\n'.join(ujranyitott_ettermek_kimenet))
        return

def mentes_menu():  # a mentés menü  létrehozása, hibakezeléssel
    print('--------------------------------------------------------------------------')
    mentes = input("Szeretné fájlba menteni az adatokat? 1-igen, 2-nem: ")

    while mentes not in ["1", "2"]:
        mentes = input("Szeretné fájlba menteni az adatokat? 1-igen, 2-nem: ")

    if mentes == "2":
        print('Mentés nélkül kilépek.')

    elif mentes == "1":
        mentes_fajlba()
        print('Az adatokat elmentettem! Nyissa meg az adatok.txt fájlt')

sorok = beolvasas()



# 2.Jelezze ki, összesen hány étteremmel került GR kapcsolatba!
print(f'2. feladat: \tGordon Ramsey {len(sorok)} étteremmel került kapcolatba.')  # egy behúzással kiírva a minta serint

# 3.Írja ki a jelenleg is működő éttermek számát!
aktualis_ev = 2023  # az aktuális év
muvekodo_ettermek_szama = 0  # változó létrehozása

for sor in sorok[1:]:  # A fejléc sort kihagyjuk
    if sor[4] == '0' or int(sor[4]) > aktualis_ev:  # Nem zárt be, vagy az aktuális év után zárt be
        muvekodo_ettermek_szama += 1  # a számláló megnövelése egyel
print(f"3. feladat: \tJelenleg  {muvekodo_ettermek_szama} étterem működik.")

# 4. Számolja ki, hány százalékuk zárt be az adatfelvétel időpontjáig!
osszes_ettermek_szama = len(sorok) - 1  # A fejléc sort kihagyjuk
zaras_arany = (osszes_ettermek_szama - muvekodo_ettermek_szama) / osszes_ettermek_szama * 100
kerekitett_arany = magyar.fel_kerekit(zaras_arany)# Az arány kiszámítása
print(f"4. feladat: \tAz éttermek {kerekitett_arany:.0f} %-a zárt be")

# 5.Írja ki azokat az éttermeket és városaikat, amelyek kaptak már Michelin-csillagot!
print(f"5. feladat: \tMichlein-csillagot már kaptak az alábbi éttermek:")
for sor in sorok:
    if int(sor[5]) > 0:  # Ha legalább egy Michelin-csillaguk van
        print(f"\t\t{sor[0]:40.40} \t {sor[1]}")  # 40 karakter fenntartott hely

# 6. Melyik éttermek voltak a legkevésbé sikeresek (nem kaptak csillagot és a legrövidebb ideig voltak nyitva)?
print("6. feladat: \tLegkevésbé sikeres éttermek adatai:")
legkevesbe_sikeresek = []

for sor in sorok:
    if int(sor[5]) == 0 and int(sor[4]) != 0:  # Ha nincs Michelin-csillaguk és van bezárás éve
        if len(legkevesbe_sikeresek) < 4:
            legkevesbe_sikeresek.append(sor)
        else:
            legkevesbe_sikeresek.sort(key=lambda x: int(x[4]) - int(x[3]))  # egy sor 4. indexű eleme
            if int(sor[4]) - int(sor[3]) < int(legkevesbe_sikeresek[-1][4]) - int(legkevesbe_sikeresek[-1][3]):
                legkevesbe_sikeresek[-1] = sor

eredmeny = [f'\t\t"{sor[0]}" {sor[1]} városában {sor[3]}-től {sor[4]}-ig volt nyitva.' for sor in legkevesbe_sikeresek]
print('\n'.join(eredmeny))


# 7. legjobb étterem
def legjobb_ettermek():
    legjobb_ettermek_kimenet = []
    legtobb_csillag_meg_mukodo = None  # változó a legtöbb csillaggal rendelkező és még működő étterem adatainak tárolására

    for sor in sorok:
        if int(sor[5]) > 0 and int(sor[4]) == 0:  # Ha legalább egy Michelin-csillagja van és a bezárás éve 0
            if legtobb_csillag_meg_mukodo is None or int(sor[5]) > int(legtobb_csillag_meg_mukodo[5]):
                legtobb_csillag_meg_mukodo = sor

    if legtobb_csillag_meg_mukodo is not None:
        legjobb_ettermek_kimenet.append(
            f'\t\t"{legtobb_csillag_meg_mukodo[0]}" , amely {legtobb_csillag_meg_mukodo[1]} városában'
            f' {legtobb_csillag_meg_mukodo[3]}. évben nyitott már {legtobb_csillag_meg_mukodo[5]} csillaga van')
    else:
        legjobb_ettermek_kimenet.append("Nincs adat a legtöbb csillaggal rendelkező és még működő étteremről 2023-ban.")

    return legjobb_ettermek_kimenet


# a 7. Feladat kiíratása a képernyőre
print("7. feladat: \tA jelenleg is működő éttermek közül a legtöbb csillaga a következő(k)nek van:")
legjobb_ettermek_kimenet = legjobb_ettermek()
for sor in legjobb_ettermek_kimenet:
    print(sor)

# 8. Sorolja fel névsorrendben, ismétlődés nélkül azokat az országokat, amelyekben működése alatt tevékenykedett a sztárszakács!
orszagok = set()  # Üres halmaz létrehozása az országok tárolására

for sor in sorok:
    orszag = sor[2]  # Az ország adata az adott sorban a 2. indexen található
    orszagok.add(orszag)  # Az ország hozzáadása a halmazhoz

orszagok_lista = list(orszagok)  # listává alakítjuk
abc = magyar.abc(orszagok_lista)  # a magyar modul használata ÍRORSZÁG jó helyre helyezésére

print("8. feladat: \tGordon Ramsey a következő országokban nyitott éttermeket:")
formazott = magyar.ftordel(abc, 5, '\t\t')  # Szöveg tordeléseés kiírása
print(formazott)


# 9.Volt-e újranyitott étterem ugyanabban a városban? Mikor és hol?
def ujranyitott_ettermek():
    ujranyitott_ettermek = []  # Üres lista az újranyitott éttermek tárolására

    for i in range(1, len(sorok)):
        etterem = sorok[i][0]  # Az étterem neve az adott sorban az 1. indexen található
        varos = sorok[i][1]  # A város neve az adott sorban a 2. indexen található
        orszag = sorok[i][2]  # Az ország neve az adott sorban a 3. indexen található
        nyitas = sorok[i][3]  # Az étterem nyitásának éve az adott sorban a 4. indexen található
        zaras = sorok[i][4]  # Az étterem bezárásának éve az adott sorban a 5. indexen található

        for j in range(i + 1, len(sorok)):
            if sorok[j][0] == etterem and sorok[j][1] == varos and sorok[j][2] == orszag:
                nyitas_ujra = sorok[j][3]  # Az étterem újranyitásának éve
                if nyitas_ujra != zaras:
                    ujranyitott_ettermek.append((etterem, varos, orszag, nyitas, nyitas_ujra))

    return ujranyitott_ettermek


# 9.Volt-e újranyitott étterem ugyanabban a városban? Mikor és hol?
def ujranyitott_ettermek_kiiras():
    ujranyitott_lista = ujranyitott_ettermek()

    if ujranyitott_lista:
        eredmeny = []
        for etterem, varos, orszag, nyitas, nyitas_ujra in ujranyitott_lista:
            eredmeny.append(
                f'\t\tA {etterem} étterem {varos} városában {nyitas}. és {nyitas_ujra}. évben is megnyitott')
        return eredmeny
    else:
        return ["9. feladat: Nem voltak újranyitott éttermek ugyanabban a városban."]


# 9. feladat kiíratása a képernyőre
ujranyitott_ettermek_kimenet = ujranyitott_ettermek_kiiras()
print("9. feladat: \tÚjranyitott éttermek:")
print('\n'.join(ujranyitott_ettermek_kimenet))

mentes_menu()
