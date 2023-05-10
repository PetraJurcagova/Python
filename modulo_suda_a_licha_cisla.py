
# modulo = zbytek po celociselnem deleni
print(12 % 10) # 2
print(6 % 4) #2
print(14 % 5) #4

cislo = int(input("Zadejte cele cislo:\n"))

if cislo % 2 == 0:
    print("Jedna se o sude cislo.")
else:
    print("Cislo je liche.")