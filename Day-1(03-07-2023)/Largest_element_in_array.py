def largestElement(arr: [], n: int) -> int:
    M=arr[0]
    for i in range(1,n):
        if(arr[i]>M): M=arr[i]
    return M
    pass
