"""Zadanie 5.
Jesteśmy w kasynie! Napisz program symulujący automat do gry z trzema obracającymi się kołami. 
Każde koło losowo zatrzymuje się na jednym z symboli ("Wiśnia", "Cytryna", "Pomarańcza", "Dzwon", "Batonik"). 
Gracz rozpoczyna grę z określoną liczbą punktów (np. 100 punktów), a każdy obrót kosztuje 5 punktów. 
Gra trwa do momentu, aż gracz zdecyduje się zakończyć grę lub skończą mu się punkty. 
Wygrane są określane na podstawie kombinacji symboli, które pojawiają się na kołach automatu po każdym obrocie:
1) Trzy identyczne symbole: gracz wygrywa 50 punktów.
2) Dwa identyczne symbole: gracz wygrywa 10 punktów.
3) Brak dopasowania: gracz nic nie wygrywa.
Podpowiedź:
Zaimplementuj funkjcę symulującą obracanie się koła automautu do gry 
(losowe wybranie jednego z symboli) i funkcję uruchamiającą grę do momentu przerwania jej przez gracza 
(lub wyczerpania punktów)."""

import random

# Lista symboli
symbole = ["Wiśnia", "Cytryna", "Pomarańcza", "Dzwon", "Batonik"]

# Ilość punktów gracza na start
punkty_gracza = 100

# Ilość obrotów koła
n = 3

# Pętla gry
while punkty_gracza >= 0:
    wybor = input ("Czy chcesz kontynuować grę? (tak/nie)")

    if wybor.lower() == "tak":
        print (f"Gramy dalej. Masz {punkty_gracza} punktów")
        punkty_gracza -= 5

        #  Funkjca symulująca obracanie się koła automautu do gry 3 razy
        symbole_gracza = []
        dlugosc_listy = len(symbole)
        for i in range(n):
            element_listy = int(random.randint (0, dlugosc_listy -1))
            wylosowany_symbol = symbole[element_listy]
            symbole_gracza.append(wylosowany_symbol)

            # Liczenie powtórzonych symboli
            ilosc_symboli = 0
            for j in symbole:
                a = symbole_gracza.count(j)
                if a > ilosc_symboli:
                    ilosc_symboli = a
                else:
                    continue
        print (f"Wylosowałeś: {symbole_gracza}")

        # Naliczanie wygranej
        if ilosc_symboli == 3:
            punkty_gracza += 50 + 5 # Żeby gracz dostał równo 50 punktów, bez straty na 5 punktów
            print ("Gratulacje!! 50 punktów idzie na Twoje konto")
        elif ilosc_symboli == 2:
            punkty_gracza += 10 + 5 # Żeby gracz dostał równo 10 punktów, bez straty na 5 punktów
            print (" Może nie zdobyłeś 3, ale zawsze 10 punktów idzie do Ciebie")
        else:
            print ("Przegrana :( Tracisz 5 punktów")
        
    elif wybor.lower() == "nie":
        print(f"Dziękuje za grę. Twój wynik to {punkty_gracza} punktów")
        break

    else:
        print("Nieprawidłowa odpowiedź. (tak/nie)")

input("\nAby zakończyć program, wciśnij Enter")