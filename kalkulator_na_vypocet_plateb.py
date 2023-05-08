print("Vitejte v kalkulatoru na vypocet plateb.")

cost = int(input("Kolik mate celkem zaplatit?\n"))
percent = int(input("Kolik chcete dat spropitne v procentech?\n"))
people = int(input("Mezi kolik lidi se ma castka rozdelit?\n"))

total = int((cost + ((cost/100) * percent))/people)

print(f"Kazdy zakaznik zaplati {total} Kc.")


















