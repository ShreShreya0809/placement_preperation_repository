class Solution:
    def findLongestConseqSubseq(self, arr, N):
        if(len(arr)<1): return 0
        val=0
        Dictionary={}
        for i in range(N):
            if arr[i] not in Dictionary: Dictionary[arr[i]] = i
        for i in range(N):
            x=0
            if(arr[i]-1 not in Dictionary):
                flag=True
                t=arr[i]
                while(flag):
                    if t in Dictionary:
                        x+=1
                        t+=1
                    else: flag=False
                val=max(val,x)
        return val
