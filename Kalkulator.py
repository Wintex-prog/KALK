print("::CALCULATOR::")

def menu():
    print("Menu\n"
          "1 - addition\n"
          "2 - subtraction\n"
          "3 - multiplication\n"
          "4 - division\n"
          "5 - exponentiation\n")

def addition():
    first_number = (input("Enter first number :"))
    second_number = (input("Enter second number :"))
    wynik = float(first_number)+float(second_number)
    return wynik
def subtraction():
    first_number = input("Enter first number :")
    second_number = input("Enter second number :")
    wynik = float(first_number) - float(second_number)
    return wynik
def multiplication():
    first_number = input("Enter first number :")
    second_number = input("Enter second number :")
    wynik = float(first_number) * float(second_number)
    return wynik
def division():
    first_number = input("Enter first number ")
    second_number = input("Enter second number ")
    wynik = float(first_number) / float(second_number)
    return wynik
def exponentiation():
    first_number = input("Enter first number :")
    second_number = input("Power :")
    wynik = float(first_number) ** float(second_number)
    return wynik

print(menu())


def Choose_option(choose_number):
    if choose_number == "1": print("add\n", addition())
    elif choose_number == "2": print("subtract\n", subtraction())
    elif choose_number == "3": print("multiply\n", multiplication())
    elif choose_number == "4": print("divide\n", division())
    elif choose_number == "5": print("intensifies\n", exponentiation())
    else:
        choose_number = input("Try Again")
        Choose_option(choose_number);


choose_number = input("What you choose? :")
Choose_option(choose_number);



