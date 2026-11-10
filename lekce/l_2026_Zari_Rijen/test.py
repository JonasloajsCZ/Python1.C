# Myslím si číslo1

import random

print("Vítej ve hře! Myslím si číslo od 1 do 10.")
tajne_cislo = random.randint(1, 10)
uhodnuto = False

while not uhodnuto:
    tip = int(input("Zadej svůj tip: "))
    
    if tip < tajne_cislo:
        print("Moc malé! Zkus to znovu.")
    elif tip > tajne_cislo:
        print("Moc velké! Zkus to znovu.")
    else:
        print("Gratuluji! Uhodl jsi správné číslo!")
        uhodnuto = True
