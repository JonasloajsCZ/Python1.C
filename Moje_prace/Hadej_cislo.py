import random  # nacteme modul pro nahodna cisla

tajne_cislo = random.randint(1, 10)  # pocitac si vybere nahodne cislo od 1 do 10
pokusy = 0  # promenna, ktera pocita nase pokusy 

print("Hádej číslo od 1 do 10")

while True:  # cyklus se opakuje, dokud ho neprerusime
    tip = int(input("Tvůj tip:"))  # input() nacte text, int() ho zmeni na cislo
    pokusy = pokusy + 1  # po kazdem tipu zvysime pocitadlo o 1

    if tip == tajne_cislo:  # == porovnava, jestli se cisla rovnaji
        print("Správně, trvalo ti to",pokusy,"pokusů.")
        break  # break ukonci cyklus
    elif tip < tajne_cislo:  # elif = jinak,pokud
        print("Moc málo, zkus víc.")
    else:  # else se provede, kdyz neplati nic z predchoziho
        print("Moc moc, zkus míň.")