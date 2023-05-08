print("Vitejte na horske draze!")

height = int(input("Jaka je vase vyska v cm?\n"))


if height >= 87:
    print("Muzete jet na horske draze!")

    age = int(input("Kolik je vam let?\n")) # doplnena podminka veku a cena listku
    if age < 12:
        print("Cena vaseho listku je 50 kc.")
    elif age < 18:
        print("Cena vaseho listku je 100 Kc.")
    else:
        print("Cena vaseho listku je 150 Kc.")
else:
    print("Nemuzete jet na horske draze.")
    












