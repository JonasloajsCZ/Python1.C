# Vytvoření seznamu čtverců pomocí list comprehension
Squares = [x**2 for x in range(10)]
print(f"čtverec čísel od 0 do 9: {Squares}")

mocnina = []
for x in range(10):
    mocnina.append(x**2)
    print(x, x**2)
 
words = ["python", "je", "skvělý", "programovací", "jazyk"]
upper_words = [word.upper() for word in words]
print(f"Slova převedená na velká písmena: {upper_words}")
    