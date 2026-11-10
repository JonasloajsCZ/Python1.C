cislo = 10
if cislo > 0:
    print("Hodnota čísla je kladná")
elif cislo < 0:
    print("Hodnota čísla je záporná.")
else:
    print("Hodnota čísla je nula.")

vek = 20
if vek >= 16 and vek < 18:
    print("Jsi mladistvý.")
else:
    print("Jsi plnoletý.")

body = 90
chceme_ho = False

if body >= 80:
    if chceme_ho:
        print("Má dost bodů.")
        print("Jooo chceme ho.")
    else:
        print("Má dost bodů.")
        print("ALE NECHCEME HO - SORRY.")
else:
    print("Nemá dost bodů. - SMŮLA")

cislo = 5

# % ke MODULO, vrací zbytek po dělení
if cislo % 2 == 0: 
    print("Cislo je sudé.")
else:
    print("Cislo je liché.")

print(7 % 2)

nakupni_kosik = []
if nakupni_kosik:
    print("Kosík není prázdný")
else:
    print("Kosík je prázdný.")

povolene_ovoce = ["jablko", "banán", "pomeranč"]
moje_ovoce = "jablko"

if moje_ovoce in povolene_ovoce:
    print(f"{moje_ovoce.capitalize()} je povolené ovoce.")
else:
    print(f"{moje_ovoce.capitalize()} není na seznamu povoleného ovoce.")