import random
import math

print ("Witaj! Wprowadz granice i sprobuj odgadnac wylosowana liczbe!")
print()
lower = int(input("Wprowadz dolna granice: "))
upper = int(input("Wprowadz gorna granice: "))
 
if lower == upper:
    print("Podaj zakres liczb, wystarczajaco duzy, aby obejmowal chociaz 2 liczby")
elif lower > upper:
    print("Dolna granica nie moze byc wieksza od granicy gornej")
else:
    # Generowanie liczby z zakresu
    proby = round(math.log(upper - lower + 1, 2))
    x = random.randint(lower, upper)
    if proby == 1:
        print("\n\tMasz tylko ", proby,
        " probe, aby odgadnac liczbe!\n")
    elif proby > 1 and proby < 5:
        print("\n\tMasz tylko ", proby,
        " proby, aby odgadnac liczbe!\n")
    elif proby > 4:
        print("\n\tMasz tylko ", proby,
        " prob, aby odgadnac liczbe!\n")
      
    count = 0
 
    # Wyliczanie mozliwych prob po ustalonych granicach
    while count < proby:
        count += 1
 
        guess = int(input("Zgadnij liczbe: "))
 
        # Sprawdzanie poprawnosci przypuszczenia
        if x == guess:
            print("Gratulacje, udalo ci sie odgadnac w",
                count, "probach!")
            break
        elif x > guess:
            print("Twoje przypuszczenie jest za male!")
        elif x < guess:
            print("Twoje przypuszczenie jest za duze!")
 
    # Jezeli nie udalo sie odgadnac w wyznaczonych probach
    if count >= proby:
        print("\nPoprawna liczba to %d" % x)
        print("\tPowodzenia nastepnym razem!")
