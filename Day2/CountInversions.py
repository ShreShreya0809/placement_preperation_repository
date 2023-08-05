def fun(arr, x, l, m, r):
    val = 0
    
    i = l
    j = m
    k = l
    while (i<=m-1 and j<=r):
        if (arr[i]<=arr[j]):
            x[k] = arr[i]
            i += 1
            k += 1
        else:
            x[k] = arr[j]
            j += 1
            k += 1
            val = val + (m - i)
    
    while (i<=m-1):
        x[k] = arr[i]
        k += 1
        i += 1
    
    while (j<=r):
        x[k] = arr[j]
        j += 1
        k += 1     
    
    for i in range(l, r + 1):
        arr[i] = x[i]
    
    return val
    
def ms(arr, x, l, r):
    val = 0
    if (r>l):
        m = (r + l) // 2
        val += ms(arr, x, l, m)
        val += ms(arr, x, m + 1, r)
        
        val += fun(arr, x, l, m + 1, r)
    return val
