import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_char = ['%', '#', '$', '!', '&', '(', ')', '*', '+', '?']

print("Vitejte v generatoru hesel!")
letters_number = int(input("Kolik pismen chcete mit ve svem heslu?\n"))
num_numbers = int(input("Kolik cisel chcete mit ve svem heslu?\n"))
num_special_char = int(input("Kolik specialnich znaku chcete mit ve svem heslu?\n"))


promenna = []

for nic in range (0, letters_number):
    #print(nic)
    random_number = random.randint(0, len(letters)-1)
    promenna.append(letters[random_number])

for _ in range (0, num_numbers):
    random_number = random.randint(0, len(numbers)-1)
    promenna.append(numbers[random_number])

for blabla in range (0, num_special_char):
    random_number = random.randint(0, len(special_char)-1)
    promenna.append(special_char[random_number])

print(promenna)
#print(promenna[0])

# nahodne zprehazeni hesla = delsi zpusob, nekde je chyba, nedari se spustit kod !
#translator = " "
#for index in range(0, 20):
    #random_index_1 = random.randint(0, (len(promenna)-1))
    #random_index_2 = random.randint(0, (len(promenna)-1))

    #translator = promenna[random_index_2]
    #promenna[random_index_2] = promenna[random_index_1]
    #random_index_1 = translator
#print(translator)

# nahodne zprehazeni znaku pomoci shuffle, toto jiz funguje2
random.shuffle(promenna)
print(promenna)


#prevod listu na string
result = " " #pomoci prazdne promenne, prazdny string, kam se mi ma ukladat vysledek
for index in promenna:
    result = result + index
    #result += index
print(result)










