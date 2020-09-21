import math
import datetime

print("Hello and welcome!")
print("Enter a number larger than 0. Then press Enter")

q = datetime.datetime.now()

n = int(input())
m = [x+2 for x in range(n-1)]

a = int(math.sqrt(n))

k = [x+2 for x in range(a-1)]

for x in k:
    a = 0
    for y in m:
        if y % x == 0 and y != x:
            m.pop(a)
        a = a + 1

print(m)
print("These are all prime numbers up til " + str(n) + "!")

b = datetime.datetime.now()
c = b - q

print("The total time it took was: " + str(c.seconds) + " s")
