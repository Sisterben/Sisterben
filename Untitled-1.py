import random
r = random.randrange(1,1000)
if r % 2 == 0:
    print(r,'is even.')
else:
    print(r,'is odd.')    
    693 is odd

for i in range(10):
    if i % 2 != 0:
        print(i)

for n in range(2, 100):
    if n == 2:
        print(n)
        continue
    for i in range(2, n):
        if (n % i) == 0:
            break
else:
    print(n)

r = 25
area = 3.1415 * r * r
print(area)
print("{:.2f}".format(area))

import turtle
turtle.pensize(2)
turtle.circle(10)
turtle.circle(40)
turtle.circle(80)
turtle.circle(160)

for n in range(2, 100):
    if n == 2:
        print(n)
        continue
    for i in range(2, int(n ** 0.5)+1):
        if (n % i) == 0:
            break
        else:
            print(n)