print("Vitejte ve hre kamen, nuzky, papir!")

list_choice = ["kamen", "papir","nuzky"]# [0,1,2]

choice = int(input("Hra zacina! Co si vyberete?\nNapiste 0 pokud kamen, 1 pro papir, 2 pro nuzky.\n"))


user_choice = list_choice[choice]

print(f"Uzivatel si vybral {user_choice}.")

# nahodny vyber pocitace
import random

computer = random.randint(0, len(list_choice)-1) # predstavuje index
computer_choice = list_choice[computer]

print(f"Pocitac si vybral {computer_choice}")# computer_choice zde predstavuje index, ktery ztotoznime s list_choice

if computer_choice == user_choice:
    print("Jedna se o remizu!")

elif computer_choice == "kamen" and user_choice == "papir":
        print("Vyhrali jste!")
elif computer_choice == "kamen" and user_choice == "nuzky":
    print("Prohrali jste :(.")

elif computer_choice == "nuzky" and user_choice == "kamen":
    print("Vyhrali jste!")
elif computer_choice == "nuzky" and user_choice == "papir":
    print("Prohrali jste :(.")

elif computer_choice == "papir" and user_choice == "nuzky":
    print("Vyhrali jste!")
elif computer_choice == "papir" and user_choice == "kamen":
    print("Prohrali jste :(.")

