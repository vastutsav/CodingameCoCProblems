I=input
n=int(I())
j=[]
for i in range(n):j.append(I().split())
j.sort(key=lambda x:-float(x[1]))
print(" ".join([i for i,k in j]))
