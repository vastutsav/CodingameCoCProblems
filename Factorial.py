import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
a = 1
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
for i in range(1,n+1):
    a = a * i
print(a)
