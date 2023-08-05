class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        Dictionary={}
        for i in range(len(arr)):
            if(target-arr[i] in d): return [Dictionary[target-arr[i]],i]
            else: Dictionary[arr[i]]=i
        return -1
