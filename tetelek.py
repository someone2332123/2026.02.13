import random
#2-es feladat

def lista_keszites(hossz, mettol, meddig):
    szamok: list[int] = []
    for i in range (hossz):
        veletlen = random.randint(mettol, meddig)
        szamok.append(veletlen)
    return szamok

def megszamlalas(szamok: list[int]):
    db = 0
    for i in range(len(szamok)):
        if szamok[i] < 60:
            db += 1
    return db



def teljes():
    szamok = lista_keszites(20, 50, 70)
    print(szamok)
    print(f"A szintet teljesítők száma: {megszamlalas(szamok)}")