import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input().split()
if len(s)%2:
    print(s[len(s)//2])
else:
    print(s[len(s)//2-1]+s[len(s)//2])
