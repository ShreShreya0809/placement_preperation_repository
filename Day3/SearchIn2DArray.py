def bs(L, target, a, b):
    l=a
    r=b-1
    while(l<=r):
        m=l+((r - l)//2)
        if(L[m]==target): return True
        elif(L[m]<target): l=m+1
        else: r=m-1
    return False

def fun(L, target, a, b):
    l=a
    r=b-1
    while(l<=r):
        m=l+((r-l)//2)
        if(target>=L[m][0] and target<=L[m][b-1]): return bs(L[m],target,0,b)
        elif(target<L[m][0]): r=m-1
        else: l=m+1

    return False


a=int(input())
L=[]
for _ in range(a):
    b=[int(x) for x in input().split(" ")]
    L.append(b)
b=len(L[0])
target=int(input())
if fun(L,target,0,a): print("Found")
else: print("Not found")
