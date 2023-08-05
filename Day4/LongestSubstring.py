class Solution:
    def longestSubstrDistinctChars(self, s):
        if(len(s)<1): return 0
        l,r,x=0,0,0
        Dictionary={}
        while(r<len(s)):
            if(s[r] in Dictionary and Dictionary[s[r]]>=l): l=Dictionary[s[r]]+1
            x=max(x,r-l+1)
            Dictionary[s[r]]=r
            r+=1
        return x
