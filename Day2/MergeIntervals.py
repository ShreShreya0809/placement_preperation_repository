class Solution:
    def fun(self, l: List[List[int]]) -> List[List[int]]:
        L = []
        n = len(l)
        if n == 0 or l is None:
            return L
        
        l.sort()
        
        arr = l[0]
        for x in l:
            if x[0] <= arr[1]:
                arr[1] = max(x[1], arr[1])
            else:
                L.append(arr)
                arr = x
        L.append(arr)
        
        return L
