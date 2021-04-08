n,l=open(0)
s=1
for c in l:
 if c=='M':s+=1*(s==1)
 if c=='F':s=3*(s>0)
 if c=='G':s=max(0,s-1)
 if c=='W':s-=1*(s>1)
print(['Dead','Small','Tall','Overpowered'][s])
