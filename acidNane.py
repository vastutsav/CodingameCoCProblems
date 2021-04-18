import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

inputs = input().split()
nonmetal_num = int(inputs[0])
nonmetal = inputs[1]
oxide_num = int(input())

oxlis = ["","mon","di","tri","tetr","pent"]
nonlis = ["","","di","tri","tetr","pent"]
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
ans = nonlis[nonmetal_num]+nonmetal + " " + oxlis[oxide_num]+"oxide"
print(ans)
