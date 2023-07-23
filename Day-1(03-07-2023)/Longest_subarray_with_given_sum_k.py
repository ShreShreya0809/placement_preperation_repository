def longestSubarrayWithSumK(a: [int], k: int) -> int:
    x,y=0,0
    count,temp=0,0
    while(x<=y and y<len(a)):
        temp=sum(a[x:y+1])
        if(temp==k):
            if(count<y-x+1):
                count=y-x+1
            y+=1
        elif(temp<k): y+=1
        else:
            if(x==y):
                x+=1
                y+=1
            else: x+=1
    return count
    pass
