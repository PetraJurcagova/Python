
height = float(input("Zadejte svou vysku v metrech.\n"))
weight = int(input("Zadejte svou vahu v kg\n"))


BMI = weight/(height*height)
#BMI = int(weight) / (float(height) * float(height))

#BMI = float(BMI)
BMI = float(round(BMI, 2))

print(f"Vas BMI index je {BMI}.")

if BMI <+ 18.5:
    print("Mate podvahu.")
elif BMI <= 24.9:
    print("Mate normalni vahu.")
elif BMI <= 29.9:
    print("Mate mirnou nadvahu, zkuste cvicit!")
elif BMI <= 34.9:
    print("Jste obezni, zacnete se hybat.")
else:
    print("Trpite extremni obezitou, vyhledejte sprintem lekare!")







