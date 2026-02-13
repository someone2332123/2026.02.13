import random
#2-es feladat

def lista_keszites(hossz, mettol, meddig):
    szamok: list[int] = []
    for i in range (hossz):
        veletlen = random.randint(mettol, meddig)
        szamok.append(veletlen)
    return szamok

def megszamlalas(szamok: list[int]) -> int:
    db = 0
    for i in range(len(szamok)):
        if szamok[i] < 60:
            db += 1
    return db

def legnagyobb(szamok: list[int]) -> int:
    max_index = 0
    for i in range(len(szamok)):
        if szamok[i] > szamok[max_index]:
            max_index = i
    return szamok[max_index]

def atlag(szamok: list[int]) -> float:
    osszeg = 0
    for i in range(len(szamok)):
        osszeg += szamok[i]
    return osszeg / len(szamok)


def teljes():
    szamok = lista_keszites(20, 50, 70)
    print(f"0.\n\t{szamok}")
    print(f"1.\n\tA szintet teljesítők száma: {megszamlalas(szamok)}")
    print(f"2.\n\tA legnagyobb szám: {legnagyobb(szamok)}")
    print(f"3.\n\tA számok átlaga: {round(atlag(szamok), 2)}")