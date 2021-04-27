import sys
import math
 
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
 
def pattern(inputv):
    if not inputv:
        return inputv
 
    nxt = [0]*len(inputv)
    for i in range(1, len(nxt)):
        k = nxt[i - 1]
        while True:
            if inputv[i] == inputv[k]:
                nxt[i] = k + 1
                break
            elif k == 0:
                nxt[i] = 0
                break
            else:
                k = nxt[k - 1]
 
    shortLen = len(inputv) - nxt[-1]
    if len(inputv) % shortLen != 0:
        return inputv
 
    return inputv[0:shortLen]
 
s = input()
 
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
 
print(pattern(s))
