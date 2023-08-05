def R(n):
    val = 0
    while(n>0):
        val=val*10+n%10
        n//=10
    return val

def CR(L, n):
    val = 0
    for x in range(n):
        for y in range(x + 1, n):
            if(R(L[x])==L[y]): val += 1
    return val


L=[int(x) for x in input().split(" ")]
n=int(input())
print(CR(L,n))
