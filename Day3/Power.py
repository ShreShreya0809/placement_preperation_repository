def p(x, n):
    val = 1
    for i in range(n): val=val*x
    return val


a=int(input())
b=int(input())
print(p(a,b))
