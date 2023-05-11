#Nagy Béla 2023-05-15   Témazáró vizsga feladat

# 1.Olvassa be egy alkalmas adatszerkezetbe az állomány tartalmát!
with open('GordonRamsayRestorants.csv', encoding='utf-8') as f:
    lines = f.readlines()                                                       # sorok beolvasása
    fejlec = lines[0]                                                           # a fejléc listába mentése, ez nem feladat
    sorok = [line.strip().split('\t') for line in lines[1:]]                    # A sorokat az 1-es indextől feldarabolom, tabulátorral
    print(f"1. feladat : Beolvasás ... készen van! ({len(sorok)} rekord)")      #kiírom a minta szerint, nincs behúzás

# 2.Jelezze ki, összesen hány étteremmel került GR kapcsolatba!
print(f'2. feladat: \tGordon Ramsey {len(sorok)} étteremmel került kapcolatba.')  # egy behúzással kiírva a minta serint

# 3.Írja ki a jelenleg is működő éttermek számát!
aktualis_ev = 2023                                                                # az aktuális év
muvekodo_ettermek_szama = 0                                                       # változó létrehozása

for sor in sorok[1:]:                                                             # A fejléc sort kihagyjuk
    if sor[4] == '0' or int(sor[4]) > aktualis_ev:                                # Nem zárt be, vagy az aktuális év után zárt be
        muvekodo_ettermek_szama += 1                                              # a számláló megnövelése egyel
print(f"3. feladat: \tJelenleg  {muvekodo_ettermek_szama} étterem működik.")

# 4. Számolja ki, hány százalékuk zárt be az adatfelvétel időpontjáig!
osszes_ettermek_szama = len(sorok)-1                                                            # A fejléc sort kihagyjuk
zaras_arany = (osszes_ettermek_szama - muvekodo_ettermek_szama) / osszes_ettermek_szama * 100   # Az arány kiszámítása
print(f"4. feladat: \tAz éttermek {zaras_arany:.0f} %-a zárt be")

# 5.Írja ki azokat az éttermeket és városaikat, amelyek kaptak már Michelin-csillagot!
print(f"5. feladat: \tMichlein-csillagot már kaptak az alábbi éttermek::")
for sor in sorok:
    if int(sor[5]) > 0:                                                             # Ha legalább egy Michelin-csillaguk van
        print(f"{sor[0]:40.40} \t {sor[1]}")                                        # 40 karakter fenntartott hely


# 6. Melyik éttermek voltak a legkevésbé sikeresek (nem kaptak csillagot és a legrövidebb ideig voltak nyitva)?
print("6. feladat: \tLegkevésbé sikeres éttermek adatai:")
legkevesbe_sikeresek = []

for sor in sorok:
    if int(sor[5]) == 0 and int(sor[4]) != 0:  # Ha nincs Michelin-csillaguk és van bezárás éve
        if len(legkevesbe_sikeresek) < 4:
            legkevesbe_sikeresek.append(sor)
        else:
            legkevesbe_sikeresek.sort(key=lambda x: int(x[4])-int(x[3]))
            if int(sor[4])-int(sor[3]) < int(legkevesbe_sikeresek[-1][4])-int(legkevesbe_sikeresek[-1][3]):
                legkevesbe_sikeresek[-1] = sor

for sor in legkevesbe_sikeresek:
    print(f'"{sor[0]}" {sor[1]} városában {sor[3]}-től {sor[4]}-ig volt nyitva.')

# 7 .Melyikek a legjobb (a legtöbb csillaggal rendelkező) és még működő éttermek?
print("7. feladat: \tA jelenleg is működő éttermek közül a legtöbb csillaga a következő(k)nek van:")
legtobb_csillag_meg_mukodo = None  # változó a legtöbb csillaggal rendelkező és még működő étterem adatainak tárolására

for sor in sorok:
    if int(sor[5]) > 0 and int(sor[4]) == 0:  # Ha legalább egy Michelin-csillagja van és a bezárás éve 0
        if legtobb_csillag_meg_mukodo is None or int(sor[5]) > int(legtobb_csillag_meg_mukodo[5]):
            legtobb_csillag_meg_mukodo = sor

if legtobb_csillag_meg_mukodo is not None:
    print(f'"{legtobb_csillag_meg_mukodo[0]}" , amely {legtobb_csillag_meg_mukodo[1]} városában'
          f' {legtobb_csillag_meg_mukodo[3]}. évben nyitott már {legtobb_csillag_meg_mukodo[5]} csillaga van')
else:
    print("Nincs adat a legtöbb csillaggal rendelkező és még működő étteremről 2023-ban.")
