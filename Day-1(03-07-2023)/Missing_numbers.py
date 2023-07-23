class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s=sum(nums)
        S=(len(nums)*(len(nums)+1))//2
        return S-s
