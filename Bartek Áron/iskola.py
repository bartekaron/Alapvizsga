hetek=36
szam=int(input("Hány hetet jártunk ebben a tanévben iskolába?"))
hatra=hetek-szam
print("Ennyi hetet kell még járnunk az iskolába:", hatra)
if hatra > 5:
    print("Még van idő javítani!")
elif hatra <= 5 and hatra > -1:
    print("Itt az év vége!")
else:
    print("Hibás adatot adott meg")

#https://github.com/fokizoli/Alapvizsga_web_2022m-jus