import time

num_1 = 0
num_2 = 0

def calculator_input(num_1, num_2):
    otwet = 1
    answer = 0
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
            print("Wat do you want to do?")
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
            return num_1, num_2;
            if answer == 1:
                pass
            elif answer == 2:
                pass
            elif answer == 3:
                pass
            elif answer == 4:
                pass
    print("Bye!")
calculator_input(num_1, num_2) 
