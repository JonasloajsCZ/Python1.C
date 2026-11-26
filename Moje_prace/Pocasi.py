# zepta se na teplotu a ulozi jako cislo
teplota = int(input("Kolik je venku stupňů? "))

# kdyz je vic jak 25
if teplota >= 25:
    print("Je horko, vezmi si tričko a kraťasy.")

# kdyz je mezi 15 a 24
elif teplota >= 15:
    print("Je příjemně, stačí lehká mikina.")

# kdyz je aspon 5
elif teplota >= 5:
    print("Je chladno, obleč si bundu.")

# jinak je zima
else:
    print("Mrzne nebo je velká zima, vezmi si zimní kabát a čepici!")