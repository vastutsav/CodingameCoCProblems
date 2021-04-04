import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
a = 0
str = []
k = ''
for i in s:
    if i == '+':
        a+=1
        if a > 255:
            k = 'OVERFLOW'
            break
    elif i == '-':
        a-=1
        if a < 0:
            k = 'UNDERFLOW'
            break
    elif i == '.':
        str.append(chr(a))

if k == '':
    print ("".join(str))
else:
    print(k)
