import random

name = input("Napis mi jmena vsech jedliku oddelena carkou.\n")

list_name = name.split(", ")
#print(list_name)

number = random.randint(0,len(list_name)-1)

print(f"{list_name[number]} bude dnes platit ucet.") # number zde predstavuje index, ktery ztotoznime se jmenem














