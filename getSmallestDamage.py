import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
vf = 9999999
k=1
n = int(input())  # The numbers of paths the train can take
for i in range(n):
    # q: The number of persons on the path
    # v: The individual value of each person on the path
    q, v = [int(j) for j in input().split()]
    if q*v < vf:
        vf = q*v
        ans = k
    k+=1

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(ans)
