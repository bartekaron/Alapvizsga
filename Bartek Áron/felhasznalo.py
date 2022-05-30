import random

def felhasznalo():
    felhasznalonev=vezeteknev[0]+keresztnev[0]+str(szam)
    print(felhasznalonev)
    return felhasznalonev




vezeteknev=input("Kérem adja meg a vezetéknevét")

keresztnev=input("Kérem adja meg a keresztnevét")

szam=random.randint(100,999)


felhasznalo()
