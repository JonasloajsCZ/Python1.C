# slovník 

kontakty  = {
    "jmeno": "Jan",
    "prijmeni": "Novák",
    "vek": 30,
    "mesto": "Praha",
    "mail": "jan.novak@email.com",
    "telefon": "792 456 789"
}
# vytiskne celou datovou strukturu
print(f"Původní kontakty: {kontakty}")

print(f"Jméno: {kontakty['jmeno']}")

kontakty["mesto"] = "Ostrava"
print(kontakty)

telefon = kontakty.get("telefon")
print("Telefonní číslo:", telefon)