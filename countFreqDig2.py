import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

i = int(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

dic = {}

for j in str(i):
    if j in dic:
        dic[j] +=1
    else:
        dic[j] = 1

sort_digits = sorted(dic.items(), key=lambda x: int(x[0]))
for k in sort_digits:
    print(str(k[1])+k[0],end="")
