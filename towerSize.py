I=input
n,m=list(map(int,I().split()))
k=int(I())
r=0
for i in range(n):r+=I().count('o')
print(r*k)
