class Solution:
    def maxLen(self, n, arr):
        val,temp=0,0
        Dictionary={}
        for i in range(n): temp += arr[i]
            if(temp==0): val=i+1
            else:
                if(temp is in Dictionary): val=max(val,i-Dictionary[temp])
                else: Dictionary[temp]=i
        return val
    

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    Sol = Solution()
    print(Sol.maxLen(n, arr))
