age = int(input("Kolik je vam let?\n"))

year = (90 - age)
month = (90*12) - (age * 12)
week = (90*52) - (age * 52)
day = (90*365) - (age * 365)

print(f"Do konce zivota vam zbyva {year} let, {month} mesicu, {week} tydnu, {day} dni.")

# nebo si lze ulozit age jako promennou napr remain, tj. 90-age = remain a pak je to: remain *12, remain *52, remain * 365










