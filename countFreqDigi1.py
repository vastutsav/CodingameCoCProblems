import sys
import math
from collections import Counter

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

N = Counter(input())

o = []
for n,c in sorted(N.items()):
    o += [str(c)+n]
print(*o,sep='')
