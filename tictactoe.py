I=input
n = int(I())
a = [" " for x in range(9)]
for i in range(n):
    if i % 2 == 0:
        a[int(I())] = "x"
    else:
        a[int(I())] = "o"
for m in range (0, 9, 3):
    print(a[m]+"|"+a[m+1]+"|"+a[m+2])

