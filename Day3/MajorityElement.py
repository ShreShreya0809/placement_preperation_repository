class Solution:
    def fun(self, nums: List[int]) -> List[int]:
        n = len(nums)
        A, a = -1, 0
        B, b = -1, 0
        L=[]
        for i in nums:
            if(i==A): a += 1
            elif(i==B): b += 1
            elif(a==0):
                A = i
                a += 1
            elif(b==x0):
                B = i
                b += 1
            else:
                a -= 1
                b -= 1
        a,b=0,0
        for i in nums:
            if(i==A): a+=1
            elif(i==B): b+=1
                
        if(a>n//3): L.append(A)
        if(b>n//3): L.append(B)
        
        return L
