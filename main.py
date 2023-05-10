#Nagy Béla 2023-05-15   Témazáró vizsga feladat

# 1.Olvassa be egy alkalmas adatszerkezetbe az állomány tartalmát!

with open('GordonRamsayRestorants.csv', encoding='utf-8') as f:
    lines = f.readlines()   # sorok beolvasása
    header = lines[0]     # a fejléc listába mentése, ez nem feladat
    rows = [line.strip().split('\t') for line in lines[1:]]  # A sorokat az 1-es indextől feldarabolom, tabulátorral
    print(f"1. feladat : Beolvasás ... készen van! ({len(rows)} rekord)") #kiírom a minta szerint, nincs behúzás

# 2.Jelezze ki, összesen hány étteremmel került GR kapcsolatba!
print(f'2. feladat: \tGordon Ramsey {len(rows)} étteremmel került kapcolatba') # egy behúzással kiírva a minta serint