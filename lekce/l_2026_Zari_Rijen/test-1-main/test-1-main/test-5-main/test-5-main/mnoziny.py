python_devs = {"Pepa","Jirka", "Honza", "Marek", "Karel", "Romana", "Petr"}
java_devs = {"Romana", "Petr", "Karel", "Mařka", "Lucie"}

# Operace sjednocení (NEBO)
vsichni_devs = python_devs | java_devs
print("Všichni vávojáři (sjednocení):", vsichni_devs)
print(20*"=")

# Operace průnik (A)
polyglot_devs = python_devs & java_devs
print("Vývojáři, kteří ovládají oba jazyky (průnik):", polyglot_devs)

# Operace rozdíl (-)
vsichni_devs = python_devs - java_devs
print("Všichni vývojáří (rozdíl):", vsichni_devs)
print(20*"=")
