import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

row1 = input()
row2 = input()
row3 = input()
row4 = input()
row5 = input()
values = [int(i[:-2]) for i in row1.split()]
d1,d2=[i for i,k in enumerate(row3) if k=="v"]
f,=[i for i,k in enumerate(row5) if k=="A"]

left = f - d1
right = d2 - f

if left*values[0] == right*values[1]:
    print(1)
else:
    print(0)

