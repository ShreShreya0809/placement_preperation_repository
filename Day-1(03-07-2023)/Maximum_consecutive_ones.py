class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m1,c1=0,0
        for i in range(len(nums)):
            if(nums[i]==1): c1+=1
            if(nums[i]==0):
                if(m1<c1): m1=c1
                c1=0
        if(m1<c1): m1=c1
        return m1
