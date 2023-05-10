print("Vitejte na horske draze!")

height = int(input("Jaka je vase vyska v cm?\n"))
bill = 0

if height >= 87:
    print("Muzete jet na horske draze!")

    age = int(input("Kolik je vam let?\n")) # doplnena podminka veku a cena listku
    if age < 12:
        bill = 50
        print("Cena vaseho listku je 50 kc.")
    elif age < 18:
        bill = 100
        print("Cena vaseho listku je 100 Kc.")
    elif age >= 40 and age <= 50: # doplneni podminky s logickym operatorem
        #bill = 0
        print("Dnes mate stastny den, jedete zdarma!")
    else:
        bill = 150
        print("Cena vaseho listku je 150 Kc.")

    photo = input("Chcete se nechat vyfotit? A nebo N\n")
    if photo == 'A':
        #bill = bill + 50
        bill += 50
        print(f"Cena vaseho listku je {bill} Kc.")
else:
    print("Nemuzete jet na horske draze.")
    












