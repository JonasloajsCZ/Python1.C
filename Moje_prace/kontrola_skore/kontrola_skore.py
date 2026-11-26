skore = 75  # ulozi cislo do promenne skore

if skore < 0 or skore > 100:  # zkontroluje, jestli je cislo mimo rozsah 0 az 100
    print("Neplatne skore, zadej cislo od 0 do 100.")  # vypise chybu mimo rozsah
elif skore >= 90:  # provede se jen pokud plati predchozi ne a skore je aspon 90
    print("Vyborny vysledek.")  # vypise pochvalu za vysoke skore
elif skore >= 50:  # provede se jen pokud skore je aspon 50 (a zaroven pod 90)
    print("Splneno, muzes jit dal.")  # vypise ze je splneno
else:  # provede se kdyz nesedi zadna podminka vyse (tedy skore 0 az 49)
    print("Nesplneno, zkus to jeste jednou.")  # vypise ze to nevyslo

print("Hotovo.")  # vypise se vzdycky na konci bez ohledu na podminky