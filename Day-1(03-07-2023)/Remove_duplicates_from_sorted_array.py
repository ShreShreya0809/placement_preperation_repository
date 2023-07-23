def removeDuplicates(arr,n):
    i=1
    while(i<len(arr)):
        if(arr[i-1]==arr[i]): arr.pop(i)
        else: i+=1
    return len(arr)
    pass
