import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
l = [str(n)]
while True:
    rev = int(str(n)[::-1])
    if rev == n:
        break;
    n = n + rev
    l.append(str(n))


print(" ".join(l))
