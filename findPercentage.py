n = int(input())
c = 0
for i in range(n):
    c += input().count('*')

if n == 0:
    print('0%')
else:
    print('{}%'.format(100 * c // (n * n)))
