"""Exercise 2 from Chapter 7 of our textbook."""

import random

lotto_ticket = []

for iteration in range(7):
    lotto_ticket.append(random.randint(0,9))
    
print("\nYour ticket numbers are:")
for lucky_number in lotto_ticket:
    print(lucky_number)