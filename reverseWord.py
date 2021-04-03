s = input().split()
s = [''.join(reversed(ss)) for ss in s]
print(' '.join(s))
