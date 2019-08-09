print("::KALKULATOR::")

def menu():
    print("Menu\n"
          "1 - dodawanie\n"
          "2 - odejmowanie\n"
          "3 - mnożenie\n"
          "4 - dzielenie\n"
          "5 - potęgowanie\n")

def dodawanie():
    a = (input("Wpisz pierwsza liczbę :"))
    b = (input("Wpisz drugą liczbę :"))
    wynik = float(a)+float(b)
    return wynik
def odejmowanie():
    a = input("Pierwsza liczba ")
    b = input("Druga liczba ")
    wynik = float(a) - float(b)
    return wynik
def mnozenie():
    a = input("Pierwsza liczba ")
    b = input("Druga liczba ")
    wynik = float(a) * float(b)
    return wynik
def dzielenie():
    a = input("Pierwsza liczba ")
    b = input("Druga liczba ")
    wynik = float(a) / float(b)
    return wynik
def potegowanie():
    a = input("Liczba ")
    b = input("Potęga ")
    wynik = float(a) ** float(b)
    return wynik

print(menu())

funkcja = input("Co wybierasz ? :")
while True:
    if funkcja == "1": print("dodaj\n", dodawanie())
    elif funkcja == "2": print("odejmij\n", odejmowanie())
    elif funkcja == "3": print("mnóż\n", mnozenie())
    elif funkcja == "4": print("dziel\n", dzielenie())
    elif funkcja == "5": print("potęguj\n", potegowanie())
    else:
        print("mamy bląd")
        break