class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        x=n+m-2
        y=m-1
        val=1
	    
        for i in range(1,r+1):
	        val=(val*(x-y+i))//i
            
        return val
