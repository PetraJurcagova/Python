#suma cisel
# Carl Gauss
total = 0
for number in range (1, 101):
    #total = 0 + number
    total += number
print(total)

# Sectete vsechna suda cisla v rozmazi 1 - 100
total = 0
for number in range (1, 101):
    if number % 2 == 0:
        total += number
print(total)

#Sectete vsechna licha cisla v rozsahu 1 - 100
total = 0
for licha in range (1, 101):
    if licha % 2 != 0:
        #total = total + licha
        total += licha
print(total)
