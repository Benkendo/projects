import random
import decimal
import itertools
random_number = int(round(((decimal.Decimal(random.random()*10))+1),2))
print (random_number)

x = ''
while x < random_number:
    for x in itertools.islice(range(random_number, 1.0, 0.1)):
        print(x)


