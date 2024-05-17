"""My part of code."""

import time


def calculator_input() -> None:
    "Input."
    otwet = 1
    print("Welcome to the calculator!")
    while otwet == 1:
        time.sleep(1)
        print("Do you want to use calculator?")
        time.sleep(0.5)
        print("1) YES!")
        time.sleep(0.5)
        print("2) NO!")
        time.sleep(0.5)
        otwet = int(input("Answer: "))
        time.sleep(1)
        if otwet == 1:
            print("What do you want to do?")
            time.sleep(0.5)
            print("1) +")
            time.sleep(0.5)
            print("2) -")
            time.sleep(0.5)
            print("3) *")
            time.sleep(0.5)
            print("4) %")
            time.sleep(0.5)
            answer = int(input("Answer: "))
            num_1 = int(input("First number: "))
            num_2 = int(input("Second number: "))
            if answer == 1:
                # Здесь должна быть логика для сложения
                pass
            elif answer == 2:
                # Здесь должна быть логика для вычитания
                pass
            elif answer == 3:
                num_3 = multiplication(num_1, num_2)
                print("Answer:", num_3)
            elif answer == 4:
                # Здесь должна быть логика для деления
                pass
    print("Bye!")
    
calculator_input()  # Теперь вызываем функцию без параметров
