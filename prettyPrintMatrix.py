r = int(input())
c = int(input())
w=len(str((r*c)-1))+1
i=[f for f in range(0,r*c)]
for z in range(0,r*c,c):
    h=""
    for e in i[z:z+c]:
        h+=" "*(w-len(str(e)))+str(e)
    print(h)
