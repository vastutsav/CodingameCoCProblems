import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

ordered_items = input().split(" ")
received_items = input()
invoiced_items = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
tmp = [value for value in ordered_items if value in received_items and value in invoiced_items]
print(" ".join(tmp))
