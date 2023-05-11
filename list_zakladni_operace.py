# list

employees = ["David", "Harry", "Ron"]

#print(employees)
#print(employees[0])
#print(employees[1])
#print(employees[2])

# menime polozku v listu
employees[0] = "Petra"
#print(employees)

# pridavani obsahu na konec listu
employees.append("John")
print(employees)

# pridani vicero polozek, do hranatych zavorek []
employees.extend(["Hana", "Dana"])
print(employees)

# odstraneni polozky
employees.remove("Hana")
print(employees)