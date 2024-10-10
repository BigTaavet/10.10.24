"""Matemaatilised tehted"""
import math


a = float(input("Sisesta kaatet A: "))
b = float(input("Sisesta kaatet B: "))

c = math.sqrt(a**2 + b**2)


ümbermõõt = a + b + c


pindala = 0.5 * a * b

# KASUTAN ROUND COMMANDI, ET ÜMARDADA VASTUSED KÜMNENDIKENI( LEIDSIN SELLE KASUTUSE NETIST )
c = round(c, 2)
ümbermõõt = round(ümbermõõt, 2)
pindala = round(pindala, 2)


print(f"Hüpoteenus c: {c}")
print(f"Ümbermõõt: {ümbermõõt}")
print(f"Pindala: {pindala}")
