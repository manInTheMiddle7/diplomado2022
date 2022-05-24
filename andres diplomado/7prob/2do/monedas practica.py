import random
import statistics
import stat


sello=0
aguila=0

for x in range(10000):
    moneda = random.randint(0, 1)
    if moneda == 0:
        sello=sello+1
    else:
        aguila=aguila+1

print("cayo sello: ",sello)
print("cayo aguila: ",aguila)


