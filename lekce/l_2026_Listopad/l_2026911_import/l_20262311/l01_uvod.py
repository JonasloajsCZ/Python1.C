jmeno = input("Zadejte své jméno: ")
print("Tšsí mě,", jmeno)

print("Python", "je", "skvělý")               # Vypíše: Python je skvělý
print("2026", "11", "12", sep="-")            # Vypíše: 2026-11-12
print("Načítám data", end="... ")
print("Hotovo!")                              # Vypíše na stejný řádek: Načítám data... Hotovo!
print()                                       # Prázdný print() pouze odřádkujejon

cena = 49.90
aktivni = True
nic = None

print(type(cena))     # <class 'float'>
print(type(aktivni))  # <class 'bool'>
print(type(nic))      # <class 'NoneType'>