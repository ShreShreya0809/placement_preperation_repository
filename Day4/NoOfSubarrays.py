def fin(L, x):
    fin,val,Dictionary=0,0,{}
    
    for i in range(len(L)):
        val^=L[i]
        t=val^x
        if(val==x): fin+=1
        if(t in Dictionary): fin+=Dictionary[t]
        if(val in Dictionary): Dictionary[val] += 1
        else: Dictionary[val] = 1
    return fin

L = list(map(int, input().split()))
x = int(input())

print(fin(L, x))
