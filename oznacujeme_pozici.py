set_1 = ["😺", "😺", "😺"]
set_2 = ["😺", "😺", "😺"]
set_3 = ["😺", "😺", "😺"]


x = "🐭"

all_sets = [set_1, set_2, set_3]

#print(all_sets)
print(f"{set_1}\n{set_2}\n{set_3}")

position = input("Zadejte souradnice:\n") #  protoze se jedna o string, tak muzeme jednotlive prvky 'vyndat' a pak je prevest na int

# vypis znaku mysi
#rozdeleni souradnic na cisla
num_1 = int(position[0])
num_2 = int(position[1])
#print(num_1)
#print(num_2)

all_sets[num_1][num_2] = x
print(f"{set_1}\n{set_2}\n{set_3}")





