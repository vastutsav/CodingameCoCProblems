import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
word = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

for i in range(n):
    word = word[1:]+word[:1]
print(word)
