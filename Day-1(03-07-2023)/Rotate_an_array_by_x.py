n=int(input())
L=[int(x) for x in (input().strip()).split(" ")]
k=int(input())
L=L[k:]+L[:k]
for i in range(n):
    print(L[i],end=' ')
