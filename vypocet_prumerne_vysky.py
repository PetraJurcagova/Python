height = input("Vlozte vysky lidi v cm oddelene carkou a mezerou.\n")

height_list = []
height_list = height.split(", ") 
print(height_list)

average_height = 0

for i in height_list:
    print(i)
    i = int(i)
    average_height += i

total = average_height/ len(height_list)

print(f"Prumerna vyska je {total} cm.")






