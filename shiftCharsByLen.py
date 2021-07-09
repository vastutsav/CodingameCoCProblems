import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

m1 = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

for i in m1:
    print (chr(ord(i)+len(m1)), end='')
