n = int(input())
line = input()
a=[]
for i in input().split():
    index = int(i)
    a.append(line[index-1])
print(''.join(a))
