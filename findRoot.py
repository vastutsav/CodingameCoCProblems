import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
y = int(input())

r = 0

while n <= y:
    y //= n
    r += 1

print(r)
