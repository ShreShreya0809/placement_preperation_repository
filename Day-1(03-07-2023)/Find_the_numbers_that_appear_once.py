class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s=0
        for i in range(len(nums)):
            s=s^nums[i]
        return s
