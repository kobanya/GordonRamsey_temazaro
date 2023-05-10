#Nagy Béla 2023-05-15   Témazáró vizsga feladat

# 1.Olvassa be egy alkalmas adatszerkezetbe az állomány tartalmát!
with open('GordonRamsayRestorants.csv', encoding='utf-8') as f:
    lines = f.readlines()                                                       # sorok beolvasása
    fejlec = lines[0]                                                           # a fejléc listába mentése, ez nem feladat
    sorok = [line.strip().split('\t') for line in lines[1:]]                    # A sorokat az 1-es indextől feldarabolom, tabulátorral
    print(f"1. feladat : Beolvasás ... készen van! ({len(sorok)} rekord)")      #kiírom a minta szerint, nincs behúzás

# 2.Jelezze ki, összesen hány étteremmel került GR kapcsolatba!
print(f'2. feladat: \tGordon Ramsey {len(sorok)} étteremmel került kapcolatba.') # egy behúzással kiírva a minta serint

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

# 5.
print(f"5. feladat: \tMichlein-csillagot már kaptak az alábbi éttermek::")
for sor in sorok:
    if int(sor[5]) > 0:                                                             # Ha legalább egy Michelin-csillaguk van
        print(f"{sor[0]:40.40} \t {sor[1]}")                                        # 40 karakter fenntartott hely

