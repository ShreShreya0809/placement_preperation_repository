def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    m1,m2=max(a),max(a)
    M2,M1=-1,-1
    for i in range(n):
        if(a[i]<m1):
            m2=m1
            m1=a[i]
        elif(a[i]<m2): m2=a[i]
        if(a[i]>M1):
            M2=M1
            M1=a[i]
        elif(a[i]>M2): M2=a[i]
    return [M2,m2]
