size = input("Vitejte v pizzerii.\nZvolte si velikost pizzy S, M, L.\n")
peppers = input("Prejete si feferonky? A nebo N\n")
cheese = input("Prejete si syr navic? A nebo N\n")

bill = 0

if size == "S":
    bill = bill + 100
    if peppers == "A":
        bill = bill + 20
    if cheese == "A":
        bill = bill + 15

elif size == "M":
    bill = bill + 150
    if peppers == "A":
        bill = bill + 30
    if cheese == "A":
        bill = bill + 15

elif size == "L":
    bill = bill + 200
    if peppers == "A":
        bill = bill + 30
    if cheese == "A":
        bill = bill + 15

print(f"Cena vasi pizzy je {bill} Kc.")









