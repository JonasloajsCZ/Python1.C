import os
script_dir = os.path.dirname(os.path.abspath(__file__))
soubor_cesta = os.path.join(script_dir, "data.txt")
print(f"Otevírám soubor v adresáři: {script_dir}")

try:
    with open(soubor_cesta, "r", encoding="utf-8") as f:
        line = f.read()
        while line:
            print(line.strip())
            line = f.readline()
except FileNotFoundError:
    print(f"Soubor {soubor_cesta} nebyl nalezen.")
    