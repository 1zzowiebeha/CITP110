"""Exercise #18 from Chapter 5 of our textbook."""

# Modules allow us to re-use code efficiently.
# Read the following super dense and scary sources if you dare!
# https://docs.python.org/3/tutorial/modules.html
# https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time
from Exercise17 import is_prime

print("Prime numbers between 1-100:\n")

for i in range(101):
    if is_prime(i):
        print(i)

