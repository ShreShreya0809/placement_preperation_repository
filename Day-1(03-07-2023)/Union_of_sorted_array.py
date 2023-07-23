def sortedArray(a: [int], b: [int]) -> [int]:
    x,y=0,0
    while(x<len(a) and y<len(b)):
        if(a[x]==b[y]):
            y+=1
        elif(a[x]<b[y]):
            x+=1
        else:
            a.insert(x,b[y])
            y+=1
    while(y<len(b)):
        a.append(b[y])
        y+=1
    x=1
    while(x<len(a)):
        if(a[x-1]==a[x]): a.pop(x)
        else: x+=1
    return a
