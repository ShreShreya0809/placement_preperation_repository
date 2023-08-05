class Solution:
    def majorityElement(self,L,n):
        count=0
        x=-1
        y=0
        
        for i in L:
            if(count==0): x=i
            if(i==x): count+=1
            else: count-=1
        for i in L:
            if(i==x): y+=1
        if(y>n//2): return x
        else: return -1
 

T=int(input())
while(T>0):
  n=int(input())
  L=[int(x) for x in (input().strip()).split(" ")]
  Sol = Solution()
  print(Sol.majorityElement(L,n))
