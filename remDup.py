import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()[::-1]

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
o=""
l = []
for i in s:
    if not i in l:
        o += i
        l += [i]
print(o[::-1])
