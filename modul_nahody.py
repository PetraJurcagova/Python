import random
import math
# generovani nahodneho celeho cisla z rozsahu
print(random.randint(10,20))

# generovani nahodneho floatu (desetineho cisla) mezi 0 a 1
print(random.random())
print(random.random() * 6) # nahodny float v rozsahu 0 - 6

#simulace hazeni kostkou
print(math.ceil(random.random()*6))
print(math.ceil(random.random()*6))
print(math.ceil(random.random()*6))
print(math.ceil(random.random()*6))



# generovani nahodneho celeho cisla v rozsahu zde po dvou krocich
print(random.randrange(15,25,2))

import math
print(math.ceil(5.1)) # zaokrouhleni nahoru
print(math.floor(5.9)) # zaokrouhleni dolu