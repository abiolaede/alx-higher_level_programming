
#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = abs(number) % 10

if number < 0:
    lastdigit *= -1
if lastdigit > 5:
    print("Last digit of {} is {} and\
 is greater than 5".format(number, lastdigit))
elif lastdigit < 6 and lastdigit != 0:
    print("Last digit of {} is {} and\
 is less than 6 and not 0".format(number, lastdigit))
else:
    print("Last digit of {} is {} and is 0".format(number, lastdigit))

