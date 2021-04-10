import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
a=[]
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
while True:
    a.append(n)
    if n == 1: break
    if n%2 == 0:
        n//=2
    else:
        n = n * 3 + 1

print(" ".join(map(str,a)))
