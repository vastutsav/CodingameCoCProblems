n=int(input())
s=sum([i for i in range(1,n)if n%i==0])
print([["abundant","deficient"][s<n],"perfect"][n==s])
