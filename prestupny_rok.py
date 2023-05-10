year = int(input("Zadejte letopocet, ktery chcete overit:\n"))

#print(f"Zadany letopocet {year} je prestupny.")
#print(f"Zadany letopocet {year} neni prestupny.")

if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print(f"Zadany letopocet {year} je prestupny.")

elif year % 4 == 0 and year % 100 != 0 :
    print(f"Zadany letopocet {year} je prestupny.")
    
else:
    print(f"Zadany letopocet {year} neni prestupny.")













