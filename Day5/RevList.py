class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head is None): return
        a,b,c= None,head,None
        while(b):
            c=b.next
            b.next=a
            a=b
            b=c
        return a
