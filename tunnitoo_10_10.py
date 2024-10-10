"""Matemaatilised tehted"""
import math
# tingimuslaused if ja else töötavad ainult andmetüübiga bool(ean)

# booleanil on vaid kaks väärtust kas False(ei kehti/0) või True (kehtiv/1)
# booleani võib igasugu moodi esitada kuid kõige levinum on võrdlemine
# kui tahame teada, kas 1 + 3 on võrdne nelajaga siis kasutame märki ==, töötab ka tekstiga
# kuid peam olema tähelepanelik, kuna "Punane" ei ole sama mis "punane", kuid "Punane".lower() on sama mis "punane"
print(1 + 3 == 4)
print("PUNANE".isupper())
print("Punanae == punane:")
print("Punane" == "punane")
print("Punane.lower() == punane:")
print("Punane".lower() == "punane")

# siis on võimalus võrrelda kas on suurem või võiksem
print("--------------------------")
print("<, >, >=, <= :")
print(1 + 2 < 4)

# Samuti on jällegi olemas sisemoodulid nagu bool() siit saab näha, et  0 = False/ei kehti ja 1= True/kehtib
print(bool(0))
# Lisaks sellele on näiteks ka sisefunktsioonid sõnel,
# mis annavad võimalust kohe kontrollida, kas midagi kehtib või mitte
# Kuidas saaks kontrollida et sõna "PUNANE" on kirjutatud suurte tähtedega
# või et "punane" on kirjutatud väikeste tähtedega


# oletame et tahame teada kas arv on paaris või paaritu, kuidas saaks sellist ülesannet lahendada
# mõtle, kuidas sina saad teada, et arv on paaris
# kirjuta kood, mis küsib kasutajalt arvu



# ülesanne


# ruutvõrrand esitatakse kujul ax2+bx+c
# ruutvõrrand lahendatakse kordajate a, b, c abil, ruutvõrrandi lahendivalemi järgi

# koosta muutuja a, lisa võimalus kasutajal sisestada arv, muuda see täisarvuks
a=int(input("Sisesta oma arv A: "))
# koosta muutuja b, lisa võimalus kasutajal sisestada arv, muuda see täisarvuks
b=int(input("Sisesta oma arv B: "))
# koosta muutuja c, lisa võimalus kasutajal sisestada arv, muuda see täisarvuks
c=int(input("Sisesta oma arv C"))
# ruutvõrrandil on tavaliselt 2 lahendit või lahendid puuduvad,
diskriminant = (b ** 2) - (4 * a * c)
if diskriminant < 0:
    print("Lahendid puuduvad")
else:
    lahend1= (-b + math.sqrt(diskriminant)) / (2 * a)
    lahend2= (-b - math.sqrt(diskriminant)) / (2 * a)
    print(f"Lahendid on: x1={lahend1} ja x2={lahend2}")
# kuidas saaks kohe üelda kasutajale, et lahendid puuduvad, kuidas neid leida
# kuidas võiks nimetada muutujaid
