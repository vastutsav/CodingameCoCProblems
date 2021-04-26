import sys
import math

n = int(input())
for i in range(n):
    a, b = [int(j) for j in input().split()]
    print(a*a+b)
