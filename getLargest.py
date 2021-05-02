import sys
import math

n = int(input())
d = list(map(int,input().split()))
d.sort(reverse=True)
print(int(''.join(map(str,d))))
