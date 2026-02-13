import random
#2-es feladat

def lista_keszites():
    szamok = [int]
    for i in range (20):
        veletlen = random.randint(50, 70)
        szamok.append(veletlen)
    return szamok

def teljes():
    szamok = lista_keszites()
    print(szamok)