def moveZeros(n: int,  a: [int]) -> [int]:
    i,count=0,0
    while(i<len(a)):
        if(a[i]==0): 
            count+=1
            a.pop(i)
        else: i+=1
    for i in range(count): a.append(0)
    return a
