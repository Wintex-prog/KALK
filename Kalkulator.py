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

def choose_option(choosed_number):
    if choosed_number == "1": print("add\n", addition())
    elif choosed_number == "2": print("subtract\n", subtraction())
    elif choosed_number == "3": print("multiply\n", multiplication())
    elif choosed_number == "4": print("divide\n", division())
    elif choosed_number == "5": print("intensifies\n", exponentiation())
    else:
        choosed_number = input("Try Again :")
        choose_option(choosed_number);

choose_number = input("What you choose? :")
choose_option(choose_number);

def menu_2():
    print("Write\n"
          "1 - If you want continue\n"
          "2 - If you want stop\n")

print(menu_2())

question = input("What is your choose? :")

def choose_option_1(question):
    if question == "1": print("Select option\n", menu_2())
    elif question == "2": print("Good bay :)")
    else:
        question= input("Try Again :")
        choose_option_1(question);



